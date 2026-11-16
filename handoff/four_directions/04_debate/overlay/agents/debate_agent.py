"""Independent debate module on the original graph. Offline preview by default."""
import argparse
import json

from agents.debate_config import DebateOptions
from agents.run_agents import run_one, append_decision, DEFAULT_ANALYSTS
from data import ROOT


def run(ticker, trade_date, *, enabled=True, rounds=3, live=False):
    options = DebateOptions(enabled=enabled, rounds=rounds)
    mode = "on" if enabled else "off"
    strategy = f"ta-debate-{mode}-r{options.effective_rounds}-v1"
    logs = ROOT / "agents/logs/modules" / strategy
    result = run_one(ticker, trade_date, strategy_version=strategy,
                     analysts=list(DEFAULT_ANALYSTS), logs_dir=logs,
                     dry_run=not live, debate_options=options)
    if live and result.get("status") == "success":
        append_decision(ROOT / "data/decisions" / f"{strategy}.csv",result["decision_row"])
    return result


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ticker",required=True,choices=["AAPL","GOOGL","AMZN"])
    parser.add_argument("--date",required=True)
    parser.add_argument("--multi-round",action=argparse.BooleanOptionalAction,default=True,
                        help="Enabled by default; --no-multi-round restores one round")
    parser.add_argument("--rounds",type=int,default=3,help="Rounds per side when enabled (default 3)")
    parser.add_argument("--live",action="store_true",help="Explicitly allow paid model and news API calls")
    args=parser.parse_args(argv)
    print(json.dumps(run(args.ticker,args.date,enabled=args.multi_round,
                         rounds=args.rounds,live=args.live),ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
