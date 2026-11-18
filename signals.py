"""CSV/JSONL final Portfolio Manager decisions; never parse analyst opinions."""
import re
from pathlib import Path
import numpy as np
import pandas as pd
from data import aware, schedule

REQUIRED = ["ticker","decision_time","information_cutoff","action","strategy_version","source"]
RATING_TO_ACTION = {
    "BUY": "BUY",
    "OVERWEIGHT": "BUY",
    "HOLD": "HOLD",
    "UNDERWEIGHT": "SELL",
    "SELL": "SELL",
}


def load_decisions(path):
    p=Path(path)
    if p.suffix==".csv": return pd.read_csv(p,keep_default_na=False)
    if p.suffix==".jsonl": return pd.read_json(p,lines=True,convert_dates=False)
    raise ValueError("Decision input must be CSV or JSONL")


def validate_weights(frame, ticker):
    """Read numeric targets; a blank target on an existing row means cash."""
    columns = ["ticker", "signal_date", "target_weight"]
    result = frame.loc[:, columns].copy()
    if result.empty or not result.ticker.eq(ticker).all():
        raise ValueError(f"Missing or mixed signals for {ticker}")
    dates = pd.to_datetime(result.signal_date, format="%Y-%m-%d", errors="raise")
    if dates.isna().any() or dates.duplicated().any():
        raise ValueError(f"Missing or duplicate signal dates for {ticker}")
    result["signal_date"] = dates.dt.strftime("%Y-%m-%d")
    raw = result.target_weight
    if raw.map(lambda value: isinstance(value, (bool, np.bool_))).any():
        raise ValueError("target_weight must be numeric")
    empty = raw.isna() | raw.astype(str).str.strip().str.lower().isin(["", "nan"])
    weights = pd.to_numeric(raw.mask(empty, 0), errors="raise")
    if not np.isfinite(weights).all():
        raise ValueError("target_weight must be finite")
    result["target_weight"] = weights.astype(float)
    return result.sort_values("signal_date").reset_index(drop=True)


def decision_sessions(start,end):
    s=schedule(start,end)
    if s.empty: raise ValueError("Empty evaluation interval")
    return s


def validate_decisions(d,ticker,start,end,source="portfolio_manager"):
    if not set(REQUIRED).issubset(d.columns): raise ValueError(f"Missing decision columns: {set(REQUIRED)-set(d.columns)}")
    d=d.copy()
    if d.empty: raise ValueError("Missing decisions")
    if not d.ticker.eq(ticker).all(): raise ValueError("Mixed/unexpected decision ticker")
    for k in REQUIRED:
        if d[k].isna().any() or d[k].astype(str).str.strip().eq("").any(): raise ValueError(f"Missing {k}")
    if not d.action.isin(["BUY","SELL","HOLD"]).all(): raise ValueError("Invalid action; only BUY/SELL/HOLD accepted")
    if not d.source.eq(source).all(): raise ValueError("Only final Portfolio Manager output accepted")
    if d.strategy_version.nunique()!=1: raise ValueError("Mixed strategy versions")
    times=d.decision_time.map(aware)
    cutoff=d.information_cutoff.map(aware)
    d["session"]=[t.tz_convert("America/New_York").strftime("%Y-%m-%d") for t in times]
    expected=decision_sessions(start,end)
    if d.session.duplicated().any() or set(d.session)!=set(expected.index.strftime("%Y-%m-%d")):
        raise ValueError("Duplicate/missing/extra decision sessions; all evaluation sessions required")
    for idx,row in d.iterrows():
        close=expected.loc[row.session,"close"]
        if times.loc[idx] < close or cutoff.loc[idx]>close or cutoff.loc[idx]>times.loc[idx]:
            raise ValueError("Decision before close or future information after exchange close")
    return d.sort_values("session").reset_index(drop=True)


def final_rating(state):
    text=state.get("final_trade_decision")
    if not isinstance(text,str) or not text.strip(): raise ValueError("Missing final Portfolio Manager decision")
    ratings=re.findall(r"^\*\*Rating\*\*:\s*(\w+)\s*$",text,re.M)
    rating=state.get("final_rating")
    if ratings and (len(ratings)!=1 or (rating and rating.upper()!=ratings[0].upper())):
        raise ValueError("Ambiguous/inconsistent final manager rating")
    rating=rating or (ratings[0] if len(ratings)==1 else None)
    if not isinstance(rating,str) or rating.upper() not in RATING_TO_ACTION:
        raise ValueError("Unsupported/absent final Portfolio Manager rating")
    return rating.upper()


def from_final_state(state):
    return RATING_TO_ACTION[final_rating(state)]
