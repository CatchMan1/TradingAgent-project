"""原版和变体共用的信号对齐、回测公式、评价和结果导出。"""
import json
from itertools import cycle

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from data import schedule, total_return_index, validate_prices
from signals import decision_sessions, load_decisions, validate_decisions


def select_period(frame, start, end):
    session_date = pd.to_datetime(frame.date)
    return_date = frame.return_end.dt.tz_localize(None).dt.normalize()
    mask = session_date.between(start, end) & return_date.le(pd.Timestamp(end))
    selected = frame.loc[mask].dropna(subset=["pct", "return_end"]).copy()
    if selected.empty:
        raise ValueError(f"{start} 至 {end} 没有可回测收益区间")
    return selected


def calculate_indicators(prices, cfg, end):
    p = prices.loc[prices.date <= end].copy().set_index("date", drop=False)
    p["technical_index"] = total_return_index(p)
    tr = p.technical_index
    fast, slow = cfg["sma"]["fast"], cfg["sma"]["slow"]
    p["sma_fast"] = tr.rolling(fast, min_periods=fast).mean()
    p["sma_slow"] = tr.rolling(slow, min_periods=slow).mean()
    p["sma_score"] = p.sma_fast - p.sma_slow
    fast, slow, signal = (cfg["macd"][k] for k in ["fast", "slow", "signal"])
    p["macd"] = (tr.ewm(span=fast, adjust=False, min_periods=fast).mean()
                 - tr.ewm(span=slow, adjust=False, min_periods=slow).mean())
    p["macd_signal"] = p.macd.ewm(span=signal, adjust=False, min_periods=signal).mean()
    p["macd_score"] = p.macd - p.macd_signal
    return p


def baseline_signals(indicators, ticker, strategy, start, end, cfg):
    sessions = decision_sessions(start, end)
    days = sessions.index.strftime("%Y-%m-%d")
    if strategy == "buy_hold":
        actions = np.full(len(days), "HOLD", dtype=object)
        actions[0] = "BUY"
    elif strategy in ["sma", "macd"]:
        score = indicators.reindex(days)[f"{strategy}_score"]
        if not np.isfinite(score.to_numpy()).all():
            raise ValueError("指标预热不足或缺少信号日行情")
        actions = np.select([score > 0, score < 0], ["BUY", "SELL"], default="HOLD")
    else:
        raise ValueError("未知基线")
    frame = pd.DataFrame({
        "ticker": ticker,
        "decision_time": [close.isoformat() for close in sessions.close],
        "information_cutoff": [close.isoformat() for close in sessions.close],
        "action": actions, "strategy_version": f"{strategy}-v1",
        "source": "baseline",
    })
    return validate_decisions(frame, ticker, start, end, source="baseline")


def signals(prices, ticker, strategy, start, end, cfg):
    # 供规则切换和关键测试复用。
    indicators = calculate_indicators(prices, cfg, end)
    return baseline_signals(indicators, ticker, strategy, start, end, cfg)


def prepare_backtest(prices, decisions, return_type="simple"):
    if prices.empty:
        raise ValueError("Empty backtest prices")
    p = validate_prices(prices, str(prices.date.iloc[0]), str(prices.date.iloc[-1]))
    d = decisions.copy().reset_index(drop=True)
    expected = decision_sessions(p.date.iloc[0], p.date.iloc[-1]).index.strftime("%Y-%m-%d").tolist()
    if "target_weight" in d:
        # 仅需要足以覆盖实际收益区间的信号，不补造期末决策。
        sessions = d.signal_date.tolist()
        if sessions != expected[:len(d)] or len(d) < len(p) - 1:
            raise ValueError("Missing/duplicate/unsorted numeric decisions")
        d["signal_session"] = d.signal_date
        d["signal"] = d.target_weight.astype(float)
        executed = d.iloc[:len(p)-1][["signal_session", "signal"]].copy()
        executed["date"] = executed.signal_session
    else:
        if d.session.tolist() != expected or not d.action.isin(["BUY", "SELL", "HOLD"]).all():
            raise ValueError("Missing/duplicate/unsorted/invalid decisions")
        columns = ["session", "action", "decision_time", "information_cutoff", "strategy_version", "source"]
        d = d.filter(items=columns)
        d["signal"] = d.action.map({"BUY": 1., "SELL": 0., "HOLD": np.nan}).ffill().fillna(0.)
        d["date"] = d.session
        executed = d.iloc[:-1].rename(columns={"session": "signal_session"}).copy()
    executed["target_position"] = executed.signal.clip(-1., 1.)
    frame = p.merge(executed, on="date", how="left", validate="one_to_one")
    sessions = schedule(p.date.iloc[0], p.date.iloc[-1])
    frame.index = pd.DatetimeIndex(sessions.close.dt.tz_convert("America/New_York"), name="DateTime")
    if "decision_time" in frame:
        frame.rename(columns={"decision_time": "archived_decision_time"}, inplace=True)
    frame["decision_time"] = frame.index
    frame["return_end"] = pd.Series(frame.index, index=frame.index).shift(-1)
    frame["asset_ret"] = (frame.close.shift(-1) - frame.close) / frame.close
    if return_type not in ["simple", "log"]:
        raise ValueError("未知收益率类型")
    frame["pct"] = frame.asset_ret if return_type == "simple" else np.log1p(frame.asset_ret)
    frame["position"] = frame.target_position
    return frame.dropna(subset=["pct", "return_end"]).copy()


def cal_net_values(post, ret, fee=0.001, return_type="simple",
                   nav_mode="additive", initial_position=0.):
    """仓位×下一期资产收益－换手费用；Agent和规则策略共用。"""
    post = np.asarray(post, dtype=float)
    ret = np.asarray(ret, dtype=float)
    post = np.clip(post, -1., 1.)
    initial_position = np.clip(initial_position, -1., 1.)
    if return_type == "log":
        ret = np.expm1(ret)
    elif return_type != "simple":
        raise ValueError("收益类型为 simple/log")

    position_changes = np.diff(np.r_[initial_position, post])
    strategy_ret = post * ret - np.abs(position_changes) * fee
    if nav_mode == "additive":
        net_values = 1 + strategy_ret.cumsum()
    elif nav_mode == "compound":
        net_values = (1 + strategy_ret).cumprod()
    else:
        raise ValueError("净值口径为 additive/compound")
    return net_values, strategy_ret


def calculate_mdd(net_values):
    nav = np.r_[1., np.asarray(net_values, dtype=float)]
    drawdown = nav / np.maximum.accumulate(nav) - 1
    index = int(drawdown.argmin())
    return float(drawdown[index]), max(0, index - 1)


def calculate_sharpe(daily_ret, rf=0., periods=252):
    excess = np.asarray(daily_ret, dtype=float) - rf / periods
    std = excess.std(ddof=0)
    return float(excess.mean() / std * np.sqrt(periods)) if len(excess) > 1 and std > 1e-14 else np.nan


def run_backtest(frame, fee, return_type="simple", nav_mode="additive", exclude_periods=()):
    df = frame.copy()
    df["position"] = df.position.clip(-1., 1.)
    df["position_changes"] = df.position.diff().fillna(df.position.iloc[0])
    df["turnover"] = df.position_changes.abs()
    df["cost"] = df.turnover * fee
    df["net_values"], df["strategy_ret"] = cal_net_values(
        df.position, df.pct, fee, return_type, nav_mode)
    # 先按完整仓位计算真实区间收益和费用，再做事后日期筛选。
    # 不先删行情，也不在筛选后的仓位间重新计算换手。
    if exclude_periods:
        starts = df.index.tz_localize(None).normalize()
        ends = df.return_end.dt.tz_localize(None).dt.normalize()
        keep = pd.Series(True, index=df.index)
        for start, end in exclude_periods:
            start, end = pd.Timestamp(start), pd.Timestamp(end)
            if start > end:
                raise ValueError("排除区间的开始日期不能晚于结束日期")
            keep &= ~((starts <= end) & (ends >= start))
        df = df.loc[keep].copy()
        if df.empty:
            raise ValueError("筛选后没有剩余收益区间")
        df["net_values"] = (1 + df.strategy_ret.cumsum() if nav_mode == "additive"
                            else (1 + df.strategy_ret).cumprod())
    df["running_peak"] = df.net_values.cummax().clip(lower=1.)
    df["drawdown"] = df.net_values / df.running_peak - 1
    return df


def evaluate_backtest(df, nav_mode="additive", annualization=252, risk_free_rate=0.):
    dates = df.return_end.dt.normalize()
    if nav_mode == "compound":
        daily_ret = (1 + df.strategy_ret).groupby(dates).prod() - 1
    else:
        daily_ret = df.strategy_ret.groupby(dates).sum()
    max_drawdown, _ = calculate_mdd(df.net_values)
    metrics = pd.Series({
        "cumulative_return": df.net_values.iloc[-1] - 1,
        "max_drawdown": max_drawdown,
        "sharpe": calculate_sharpe(daily_ret, rf=risk_free_rate, periods=annualization),
        "annualized_volatility": daily_ret.std(ddof=0) * np.sqrt(annualization) if len(daily_ret) > 1 else np.nan,
        "position_change_count": int(df.turnover.gt(0).sum()),
        "turnover_sum": df.turnover.sum(), "cost_sum": df.cost.sum(),
        "return_intervals": len(df), "return_days": len(daily_ret),
    })
    if "action" in df:
        direction = df.action.map({"BUY": 1, "SELL": -1})
        calls = direction.notna()
        metrics["directional_calls"] = calls.sum()
        metrics["directional_accuracy"] = (direction[calls] * df.pct[calls] > 0).mean()
    return metrics


def plot_backtest(backtests, strategy_names, metrics_table, title, nav_mode="additive", *, axes=None):
    first = next(iter(backtests.values()))
    index = pd.DatetimeIndex([first.index[0], *first.return_end])
    curves = pd.DataFrame({
        strategy: np.r_[1., frame.net_values.to_numpy()]
        for strategy, frame in backtests.items()
    }, index=index)
    order = [s for s in ["agent", "buy_hold", "sma", "macd"] if s in curves]
    curves = curves[order + [s for s in curves if s not in order]]

    # Break the display across excluded intervals and resume at the next included close.
    gap = first.index[1:] != index[1:-1]
    gap_left, gap_right = index[1:-1][gap], first.index[1:][gap]
    plot_curves = curves
    if len(gap_right):
        gap_mid = gap_left + (gap_right - gap_left) / 2
        plot_curves = curves.reindex(index.union(gap_right).union(gap_mid))
        plot_curves.loc[gap_right] = curves.loc[gap_left].to_numpy()
    drawdowns = (plot_curves / plot_curves.cummax() - 1) * 100
    styles = {
        "agent": ("#1f77b4", "-", 2.1),
        "buy_hold": ("#808080", "-", 1.5),
        "sma": ("#a65b27", "-.", 1.15),
        "macd": ("#7152a0", ":", 1.35),
    }

    if axes is None:
        fig, (ax_nav, ax_dd) = plt.subplots(
            2, 1, figsize=(14, 8), sharex=True, constrained_layout=True)
        fig.suptitle(f"{title} | {index[0]:%Y-%m-%d} to {index[-1]:%Y-%m-%d}", fontsize=14)
    else:
        ax_nav, ax_dd = axes
        fig = ax_nav.figure

    variant_colors = cycle(plt.get_cmap("tab10").colors[3:])
    for strategy in curves:
        color, linestyle, width = (styles[strategy] if strategy in styles
                                  else (next(variant_colors), "-", 1.6))
        label = strategy_names[strategy]
        ax_nav.plot(plot_curves.index, plot_curves[strategy], color=color,
                    linestyle=linestyle, linewidth=width, label=label,
                    zorder=4 if strategy == "agent" else 3)
        ax_dd.fill_between(plot_curves.index, drawdowns[strategy], 0, color=color,
                           alpha=.15, linewidth=0, zorder=1)
        ax_dd.plot(plot_curves.index, drawdowns[strategy], color=color,
                   linestyle=linestyle, linewidth=.85, alpha=.85,
                   label=label)

    sharpe_names = strategy_names if axes is None else {"agent": "Strategy", "buy_hold": "Buy and Hold"}
    sharpe_text = " vs ".join(
        f"{sharpe_names[s]} {metrics_table.loc[s, 'sharpe']:+.2f}"
        for s in ["agent", "buy_hold"] if s in curves)
    sharpe_title = f"Sharpe {sharpe_text}" if sharpe_text else ""
    ax_nav.set_title(sharpe_title if axes is None else f"{title}\n{sharpe_title}", fontsize=10)
    ax_nav.set_ylabel(f"NAV ({nav_mode}, start = 1)")
    ax_nav.axhline(1, color="black", linewidth=.7)
    ax_nav.legend(loc="upper left", fontsize=9)
    ax_nav.tick_params(axis="x", labelbottom=True)
    ax_dd.set_title("Drawdown" if axes is None else f"{title} drawdown", fontsize=11)
    ax_dd.set_ylabel("Drawdown (%)")
    ax_dd.axhline(0, color="black", linewidth=.7)
    ax_dd.legend(loc="lower left", fontsize=9)
    for ax in (ax_nav, ax_dd):
        ax.set_facecolor("white")
        ax.set_axisbelow(True)
        ax.grid(True, color="#d0d0d0", linewidth=.8, alpha=.55)
        ax.margins(x=.02)
        ax.tick_params(axis="x", labelrotation=25)
    ax_dd.xaxis.set_major_locator(mdates.AutoDateLocator(tz=index.tz, minticks=3, maxticks=5))
    ax_dd.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d", tz=index.tz))
    return fig, curves


def build_baselines(price_histories, cfg, backtest_start, backtest_end):
    baseline_tables = {}
    for ticker, prices in price_histories.items():
        indicators = calculate_indicators(prices, cfg, backtest_end)
        baseline_tables[ticker] = {
            strategy: baseline_signals(indicators, ticker, strategy, backtest_start, backtest_end, cfg)
            for strategy in ["buy_hold", "sma", "macd"]
        }
    return baseline_tables


def save_baselines(baseline_tables, root, backtest_start, backtest_end, cfg):
    baseline_paths = {}
    for ticker, tables in baseline_tables.items():
        path = root / "data/decisions" / f"baseline_{ticker}_agent_period.csv"
        path.parent.mkdir(parents=True, exist_ok=True)
        exported = pd.concat([rows.assign(strategy=strategy) for strategy, rows in tables.items()], ignore_index=True)
        sessions = decision_sessions(backtest_start, backtest_end)
        execution_dates = dict(zip(sessions.index.strftime("%Y-%m-%d"),
                                  sessions.close.dt.tz_convert(cfg["timezone"])))
        exported["DateTime"] = exported.session.map(execution_dates)
        exported.to_csv(path, index=False)
        baseline_paths[ticker] = path
    return baseline_paths


def load_baselines(baseline_paths, backtest_start, backtest_end):
    decision_tables = {}
    for ticker, path in baseline_paths.items():
        baseline_input = load_decisions(path)
        if set(baseline_input.ticker) != {ticker} or set(baseline_input.strategy) != {"buy_hold", "sma", "macd"}:
            raise ValueError("Missing/extra baseline stocks or strategies in CSV")
        for strategy, rows in baseline_input.groupby("strategy", sort=False):
            decision_tables[ticker, strategy] = validate_decisions(
                rows, ticker, backtest_start, backtest_end, source="baseline")
    return decision_tables


def load_original(agent_csv, tickers, start, end):
    imported = load_decisions(agent_csv)
    if not set(imported.ticker).issubset(tickers):
        raise ValueError("Agent CSV 含未知股票")
    return {
        (ticker, "agent"): validate_decisions(imported.loc[imported.ticker == ticker], ticker, start, end)
        for ticker in tickers
    }


def original_frames(price_histories, decision_tables, start, end, return_type):
    prices = {ticker: frame.loc[frame.date.between(start, end)]
              for ticker, frame in price_histories.items()}
    return {(ticker, strategy): prepare_backtest(prices[ticker], decisions, return_type)
            for (ticker, strategy), decisions in decision_tables.items()}


def compare_positions(position_tables, strategy_names, cfg, fee, return_type, nav_mode, exclude_periods):
    backtests = {key: run_backtest(frame, fee, return_type=return_type, nav_mode=nav_mode,
                                  exclude_periods=exclude_periods)
                 for key, frame in position_tables.items()}
    metrics_table = pd.DataFrame([
        {"ticker": ticker, "period": period, "strategy": strategy,
         "strategy_name": strategy_names[strategy],
         **evaluate_backtest(frame, nav_mode=nav_mode, annualization=cfg["annualization"],
                             risk_free_rate=cfg["risk_free_rate"]).to_dict()}
        for (ticker, period, strategy), frame in backtests.items()
    ]).set_index(["ticker", "period", "strategy"])
    return backtests, metrics_table


def monthly_strategy_returns(backtests, nav_mode):
    monthly_tables = {}
    for key, frame in backtests.items():
        interval_ret = pd.Series(frame.strategy_ret.to_numpy(), index=pd.DatetimeIndex(frame.return_end))
        monthly_tables[key] = ((1 + interval_ret).resample("ME").prod() - 1
                               if nav_mode == "compound" else interval_ret.resample("ME").sum())
    monthly_returns = pd.concat(monthly_tables, names=["ticker", "period", "strategy", "month"]).rename("return")
    return monthly_returns


def save_results(output_dir, cases, metrics_table, monthly_returns, figures, record):
    """Export one experiment with its own date windows and input manifest."""
    output_dir.mkdir(parents=True, exist_ok=True)
    keys = [(ticker, period, strategy) for (ticker, period), frames in cases.items()
            for strategy in frames]
    metrics_table.loc[keys].to_csv(output_dir / "metrics.csv")
    month_mask = monthly_returns.index.droplevel("month").isin(keys)
    monthly_returns.loc[month_mask].to_csv(output_dir / "monthly_returns.csv")

    for (ticker, period), frames in cases.items():
        for strategy, frame in frames.items():
            folder = output_dir / ticker / period / strategy
            folder.mkdir(parents=True, exist_ok=True)
            frame.to_csv(folder / "daily.csv")
            trades = frame.loc[frame.turnover > 0,
                               ["signal_session", "date", "close", "position_changes", "position", "cost"]]
            trades.to_csv(folder / "position_changes.csv")
        figures[ticker, period].savefig(output_dir / ticker / f"{period}_equity_drawdown.png",
                                       dpi=120, bbox_inches="tight")

    (output_dir / "run.json").write_text(json.dumps(record, ensure_ascii=False, indent=2))
