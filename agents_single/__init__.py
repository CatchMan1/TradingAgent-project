"""Validate external binary target weights for the shared backtest."""

import pandas as pd

from signals import validate_weights


def validate_single_agent(rows, ticker):
    missing = {"ticker", "signal_date", "target_weight"} - set(rows.columns)
    if missing:
        raise ValueError(f"Missing single-agent decision columns: {sorted(missing)}")
    if not pd.to_numeric(rows.target_weight, errors="coerce").isin([0, 1]).all():
        raise ValueError(f"{ticker}: single-agent target_weight must be 0 or 1 on every row")
    return validate_weights(rows, ticker)
