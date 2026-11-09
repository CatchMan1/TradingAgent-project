"""Run the existing Notebook code for selected stocks; no model API calls."""
from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path

from data import ROOT


def compare(tickers, single_csv=None, output_dir=None):
    os.environ.setdefault("MPLBACKEND", "Agg")
    os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir())/"trading-matplotlib-cache"))
    single_csv=Path(single_csv or ROOT/"data/decisions/deepseek-flash-single-shared-memory-2026jul-oct-v1.csv").resolve()
    if not single_csv.is_file():
        raise FileNotFoundError("Single-agent decisions are not available yet")
    output_dir=Path(output_dir or ROOT/"results"/("single_vs_multi_"+"_".join(tickers))).resolve()
    scope={"__name__":"__main__", "EVALUATION_TICKERS":tickers, "SHOW_PLOTS":False,
           "SINGLE_AGENT_CSV_OVERRIDE":single_csv, "COMPARE_OUTPUT_DIR":output_dir}
    previous=Path.cwd()
    try:
        os.chdir(ROOT)
        notebook=json.loads((ROOT/"analysis.ipynb").read_text())
        for i,cell in enumerate(notebook["cells"]):
            if cell["cell_type"]=="code":
                exec(compile("".join(cell["source"]),f"<analysis.ipynb cell {i}>","exec"),scope)
    finally:
        os.chdir(previous)
    return output_dir


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tickers",default="AAPL")
    parser.add_argument("--single-csv")
    parser.add_argument("--output-dir")
    args=parser.parse_args(argv)
    tickers=[s.strip().upper() for s in args.tickers.split(",") if s.strip()]
    if not tickers or len(set(tickers))!=len(tickers) or not set(tickers).issubset({"AAPL","GOOGL","AMZN"}):
        parser.error("Use unique tickers from AAPL, GOOGL, AMZN")
    print(compare(tickers,args.single_csv,args.output_dir))


if __name__=="__main__":
    main()
