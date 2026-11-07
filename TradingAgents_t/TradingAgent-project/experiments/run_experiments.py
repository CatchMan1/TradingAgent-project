"""Run a fixed Role C manifest with isolated evidence and resumable CSV output."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

from agents.run_agents import append_decision, run_one
from data import DATA_DIR, ROOT, schedule


EXPERIMENTS_DIR = ROOT / "experiments"
DEFAULT_MANIFEST = EXPERIMENTS_DIR / "experiment_manifest.csv"
TRUTHY = {"1", "true", "yes", "on"}
RUN_FIELDS = [
    "attempt_id", "run_id", "strategy_version", "ticker", "trade_date", "analysts",
    "model_provider", "quick_model", "deep_model", "status", "llm_calls", "tool_calls",
    "input_tokens", "output_tokens", "elapsed_seconds", "action", "final_rating",
    "error_type", "error", "decision_file", "log_file", "course_project_commit",
    "tradingagents_commit", "data_snapshot_sha256",
]
COST_FIELDS = [
    "attempt_id", "run_id", "provider", "model", "input_tokens", "cache_hit_input_tokens",
    "cache_miss_input_tokens", "output_tokens", "input_price_usd_per_million",
    "cache_hit_price_usd_per_million", "output_price_usd_per_million",
    "estimated_cost_usd", "billed_cost_usd", "price_effective_date", "price_source",
    "currency", "notes",
]


def _slug(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", value):
        raise ValueError(f"Unsafe strategy_version: {value!r}")
    return value


def _strategy_logs_dir(strategy: str) -> Path:
    """Keep Windows cache/report paths below the legacy MAX_PATH boundary."""
    short_id = hashlib.sha256(strategy.encode("utf-8")).hexdigest()[:12]
    return ROOT / "agents" / "logs" / "e" / short_id


def load_manifest(path: str | Path = DEFAULT_MANIFEST) -> list[dict[str, str]]:
    target = Path(path)
    with target.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    required = {"order", "enabled", "strategy_version", "ticker", "trade_date", "analysts"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError(f"Manifest must contain columns: {sorted(required)}")
    enabled = [row for row in rows if row["enabled"].strip().lower() in TRUTHY]
    enabled.sort(key=lambda row: int(row["order"]))
    seen: set[tuple[str, str, str]] = set()
    for row in enabled:
        row["strategy_version"] = _slug(row["strategy_version"].strip())
        row["ticker"] = row["ticker"].strip().upper()
        row["trade_date"] = row["trade_date"].strip()
        analysts = [item.strip().lower() for item in row["analysts"].split(",") if item.strip()]
        row["analysts"] = ",".join(analysts)
        if row["ticker"] not in {"AAPL", "GOOGL", "AMZN"}:
            raise ValueError(f"Unsupported ticker: {row['ticker']}")
        if schedule(row["trade_date"], row["trade_date"]).empty:
            raise ValueError(f"Not an NYSE session: {row['trade_date']}")
        key = (row["strategy_version"], row["ticker"], row["trade_date"])
        if key in seen:
            raise ValueError(f"Duplicate manifest cell: {key}")
        seen.add(key)
    return enabled


def _completed(path: Path, strategy: str) -> set[tuple[str, str]]:
    if not path.exists() or path.stat().st_size == 0:
        return set()
    with path.open(newline="", encoding="utf-8") as handle:
        return {
            (row["ticker"].strip().upper(), row["information_cutoff"][:10])
            for row in csv.DictReader(handle)
            if row.get("strategy_version") == strategy and row.get("source") == "portfolio_manager"
        }


def _write_csv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _last_jsonl(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    last = ""
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                last = line
    return json.loads(last) if last else {}


def _cumulative_round_limit(total: int, round_number: int, total_rounds: int) -> int:
    """Return the cumulative manifest prefix for a resumable batch round."""
    if total_rounds <= 0:
        raise ValueError("total_rounds must be positive")
    if not 1 <= round_number <= total_rounds:
        raise ValueError(f"round_number must be between 1 and {total_rounds}")
    return math.ceil(total * round_number / total_rounds)


def rebuild_audit_tables(logs_root: Path = ROOT / "agents" / "logs") -> tuple[int, int]:
    run_rows: list[dict[str, Any]] = []
    cost_rows: list[dict[str, Any]] = []
    for log_path in sorted(logs_root.rglob("runs.jsonl")):
        with log_path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                try:
                    item = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Malformed JSONL: {log_path}:{line_number}") from exc
                attempt_id = f"{item.get('run_id', 'unknown')}__{item.get('started_at', 'undated')}__{line_number}"
                decision_file = ""
                strategy = item.get("strategy_version", "")
                if strategy:
                    decision_file = str(DATA_DIR / "decisions" / f"{strategy}.csv")
                news = item.get("data_snapshot", {}).get("sources", {}).get("news", {})
                run_rows.append({
                    "attempt_id": attempt_id,
                    "run_id": item.get("run_id", ""),
                    "strategy_version": strategy,
                    "ticker": item.get("ticker", ""),
                    "trade_date": item.get("trade_date", ""),
                    "analysts": ",".join(item.get("analysts", [])),
                    "model_provider": item.get("model_provider", ""),
                    "quick_model": item.get("quick_model", ""),
                    "deep_model": item.get("deep_model", ""),
                    "status": item.get("status", ""),
                    "llm_calls": item.get("llm_calls", 0),
                    "tool_calls": item.get("tool_calls", 0),
                    "input_tokens": item.get("input_tokens", 0),
                    "output_tokens": item.get("output_tokens", 0),
                    "elapsed_seconds": item.get("elapsed_seconds", ""),
                    "action": item.get("action", ""),
                    "final_rating": item.get("final_rating", ""),
                    "error_type": item.get("error_type", ""),
                    "error": item.get("error", ""),
                    "decision_file": decision_file,
                    "log_file": str(log_path),
                    "course_project_commit": item.get("course_project_git", {}).get("commit", ""),
                    "tradingagents_commit": item.get("tradingagents_git", {}).get("commit", ""),
                    "data_snapshot_sha256": news.get("sha256", ""),
                })
                cost_rows.append({
                    "attempt_id": attempt_id,
                    "run_id": item.get("run_id", ""),
                    "provider": item.get("model_provider", ""),
                    "model": item.get("quick_model", ""),
                    "input_tokens": item.get("input_tokens", 0),
                    "cache_hit_input_tokens": "",
                    "cache_miss_input_tokens": "",
                    "output_tokens": item.get("output_tokens", 0),
                    "input_price_usd_per_million": "",
                    "cache_hit_price_usd_per_million": "",
                    "output_price_usd_per_million": "",
                    "estimated_cost_usd": "",
                    "billed_cost_usd": "",
                    "price_effective_date": "",
                    "price_source": "",
                    "currency": "USD",
                    "notes": "Token totals only; cache split and billed cost unavailable in local logs.",
                })
    _write_csv(EXPERIMENTS_DIR / "runs.csv", RUN_FIELDS, run_rows)
    _write_csv(EXPERIMENTS_DIR / "costs.csv", COST_FIELDS, cost_rows)
    return len(run_rows), len(cost_rows)


def run_manifest(
    path: str | Path = DEFAULT_MANIFEST,
    *,
    dry_run: bool = False,
    limit: int | None = None,
    round_number: int | None = None,
    total_rounds: int = 6,
) -> dict[str, Any]:
    rows = load_manifest(path)
    if limit is not None and round_number is not None:
        raise ValueError("Use either limit or round_number, not both")
    if round_number is not None:
        limit = _cumulative_round_limit(len(rows), round_number, total_rounds)
    if limit is not None:
        if limit < 0:
            raise ValueError("limit must be non-negative")
        rows = rows[:limit]
    summary: dict[str, Any] = {
        "requested": len(rows), "success": 0, "failed": 0, "skipped": 0,
        "input_tokens": 0, "output_tokens": 0, "elapsed_seconds": 0.0, "failures": [],
    }
    completed_by_strategy: dict[str, set[tuple[str, str]]] = {}
    for position, row in enumerate(rows, start=1):
        strategy = row["strategy_version"]
        output = DATA_DIR / "decisions" / f"{strategy}.csv"
        done = completed_by_strategy.setdefault(strategy, _completed(output, strategy))
        key = (row["ticker"], row["trade_date"])
        if not dry_run and key in done:
            summary["skipped"] += 1
            print(
                f"[decision {position}/{len(rows)}] SKIP {row['ticker']} "
                f"{row['trade_date']} already completed",
                flush=True,
            )
            continue
        print(
            f"[decision {position}/{len(rows)}] START {row['ticker']} {row['trade_date']}",
            flush=True,
        )
        logs_dir = _strategy_logs_dir(strategy)
        # The Finnhub vendor writes atomically via a temporary file and expects
        # its parent to exist before graph construction. Isolated experiment
        # roots therefore need this directory created explicitly.
        (logs_dir / "cache" / "finnhub").mkdir(parents=True, exist_ok=True)
        try:
            result = run_one(
                row["ticker"], row["trade_date"], strategy_version=strategy,
                analysts=row["analysts"], logs_dir=logs_dir, dry_run=dry_run,
                progress_label=f"{position}/{len(rows)}",
            )
            if not dry_run:
                append_decision(output, result["decision_row"])
                done.add(key)
            summary["success"] += 1
            summary["input_tokens"] += int(result.get("input_tokens", 0))
            summary["output_tokens"] += int(result.get("output_tokens", 0))
            summary["elapsed_seconds"] += float(result.get("elapsed_seconds", 0))
            print(
                f"[decision {position}/{len(rows)}] DONE {row['ticker']} "
                f"{row['trade_date']} -> {result.get('action', result['status'])}",
                flush=True,
            )
        except Exception as exc:
            failed_record = _last_jsonl(logs_dir / "runs.jsonl")
            if (failed_record.get("ticker") == row["ticker"]
                    and failed_record.get("trade_date") == row["trade_date"]
                    and failed_record.get("strategy_version") == strategy):
                summary["input_tokens"] += int(failed_record.get("input_tokens", 0))
                summary["output_tokens"] += int(failed_record.get("output_tokens", 0))
                summary["elapsed_seconds"] += float(failed_record.get("elapsed_seconds", 0))
            summary["failed"] += 1
            summary["failures"].append({
                "ticker": row["ticker"], "trade_date": row["trade_date"],
                "error": f"{type(exc).__name__}: {exc}",
            })
            print(
                f"[decision {position}/{len(rows)}] FAILED {row['ticker']} "
                f"{row['trade_date']}: {type(exc).__name__}: {exc}",
                flush=True,
            )
        finally:
            rebuild_audit_tables()
    summary["complete"] = summary["success"] + summary["skipped"] == summary["requested"]
    summary["elapsed_seconds"] = round(summary["elapsed_seconds"], 3)
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--round", dest="round_number", type=int)
    parser.add_argument("--rounds", dest="total_rounds", type=int, default=6)
    args = parser.parse_args(argv)
    try:
        summary = run_manifest(
            args.manifest,
            dry_run=args.dry_run,
            limit=args.limit,
            round_number=args.round_number,
            total_rounds=args.total_rounds,
        )
    except Exception as exc:
        print(f"Experiment setup failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1
    return 0 if summary["complete"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

