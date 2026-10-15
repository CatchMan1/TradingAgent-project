"""Sequential, resumable batch runner for A -> B decision generation."""

from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path

import pandas as pd

from data import DATA_DIR, ROOT, schedule
from settings import load_config

from .run_agents import DEFAULT_STRATEGY, append_decision, run_one


FIELDS = ["ticker", "decision_time", "information_cutoff", "action", "strategy_version", "source"]


def _dates(start: str, end: str) -> list[str]:
    """Return B's required seed session followed by every session in the range."""
    sessions = schedule(start, end)
    if sessions.empty:
        raise ValueError(f"No NYSE sessions between {start} and {end}")
    previous = schedule(
        (sessions.index[0] - pd.Timedelta(days=14)).strftime("%Y-%m-%d"),
        (sessions.index[0] - pd.Timedelta(days=1)).strftime("%Y-%m-%d"),
    )
    if previous.empty:
        raise ValueError("Could not find the seed session before the requested interval")
    return [previous.index[-1].strftime("%Y-%m-%d"), *sessions.index.strftime("%Y-%m-%d").tolist()]


def _completed(path: Path, strategy: str) -> set[tuple[str, str, str]]:
    if not path.exists() or path.stat().st_size == 0:
        return set()
    with path.open(newline="", encoding="utf-8") as handle:
        return {
            (row["ticker"].strip().upper(), row["information_cutoff"][:10], row["strategy_version"])
            for row in csv.DictReader(handle)
            if row.get("source") == "portfolio_manager" and row.get("strategy_version") == strategy
        }


def run_batch(
    tickers: list[str],
    start: str,
    end: str,
    *,
    strategy_version: str = DEFAULT_STRATEGY,
    analysts: str | None = None,
    output_csv: str | Path | None = None,
    logs_dir: str | Path | None = None,
) -> dict:
    output = Path(output_csv or DATA_DIR / "decisions" / f"{strategy_version}.csv")
    dates = _dates(start, end)
    done = _completed(output, strategy_version)
    cells = [(ticker.strip().upper(), date) for ticker in tickers for date in dates]
    summary = {"strategy_version": strategy_version, "output_csv": str(output), "requested": len(cells), "skipped": 0, "success": 0, "failed": 0, "failures": []}

    for ticker, date in cells:
        if (ticker, date, strategy_version) in done:
            summary["skipped"] += 1
            continue
        try:
            result = run_one(
                ticker,
                date,
                strategy_version=strategy_version,
                analysts=analysts,
                logs_dir=logs_dir,
            )
            append_decision(output, result["decision_row"])
            done.add((ticker, date, strategy_version))
            summary["success"] += 1
            print(f"[ok] {ticker} {date} -> {result['action']}")
        except Exception as exc:
            summary["failed"] += 1
            summary["failures"].append({"ticker": ticker, "date": date, "error": f"{type(exc).__name__}: {exc}"})
            print(f"[failed] {ticker} {date}: {type(exc).__name__}: {exc}")

    summary["complete"] = summary["success"] + summary["skipped"] == summary["requested"]
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return summary


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run all AAPL/GOOGL/AMZN cells and create B's decision CSV")
    parser.add_argument("--tickers", default="AAPL,GOOGL,AMZN")
    parser.add_argument("--start", required=True, help="First evaluation session, YYYY-MM-DD")
    parser.add_argument("--end", required=True, help="Last evaluation session, YYYY-MM-DD")
    parser.add_argument("--analysts", default=os.getenv("TRADINGAGENTS_ANALYSTS", "market,fundamentals"))
    parser.add_argument("--strategy-version", default=DEFAULT_STRATEGY)
    parser.add_argument("--output", default=None)
    parser.add_argument("--logs-dir", default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        cfg = load_config()
        tickers = [item.strip().upper() for item in args.tickers.split(",") if item.strip()]
        if tickers != cfg["tickers"]:
            raise ValueError(f"Tickers must match B config exactly: {cfg['tickers']}")
        summary = run_batch(
            tickers,
            args.start,
            args.end,
            strategy_version=args.strategy_version,
            analysts=args.analysts,
            output_csv=args.output,
            logs_dir=args.logs_dir,
        )
        return 0 if summary["complete"] else 1
    except Exception as exc:
        print(f"Batch setup failed: {type(exc).__name__}: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
