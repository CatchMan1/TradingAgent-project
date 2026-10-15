"""Run one official TradingAgents decision and adapt it to B's CSV contract.

This module deliberately treats the official TradingAgents repository as an
external runtime. It does not copy or reimplement the graph. The only value
that crosses into B's backtest is the final Portfolio Manager rating; analyst,
Trader, and debate opinions remain in the saved report/state logs.

Run from the B-project root:

    python -m agents.run_agents --ticker AAPL --date 2024-01-02

The official package must be installed separately (see agents/README.md).
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import timedelta
from pathlib import Path
from typing import Any

from data import DATA_DIR, ROOT, data_asof, schedule


NY_TZ = "America/New_York"
DEFAULT_ANALYSTS = ("market", "fundamentals")
DEFAULT_STRATEGY = "ta-v0.6.0-deepseek-flash-market-fundamentals-v1"


def _safe_analysts(value: str | list[str] | tuple[str, ...] | None) -> list[str]:
    names = value if isinstance(value, (list, tuple)) else str(value or "").split(",")
    names = [str(name).strip().lower() for name in names if str(name).strip()]
    allowed = {"market", "social", "news", "fundamentals"}
    unknown = sorted(set(names) - allowed)
    if unknown:
        raise ValueError(f"Unknown analyst(s): {', '.join(unknown)}")
    if not names:
        raise ValueError("At least one analyst is required")
    return list(dict.fromkeys(names))


def _import_official():
    """Import the pinned external runtime only when a real run is requested."""
    try:
        import tradingagents
        from cli.stats_handler import StatsCallbackHandler
        from tradingagents.agents.rating import is_review
        from tradingagents.graph.trading_graph import TradingAgentsGraph
        from tradingagents.default_config import DEFAULT_CONFIG
    except ImportError as exc:
        raise RuntimeError(
            "Official TradingAgents is not installed in this Python environment. "
            "Install the pinned v0.6.0 checkout described in agents/README.md, "
            "then rerun the command."
        ) from exc
    return tradingagents, StatsCallbackHandler, is_review, TradingAgentsGraph, DEFAULT_CONFIG


def _build_runtime_config(default_config: dict[str, Any], analysts: list[str], logs_dir: Path) -> dict[str, Any]:
    """Apply course-project defaults without mutating the upstream global config."""
    config = copy.deepcopy(default_config)
    config.update(
        llm_provider=os.getenv("TRADINGAGENTS_LLM_PROVIDER", "deepseek"),
        quick_think_llm=os.getenv("TRADINGAGENTS_QUICK_THINK_LLM", "deepseek-flash"),
        deep_think_llm=os.getenv("TRADINGAGENTS_DEEP_THINK_LLM", "deepseek-flash"),
        output_language=os.getenv("TRADINGAGENTS_OUTPUT_LANGUAGE", "English"),
        max_debate_rounds=int(os.getenv("TRADINGAGENTS_MAX_DEBATE_ROUNDS", "1")),
        max_risk_discuss_rounds=int(os.getenv("TRADINGAGENTS_MAX_RISK_ROUNDS", "1")),
        checkpoint_enabled=os.getenv("TRADINGAGENTS_CHECKPOINT_ENABLED", "true").lower() in {"1", "true", "yes", "on"},
        temperature=float(os.getenv("TRADINGAGENTS_TEMPERATURE", "0.0")),
        llm_max_retries=int(os.getenv("TRADINGAGENTS_LLM_MAX_RETRIES", "6")),
        max_tokens=int(os.getenv("TRADINGAGENTS_MAX_TOKENS", "8192")),
        results_dir=str(logs_dir / "results"),
        data_cache_dir=str(logs_dir / "cache"),
        memory_log_path=str(logs_dir / "memory" / "trading_memory.md"),
    )
    config["data_vendors"] = {
        **config.get("data_vendors", {}),
        "core_stock_apis": "course_project",
        "technical_indicators": "course_project",
        "fundamental_data": "course_project",
    }
    config["tool_vendors"] = {
        **config.get("tool_vendors", {}),
        "get_insider_transactions": "course_project",
    }
    return config


def _session_cutoff(trade_date: str):
    sessions = schedule(trade_date, trade_date)
    if sessions.empty:
        raise ValueError(f"{trade_date} is not an NYSE trading session")
    close = sessions.iloc[0]["close"]
    cutoff = close.tz_convert(NY_TZ)
    decision_time = cutoff + timedelta(minutes=30)
    return cutoff, decision_time


def _snapshot_manifest(ticker: str, cutoff, data_dir: Path = DATA_DIR) -> dict[str, Any]:
    """Read B's as-of views before any model call and record their sizes/hashes."""
    manifest: dict[str, Any] = {"cutoff": cutoff.isoformat(), "sources": {}}
    for kind in ("prices", "financials"):
        frame = data_asof(ticker, kind, cutoff.isoformat(), data_dir=data_dir)
        payload = frame.to_csv(index=False).encode()
        manifest["sources"][kind] = {
            "rows": int(len(frame)),
            "sha256": hashlib.sha256(payload).hexdigest(),
        }
    return manifest


def _append_jsonl(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def _record_stats(record: dict[str, Any], stats: Any) -> None:
    usage = stats.get_stats()
    record.update(usage)
    record["input_tokens"] = usage["tokens_in"]
    record["output_tokens"] = usage["tokens_out"]


def _git_state(path: Path) -> dict[str, Any]:
    """Return reproducibility metadata without failing a run outside a checkout."""
    try:
        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=path, check=True,
            capture_output=True, text=True, timeout=5,
        ).stdout.strip()
        dirty = bool(subprocess.run(
            ["git", "status", "--porcelain"], cwd=path, check=True,
            capture_output=True, text=True, timeout=5,
        ).stdout.strip())
        return {"commit": commit, "dirty": dirty}
    except (OSError, subprocess.SubprocessError):
        return {"commit": None, "dirty": None}


def run_one(
    ticker: str,
    trade_date: str,
    *,
    strategy_version: str = DEFAULT_STRATEGY,
    analysts: str | list[str] | tuple[str, ...] | None = None,
    logs_dir: str | Path | None = None,
    data_dir: str | Path = DATA_DIR,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Run one `(ticker, trade_date)` cell and return its B-compatible row.

    A failed cell is logged and raised to the batch caller. It never writes a
    partial or guessed decision row.
    """
    try:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env", override=False)
    except ImportError:
        pass
    started = time.monotonic()
    ticker = ticker.strip().upper()
    selected = _safe_analysts(analysts or os.getenv("TRADINGAGENTS_ANALYSTS") or DEFAULT_ANALYSTS)
    logs = Path(logs_dir or ROOT / "agents" / "logs")
    record: dict[str, Any] = {
        "run_id": f"{ticker}_{trade_date}_{strategy_version}",
        "strategy_version": strategy_version,
        "ticker": ticker,
        "trade_date": trade_date,
        "analysts": selected,
        "status": "failed",
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "input_tokens": 0,
        "output_tokens": 0,
        "tokens_in": 0,
        "tokens_out": 0,
        "llm_calls": 0,
        "tool_calls": 0,
        "course_project_git": _git_state(ROOT),
    }
    stats = None
    try:
        cutoff, decision_time = _session_cutoff(trade_date)
        # This is the important B/A boundary: if local point-in-time data is
        # absent or malformed, fail before an API call rather than substituting
        # current data or silently producing a non-comparable signal.
        record["data_snapshot"] = _snapshot_manifest(ticker, cutoff, Path(data_dir))
        if dry_run:
            record.update(status="dry_run", elapsed_seconds=round(time.monotonic() - started, 3))
            _append_jsonl(logs / "runs.jsonl", record)
            return record

        tradingagents, StatsCallbackHandler, is_review, TradingAgentsGraph, default_config = _import_official()
        config = _build_runtime_config(default_config, selected, logs)
        official_root = Path(tradingagents.__file__).resolve().parents[1]
        record.update(
            tradingagents_version=tradingagents.__version__,
            tradingagents_git=_git_state(official_root),
            model_provider=config.get("llm_provider"),
            quick_model=config.get("quick_think_llm"),
            deep_model=config.get("deep_think_llm"),
            max_debate_rounds=config.get("max_debate_rounds"),
            max_risk_discuss_rounds=config.get("max_risk_discuss_rounds"),
            temperature=config.get("temperature"),
        )
        stats = StatsCallbackHandler()
        from agents.local_data_vendor import install as install_local_data_vendor

        install_local_data_vendor(Path(data_dir))
        graph = TradingAgentsGraph(selected, config=config, debug=False, callbacks=[stats])
        final_state, signal = graph.propagate(ticker, trade_date, asset_type="stock")
        _record_stats(record, stats)
        if is_review(signal):
            raise ValueError("Final Portfolio Manager rating is REVIEW/unparseable")

        # Only the final manager rating crosses into B's binary-position backtest.
        from signals import final_rating, from_final_state

        action = from_final_state(final_state)
        rating = final_rating(final_state)
        reports = logs / "reports" / ticker / trade_date
        reports.mkdir(parents=True, exist_ok=True)
        graph.save_reports(final_state, ticker, save_path=reports, html=True)
        record.update(
            status="success",
            action=action,
            final_rating=rating,
            report_dir=str(reports.relative_to(ROOT)),
            decision_time=decision_time.isoformat(),
            information_cutoff=cutoff.isoformat(),
        )
        row = {
            "ticker": ticker,
            "decision_time": decision_time.isoformat(),
            "information_cutoff": cutoff.isoformat(),
            "action": action,
            "strategy_version": strategy_version,
            "source": "portfolio_manager",
        }
        record["decision_row"] = row
        record["elapsed_seconds"] = round(time.monotonic() - started, 3)
        _append_jsonl(logs / "runs.jsonl", record)
        return record
    except Exception as exc:
        if stats is not None:
            _record_stats(record, stats)
        record.update(
            error_type=type(exc).__name__,
            error=str(exc),
            elapsed_seconds=round(time.monotonic() - started, 3),
        )
        _append_jsonl(logs / "runs.jsonl", record)
        raise


def append_decision(path: str | Path, row: dict[str, str]) -> None:
    """Append one validated row, creating B's required header if necessary."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fields = ["ticker", "decision_time", "information_cutoff", "action", "strategy_version", "source"]
    new_file = not target.exists() or target.stat().st_size == 0
    with target.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        if new_file:
            writer.writeheader()
        writer.writerow({field: row[field] for field in fields})


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run one TradingAgents decision for B's CSV interface")
    parser.add_argument("--ticker", required=True)
    parser.add_argument("--date", required=True, dest="trade_date")
    parser.add_argument("--analysts", default=None, help="Comma-separated; default: market,fundamentals")
    parser.add_argument("--strategy-version", default=DEFAULT_STRATEGY)
    parser.add_argument("--output", default=None, help="Optional B decision CSV to append on success")
    parser.add_argument("--dry-run", action="store_true", help="Validate date and local as-of data without calling an LLM")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = run_one(
            args.ticker,
            args.trade_date,
            strategy_version=args.strategy_version,
            analysts=args.analysts,
            dry_run=args.dry_run,
        )
        if result.get("status") == "success" and args.output:
            append_decision(args.output, result["decision_row"])
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        print(f"A run failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
