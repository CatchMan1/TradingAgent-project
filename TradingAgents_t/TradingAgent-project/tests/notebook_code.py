"""仅供测试：直接读取 Notebook 的函数，不维护第二套公式。"""
import json
from pathlib import Path
import numpy as np
import pandas as pd
from data import validate_prices, total_return_index, schedule
from signals import decision_sessions, validate_decisions

notebook = json.loads((Path(__file__).resolve().parents[1] / "analysis.ipynb").read_text())
namespace = dict(np=np, pd=pd, validate_prices=validate_prices, total_return_index=total_return_index,
                 schedule=schedule, decision_sessions=decision_sessions, validate_decisions=validate_decisions)
for cell in notebook["cells"]:
    if "definitions" in cell.get("metadata", {}).get("tags", []):
        exec(compile("".join(cell["source"]), "<analysis function cell>", "exec"), namespace)
signals = namespace["signals"]
