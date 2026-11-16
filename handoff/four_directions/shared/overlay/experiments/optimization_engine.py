"""Signed-share, next-open simulator for the optimization ablation.

No model calls. HOLD retains shares, not a daily rebalanced weight. Fees are
charged on actual traded notional. Short proceeds stay in the account.
"""
from __future__ import annotations

import math
import pandas as pd


def target_weight(rating, previous_weight, fractional=False, short=False):
    if rating not in {"Buy", "Overweight", "Hold", "Underweight", "Sell"}:
        raise ValueError(f"Unusable rating: {rating}")
    if rating == "Hold":
        return None
    if rating == "Buy":
        return 1.0
    if rating == "Overweight":
        return .5 if fractional else 1.0
    if rating == "Sell":
        return -1.0 if short else 0.0
    # Underweight trims an existing long; never creates a new long from cash.
    return min(.25, max(0., previous_weight)) if fractional else 0.0


def rebalance(equity, old_notional, target, fee):
    """Solve target * post-fee equity exactly, including long/short reversals."""
    if equity <= 0 or not -1 <= target <= 1 or not 0 <= fee < .1:
        raise ValueError("Invalid equity, target, or fee")
    lo, hi = 0., equity
    for _ in range(80):
        cost = (lo + hi) / 2
        required = fee * abs(target * (equity - cost) - old_notional)
        if cost < required:
            lo = cost
        else:
            hi = cost
    cost = (lo + hi) / 2
    return target * (equity - cost), cost


def simulate(prices, ratings, start, end, *, fractional=False, short=False,
             fee_bps=10., borrow_apr=.03, initial_cash=100000.,
             short_authorizations=None, maintenance_margin=.30):
    """Trade opens in [start,end], value at the following open, then liquidate.

    Rating keys must be the immediately preceding price session. Missing cells
    fail closed. Dividends on the interval's ending ex-date accrue to the old
    holder (negative for a short). Splits adjust shares before that dividend.
    Borrow accrues on opening short notional over actual calendar days / 365.
    No interest on cash/collateral, no borrow locate/slippage market-impact model.
    """
    p = prices.copy().sort_values("date").reset_index(drop=True)
    p["date"] = p.date.astype(str).str[:10]
    if p.date.duplicated().any():
        raise ValueError("Duplicate price sessions")
    if not math.isfinite(initial_cash) or initial_cash <= 0 or not 0 <= borrow_apr <= 1:
        raise ValueError("Invalid initial cash or borrow rate")
    fee = fee_bps / 10000
    if not 0 <= fee < .1:
        raise ValueError("Invalid fees")
    indices = p.index[(p.date >= start) & (p.date <= end)].tolist()
    if not indices or indices[0] == 0 or indices[-1] + 1 >= len(p):
        raise ValueError("Need previous signal session and final valuation open")
    cash, shares = initial_cash, 0.
    rows = []
    for i in indices:
        today, following = p.iloc[i], p.iloc[i+1]
        signal = p.iloc[i-1].date
        if signal not in ratings:
            raise ValueError(f"Missing decision for {signal}")
        opening, next_open = float(today.open), float(following.open)
        split, dividend = float(following.split), float(following.dividend)
        if not all(math.isfinite(v) for v in [opening, next_open, split, dividend]) or min(opening, next_open, split) <= 0:
            raise ValueError("Invalid market data")
        equity = cash + shares * opening
        if equity <= 0:
            raise ValueError("Insolvent account; experiment cannot continue")
        previous_weight = shares * opening / equity
        target = target_weight(ratings[signal], previous_weight, fractional, short)
        margin_cover = False
        if short and short_authorizations is not None:
            if fractional:raise ValueError('Discrete short extension excludes fractional sizing')
            approved=short_authorizations[signal]
            if type(approved) is not bool:raise ValueError('Explicit boolean short authorization required')
            if approved and ratings[signal] not in {'Underweight','Sell'}:
                raise ValueError('Short overlay may only override original exit decisions')
            target=-1. if approved else target_weight(ratings[signal],previous_weight,False,False)
            # Old Hold referred to the old long/flat portfolio, never an approved short.
            if target is None and shares<0:target=0.
            margin_cover=shares<0 and equity/abs(shares*opening)<maintenance_margin
            if margin_cover:target=0.
        old_shares = shares
        cost = 0.
        if target is not None:
            notional, cost = rebalance(equity, shares * opening, target, fee)
            shares = notional / opening
            cash -= (shares - old_shares) * opening + cost
        turnover = abs(shares-old_shares)*opening/equity
        days = (pd.Timestamp(following.date)-pd.Timestamp(today.date)).days
        borrow = max(0., -shares * opening) * borrow_apr * days / 365
        cash -= borrow
        weight = shares * opening / (equity - cost)
        shares *= split
        distribution = shares * dividend
        cash += distribution
        liquidation_fee = 0.
        if i == indices[-1]:
            liquidation_fee = abs(shares * next_open) * fee
            turnover += abs(shares * next_open) / equity
            cash += shares * next_open - liquidation_fee
            shares = 0.
        value = cash + shares * next_open
        if value <= 0:
            raise ValueError("Insolvent short account; losses exceed equity")
        rows.append(dict(signal_date=signal, execution_date=today.date,
                         valuation_date=following.date, rating=ratings[signal],
                         target_weight=target, actual_weight=weight,
                         shares=shares, cash=cash, equity=value,
                         net_return=value/equity-1, turnover=turnover,
                         trading_cost=cost+liquidation_fee, borrow_cost=borrow,
                         dividend_cash=distribution, margin_cover=margin_cover))
    frame = pd.DataFrame(rows)
    values = pd.Series([initial_cash, *frame.equity])
    drawdown = values / values.cummax()-1
    std = frame.net_return.std(ddof=0)
    metrics = dict(total_return=frame.equity.iloc[-1]/initial_cash-1,
                   max_drawdown=float(drawdown.min()),
                   sharpe=float(frame.net_return.mean()/std*math.sqrt(252)) if std > 0 else None,
                   turnover=float(frame.turnover.sum()),
                   trading_cost=float(frame.trading_cost.sum()),
                   borrow_cost=float(frame.borrow_cost.sum()),
                   short_days=int((frame.actual_weight < 0).sum()),
                   sessions=len(frame), final_equity=float(frame.equity.iloc[-1]))
    return frame, metrics
