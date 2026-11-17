"""Generate one numeric weight per session, starting with the seed date."""
import argparse
import csv
import json
from pathlib import Path

from agents.run_agents import DEFAULT_ANALYSTS, run_one
from agents_debate.options import DebateOptions
from data import ROOT, schedule
from signals import load_decisions, validate_weights


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variant", required=True,
                        choices=["baseline", "position", "sentiment", "short", "debate"])
    parser.add_argument("--ticker", required=True, choices=["AAPL", "GOOGL", "AMZN"])
    parser.add_argument("--date", required=True)
    parser.add_argument("--rounds", type=int, default=3)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--live", action="store_true")
    args = parser.parse_args()

    options = DebateOptions(rounds=args.rounds)
    strategy = f"numeric-{args.variant}" + (f"-r{options.rounds}" if args.variant == "debate" else "")
    output = args.output or ROOT / "data/decisions" / args.variant / f"{strategy}.csv"
    previous = 0.
    if output.is_file():
        table = load_decisions(output)
        rows = table.loc[table.ticker == args.ticker]
        if not rows.empty:
            rows = validate_weights(rows, args.ticker)
            if args.date in set(rows.signal_date):
                print("Signal already exists.")
                return
            last = rows.iloc[-1]
            dates = schedule(last.signal_date, args.date).index.strftime("%Y-%m-%d").tolist()
            if dates != [last.signal_date, args.date]:
                parser.error(f"{args.date} must be the next session after {last.signal_date}")
            previous = float(last.target_weight)

    result = run_one(args.ticker, args.date, strategy_version=strategy, analysts=DEFAULT_ANALYSTS,
                     logs_dir=ROOT / "agents/logs/variants" / strategy, dry_run=not args.live,
                     variant=args.variant, previous_weight=previous, debate_rounds=options.rounds)
    if args.live:
        output.parent.mkdir(parents=True, exist_ok=True)
        new = not output.exists() or output.stat().st_size == 0
        with output.open("a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=["ticker", "signal_date", "target_weight"])
            if new:
                writer.writeheader()
            writer.writerow(result["decision_row"])
    print(json.dumps(result.get("decision_row", {"status": result["status"]})))


if __name__ == "__main__":
    main()
