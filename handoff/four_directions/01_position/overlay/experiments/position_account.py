"""Long-only account arithmetic shared by live sequential sizing and offline tests."""
from copy import deepcopy
from dataclasses import dataclass
import math
import pandas as pd
from experiments.optimization_engine import rebalance


def validate_decision(d):
    if not isinstance(d, dict) or d.get('action') not in {'keep_shares', 'rebalance'}:
        raise ValueError('Expected keep_shares or rebalance')
    w = d.get('target_weight_now')
    if d['action'] == 'keep_shares':
        if w is not None:
            raise ValueError('keep_shares requires null target')
    elif isinstance(w, bool) or not isinstance(w, (int, float)) or not math.isfinite(w) or not 0 <= w <= 1:
        raise ValueError('Target must be a finite number in [0,1]')
    for key in ['rationale', 'why_change_from_current', 'increase_condition', 'reduce_condition']:
        if not isinstance(d.get(key), str) or not d[key].strip():
            raise ValueError(f'Missing {key}')
    return d


@dataclass
class Account:
    cash: float = 100000.
    shares: float = 0.
    average_cost: float = 0.
    realized_pnl: float = 0.
    dividends: float = 0.
    fees: float = 0.

    def equity(self, price):
        if not math.isfinite(price) or price <= 0:
            raise ValueError('Invalid price')
        return self.cash + self.shares * price

    def snapshot(self, day, price, recent_trades):
        equity = self.equity(price)
        return dict(as_of=day, currency='USD', mark_price=price, total_equity=equity,
                    cash=self.cash, shares=self.shares, current_weight=self.shares * price / equity,
                    average_cost_including_buy_fees=self.average_cost,
                    unrealized_pnl=(price-self.average_cost)*self.shares,
                    realized_pnl=self.realized_pnl, cumulative_dividends=self.dividends,
                    cumulative_trading_fees=self.fees, recent_trades=recent_trades[-5:])

    def corporate_actions(self, row):
        split, dividend = float(row['split']), float(row['dividend'])
        if not math.isfinite(split) or split <= 0 or not math.isfinite(dividend):
            raise ValueError('Invalid corporate action')
        self.shares *= split
        self.average_cost /= split
        distribution = self.shares * dividend
        self.cash += distribution
        self.dividends += distribution
        return distribution

    def trade(self, price, target, fee_bps=10.):
        equity = self.equity(price)
        if equity <= 0 or not 0 <= fee_bps < 1000:
            raise ValueError('Invalid equity or fees')
        if target is None:
            return dict(traded_shares=0., traded_notional=0., trading_cost=0., turnover=0.)
        if isinstance(target, bool) or not math.isfinite(target) or not 0 <= target <= 1:
            raise ValueError('Invalid target')
        notional, cost = rebalance(equity, self.shares*price, target, fee_bps/10000)
        new_shares = notional / price
        delta = new_shares - self.shares
        if delta > 0:
            self.average_cost = (self.shares*self.average_cost + delta*price + cost) / new_shares
        elif delta < 0:
            self.realized_pnl += (-delta)*(price-self.average_cost)-cost
        self.cash -= delta*price + cost
        self.shares = new_shares
        self.fees += cost
        if new_shares == 0:
            self.average_cost = 0.
        if self.cash < -1e-7 or self.shares < 0:
            raise ValueError('Trade violates long-only/cash constraints')
        return dict(traded_shares=delta, traded_notional=abs(delta)*price,
                    trading_cost=cost, turnover=abs(delta)*price/equity)


def execute_interval(account, decision, signal_date, execution, following, terminal=False, fee_bps=10.):
    """Mutate account through execution only; value a clone at the following open.

    The live account remains on the execution day so the next decision cannot
    observe the next open, dividend, split, or liquidation prematurely.
    """
    validate_decision(decision)
    account.corporate_actions(execution)
    opening = float(execution['open'])
    trade = account.trade(opening, decision['target_weight_now'], fee_bps)
    weight = account.shares*opening/account.equity(opening)
    projected = deepcopy(account)
    distribution = projected.corporate_actions(following)
    next_open = float(following['open'])
    liquidation_fee = 0.
    if terminal:
        end_trade = projected.trade(next_open, 0., fee_bps)
        liquidation_fee = end_trade['trading_cost']
    row = dict(signal_date=signal_date, execution_date=execution['date'],
               valuation_date=following['date'], action=decision['action'],
               target_weight=decision['target_weight_now'], actual_weight=weight,
               shares_after_execution=account.shares, cash_after_execution=account.cash,
               average_cost_after_execution=account.average_cost,
               equity=projected.equity(next_open), dividend_cash=distribution,
               **trade)
    row['trading_cost'] += liquidation_fee
    if terminal:
        # Same turnover denominator convention as the original experiment.
        pre_trade_equity = account.equity(opening) + trade['trading_cost']
        row['turnover'] += end_trade['traded_notional']/pre_trade_equity
    return row


def metrics(rows, initial_cash=100000.):
    frame = pd.DataFrame(rows)
    values = pd.Series([initial_cash, *frame.equity])
    returns = values.pct_change().dropna()
    std = returns.std(ddof=0)
    return dict(total_return=float(values.iloc[-1]/initial_cash-1),
                max_drawdown=float((values/values.cummax()-1).min()),
                sharpe=float(returns.mean()/std*math.sqrt(252)) if std > 0 else None,
                trading_cost=float(frame.trading_cost.sum()), turnover=float(frame.turnover.sum()),
                final_equity=float(values.iloc[-1]), sessions=len(rows),
                mean_exposure=float(frame.actual_weight.mean()))
