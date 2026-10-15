"""Expose B's frozen, point-in-time data through TradingAgents data tools.

The official graph is left untouched. At process startup A registers one local
vendor in the official router and points the market/fundamental tools at it.
This prevents an historical run from silently fetching today's Yahoo/SEC view.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from data import DATA_DIR, data_asof, schedule


_DATA_DIR = DATA_DIR


def _cutoff(date: str) -> str:
    # Match run_agents' information_cutoff, including early-close sessions.
    # Midnight would expose filings accepted after the simulated market close.
    sessions = schedule(date, date)
    if sessions.empty:
        raise ValueError(f"{date} is not an NYSE trading session")
    return sessions.iloc[0]["close"].tz_convert("America/New_York").isoformat()


def _prices(ticker: str, end_date: str) -> pd.DataFrame:
    return data_asof(ticker, "prices", _cutoff(end_date), data_dir=_DATA_DIR)


def get_stock_data(ticker: str, start_date: str, end_date: str) -> str:
    frame = _prices(ticker, end_date)
    frame = frame.loc[frame.date.between(start_date, end_date)]
    if frame.empty:
        raise ValueError(f"No cached B-project prices for {ticker} from {start_date} to {end_date}")
    return (
        f"# B-project point-in-time stock data for {ticker} from {start_date} to {end_date}\n"
        f"# Total records: {len(frame)}\n\n{frame.to_csv(index=False)}"
    )


_INDICATOR_HELP = {
    "close_50_sma": "50-day simple moving average",
    "close_200_sma": "200-day simple moving average",
    "close_10_ema": "10-day exponential moving average",
    "macd": "MACD line",
    "macds": "MACD signal line",
    "macdh": "MACD histogram",
    "rsi": "relative strength index",
    "boll": "Bollinger middle band",
    "boll_ub": "Bollinger upper band",
    "boll_lb": "Bollinger lower band",
    "atr": "average true range",
    "vwma": "volume-weighted moving average",
    "mfi": "money flow index",
}


def _stockstats(ticker: str, as_of_date: str):
    from stockstats import wrap

    frame = _prices(ticker, as_of_date).copy()
    frame = frame.rename(columns={name: name.capitalize() for name in ["open", "high", "low", "close", "volume"]})
    frame["Date"] = pd.to_datetime(frame.pop("date"))
    return wrap(frame)


def get_indicators(ticker: str, indicator: str, as_of_date: str, look_back_days: int) -> str:
    if indicator not in _INDICATOR_HELP:
        raise ValueError(f"Unsupported indicator {indicator!r}; choose from {sorted(_INDICATOR_HELP)}")
    frame = _stockstats(ticker, as_of_date)
    frame[indicator]
    start = pd.Timestamp(as_of_date) - pd.Timedelta(days=int(look_back_days))
    view = frame.loc[frame["Date"].between(start, pd.Timestamp(as_of_date)), ["Date", indicator]].copy()
    view["Date"] = view["Date"].dt.strftime("%Y-%m-%d")
    return (
        f"## {indicator}: {_INDICATOR_HELP[indicator]}\n"
        "Source: B-project cached OHLCV, filtered to the simulated date.\n\n"
        + view.to_csv(index=False)
    )


def get_verified_market_snapshot(
    symbol: str,
    curr_date: str,
    look_back_days: int = 30,
    trade_date: str = "",
) -> str:
    effective = min(curr_date, trade_date) if trade_date else curr_date
    raw = _prices(symbol, effective)
    recent = raw.tail(max(1, int(look_back_days))).copy()
    stats = _stockstats(symbol, effective)
    indicator_values = {}
    for name in ("close_50_sma", "close_200_sma", "close_10_ema", "macd", "macds", "macdh", "rsi", "boll", "boll_ub", "boll_lb", "atr", "vwma", "mfi"):
        try:
            stats[name]
            value = stats.iloc[-1][name]
            indicator_values[name] = None if pd.isna(value) else round(float(value), 6)
        except Exception:
            indicator_values[name] = None
    return (
        f"# Verified B-project snapshot for {symbol} as of {effective}\n"
        "This snapshot is computed only from locally frozen rows visible by the simulated date.\n\n"
        "## Latest OHLCV and recent rows\n"
        + recent.to_csv(index=False)
        + "\n## Indicators on the latest visible session\n"
        + pd.DataFrame([indicator_values]).to_csv(index=False)
    )


def _facts(ticker: str, date: str) -> pd.DataFrame:
    frame = data_asof(ticker, "financials", _cutoff(date), data_dir=_DATA_DIR)
    if frame.empty:
        raise ValueError(f"No B-project financial facts visible for {ticker} by {date}")
    return frame


def _format_facts(ticker: str, date: str, title: str, pattern: str | None = None) -> str:
    frame = _facts(ticker, date)
    if pattern:
        selected = frame.loc[frame.tag.str.contains(pattern, case=False, regex=True, na=False)]
        if not selected.empty:
            frame = selected
    # Latest public versions first, then cap the prompt payload. The complete
    # frame remains in B's data package and its hash is recorded in the run log.
    columns = [name for name in ["tag", "unit", "start", "end", "val", "form", "filed", "accepted_at", "accn"] if name in frame]
    frame = frame.sort_values(["accepted_at", "tag"], ascending=[False, True]).head(160)
    return (
        f"# {title} for {ticker}, public by {date}\n"
        "Source: B-project cached SEC facts; rows are filtered by actual EDGAR acceptance time.\n\n"
        + frame[columns].to_csv(index=False)
    )


def get_fundamentals(ticker: str, date: str) -> str:
    return _format_facts(ticker, date, "Point-in-time SEC fundamental facts")


def get_balance_sheet(ticker: str, freq: str, date: str) -> str:
    pattern = r"asset|liabilit|equity|cash|inventory|receivable|debt"
    return _format_facts(ticker, date, f"Balance-sheet facts ({freq})", pattern)


def get_cashflow(ticker: str, freq: str, date: str) -> str:
    pattern = r"cashflow|cashprovided|cashused|operatingactivities|investingactivities|financingactivities|payments|proceeds|capitalexpenditure"
    return _format_facts(ticker, date, f"Cash-flow facts ({freq})", pattern)


def get_income_statement(ticker: str, freq: str, date: str) -> str:
    pattern = r"revenue|sales|income|loss|expense|earningspershare|grossprofit|operating"
    return _format_facts(ticker, date, f"Income-statement facts ({freq})", pattern)


def get_insider_transactions(ticker: str, date: str | None = None) -> str:
    return (
        "DATA_UNAVAILABLE: the B-project data package has no authorized, "
        f"point-in-time insider-transactions archive for {ticker} by {date}. "
        "Do not infer or fabricate insider activity."
    )


def install(data_dir: str | Path = DATA_DIR) -> None:
    """Register this module as the official graph's `course_project` vendor."""
    global _DATA_DIR
    _DATA_DIR = Path(data_dir)

    from tradingagents.agents import tools
    from tradingagents.dataflows import router

    methods = {
        "get_stock_data": get_stock_data,
        "get_indicators": get_indicators,
        "get_fundamentals": get_fundamentals,
        "get_balance_sheet": get_balance_sheet,
        "get_cashflow": get_cashflow,
        "get_income_statement": get_income_statement,
        "get_insider_transactions": get_insider_transactions,
    }
    for name, function in methods.items():
        router.VENDOR_METHODS[name]["course_project"] = function

    # This verification tool bypasses the router upstream, so update the
    # StructuredTool object in place; the market analyst holds this same object.
    tools.get_verified_market_snapshot.func = get_verified_market_snapshot
