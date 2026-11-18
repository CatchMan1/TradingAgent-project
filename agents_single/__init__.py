"""Import external single-agent decisions for the shared backtest."""

from data import aware
from signals import REQUIRED, validate_decisions


def validate_single_agent(rows, ticker):
    missing = set(REQUIRED) - set(rows.columns)
    if missing:
        raise ValueError(f"Missing single-agent decision columns: {sorted(missing)}")
    if len(rows) < 3:
        raise ValueError(f"{ticker}: single-agent decisions need a seed session and at least two evaluation sessions")
    sessions = sorted(
        aware(value).tz_convert("America/New_York").strftime("%Y-%m-%d")
        for value in rows.decision_time
    )
    return validate_decisions(
        rows.loc[:, REQUIRED], ticker, sessions[1], sessions[-1], source="single_agent"
    )
