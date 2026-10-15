"""Recover a paid decision from the official saved state without an LLM call."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

from data import DATA_DIR, ROOT
from signals import final_rating, from_final_state

from .run_agents import DEFAULT_STRATEGY, _append_jsonl, _session_cutoff, append_decision


def recover_decision(
    ticker: str,
    trade_date: str,
    strategy_version: str = DEFAULT_STRATEGY,
    *,
    logs_dir: str | Path | None = None,
    output_csv: str | Path | None = None,
) -> dict:
    ticker = ticker.strip().upper()
    if ticker not in {"AAPL", "GOOGL", "AMZN"}:
        raise ValueError("Ticker is outside the configured project universe")
    if not strategy_version.strip():
        raise ValueError("A strategy version is required")
    cutoff, decision_time = _session_cutoff(trade_date)
    logs = Path(logs_dir or ROOT / "agents" / "logs")
    state_path = logs / "results" / ticker / "TradingAgentsStrategy_logs" / f"full_states_log_{trade_date}.json"
    state_bytes = state_path.read_bytes()
    state = json.loads(state_bytes)
    if state.get("company_of_interest") != ticker or state.get("trade_date") != trade_date:
        raise ValueError("Saved state ticker/date does not match the requested decision")

    run_log = logs / "runs.jsonl"
    matching = []
    with run_log.open(encoding="utf-8") as handle:
        for line in handle:
            entry = json.loads(line)
            if (entry.get("ticker") == ticker and entry.get("trade_date") == trade_date
                    and entry.get("strategy_version") == strategy_version
                    and entry.get("status") == "failed"
                    and entry.get("error_type") == "ValueError"
                    and "Unsupported/absent final rating" in entry.get("error", "")):
                matching.append(entry)
    if not matching:
        raise ValueError("No matching adapter-failure run found; recovery provenance cannot be verified")

    rating = final_rating(state)
    action = from_final_state(state)
    output = Path(output_csv or DATA_DIR / "decisions" / f"{strategy_version}.csv")
    if output.exists() and output.stat().st_size:
        with output.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                if (row.get("ticker") == ticker and row.get("information_cutoff", "")[:10] == trade_date
                        and row.get("strategy_version") == strategy_version):
                    raise ValueError("Decision already exists in output CSV")

    row = {
        "ticker": ticker,
        "decision_time": decision_time.isoformat(),
        "information_cutoff": cutoff.isoformat(),
        "action": action,
        "strategy_version": strategy_version,
        "source": "portfolio_manager",
    }
    append_decision(output, row)
    recovery = {
        "run_id": f"{ticker}_{trade_date}_{strategy_version}_recovery",
        "recovered_from_run_id": matching[-1].get("run_id"),
        "status": "recovered",
        "ticker": ticker,
        "trade_date": trade_date,
        "strategy_version": strategy_version,
        "final_rating": rating,
        "action": action,
        "state_sha256": hashlib.sha256(state_bytes).hexdigest(),
        "output_csv": str(output),
        "llm_calls": 0,
        "tool_calls": 0,
        "input_tokens": 0,
        "output_tokens": 0,
        "tokens_in": 0,
        "tokens_out": 0,
    }
    _append_jsonl(run_log, recovery)
    return recovery


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--strategy-version", default=DEFAULT_STRATEGY)
    parser.add_argument("--logs-dir")
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    try:
        result = recover_decision(
            args.ticker, args.date, args.strategy_version,
            logs_dir=args.logs_dir, output_csv=args.output,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.exit(1, f"Recovery failed: {type(exc).__name__}: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
