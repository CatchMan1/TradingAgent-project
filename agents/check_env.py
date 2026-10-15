"""Fail-fast environment and data checks for the A/B handoff."""

from __future__ import annotations

import os
import sys

import pandas as pd

from data import DATA_DIR, ROOT, data_asof, schedule
from settings import load_config


def main() -> int:
    try:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env", override=False)
    except ImportError:
        pass
    errors: list[str] = []
    try:
        cfg = load_config()
    except Exception as exc:
        print(f"[failed] B config: {type(exc).__name__}: {exc}")
        return 1

    print(f"[ok] Python {sys.version.split()[0]}")
    print(f"[ok] B project: {ROOT}")
    print(f"[ok] tickers: {', '.join(cfg['tickers'])}")
    print(f"[ok] data directory: {DATA_DIR}")

    try:
        import tradingagents
        print(f"[ok] TradingAgents {tradingagents.__version__}")
    except ImportError:
        errors.append("official TradingAgents is not importable; install pinned v0.6.0")

    provider = os.getenv("TRADINGAGENTS_LLM_PROVIDER", "deepseek")
    key_name = {"deepseek": "DEEPSEEK_API_KEY", "openai": "OPENAI_API_KEY"}.get(provider)
    if key_name and not os.getenv(key_name):
        errors.append(f"{key_name} is empty; put it in a local .env (never commit it)")
    print(f"[ok] provider: {provider}")

    for ticker in cfg["tickers"]:
        try:
            start = pd.Timestamp(cfg["splits"]["train"][0])
            session = schedule(start.strftime("%Y-%m-%d"), (start + pd.Timedelta(days=14)).strftime("%Y-%m-%d"))
            cutoff = session.iloc[0]["close"]
            for kind in ("prices", "financials"):
                frame = data_asof(ticker, kind, cutoff.isoformat())
                print(f"[ok] {kind}/{ticker}: {len(frame)} rows visible at {cutoff.date()}")
        except Exception as exc:
            errors.append(f"as-of data check {ticker}: {type(exc).__name__}: {exc}")

    if errors:
        for error in errors:
            print(f"[failed] {error}")
        return 1
    print("Environment is ready for a dry-run or API run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
