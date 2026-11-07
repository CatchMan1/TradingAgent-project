"""实验参数与最终测试保护。"""
from data import ROOT, DATA_DIR, data_hash, digest, json_bytes, utcnow
import json
import math
from pathlib import Path


def load_config(path=None):
    c=path.copy() if isinstance(path, dict) else json.loads(Path(path or ROOT/"config.json").read_text())
    import pandas as pd
    if c["tickers"] != ["AAPL","GOOGL","AMZN"]:
        raise ValueError("This project requires separate AAPL/GOOGL/AMZN accounts")
    if c["timezone"] != "America/New_York":
        raise ValueError("Unsupported timezone")
    prior=pd.Timestamp(c["warmup_start"])
    for stage in ["train","test"]:
        a,b=map(pd.Timestamp,c["splits"][stage])
        if not prior < a <= b: raise ValueError("Overlapping/invalid date splits")
        prior=b
    for k in ["commission_bps","slippage_bps","annualization","risk_free_rate"]:
        if not isinstance(c[k],(int,float)) or not math.isfinite(c[k]): raise ValueError(f"Invalid {k}")
    if not 0<=c["commission_bps"]<10000 or not 0<=c["slippage_bps"]<10000 or c["annualization"]<=1 or c["risk_free_rate"]<=-1:
        raise ValueError("Invalid cost/annualization/risk-free rate")
    for k in ["sma","macd"]:
        if any(type(v) is not int or v<=0 for v in c[k].values()) or c[k]["fast"]>=c[k]["slow"]:
            raise ValueError("Invalid indicator windows")
    import datetime
    datetime.time.fromisoformat(c["decision_clock"])
    if c["decision_clock"] <= "16:00": raise ValueError("Decision clock must be after regular close")
    return c


def code_hash():
    # 只哈希 Notebook 源码，不包含输出和 execution_count。
    notebook = json.loads((ROOT / "analysis.ipynb").read_text())
    # 区间、输入路径、显式测试开关是运行参数；交易参数另由 config_hash 锁定。
    cells = ["".join(c["source"]) for c in notebook["cells"]
             if c["cell_type"] == "code" and "parameters" not in c.get("metadata", {}).get("tags", [])]
    sources = b"".join((ROOT / name).read_bytes() for name in ["data.py", "signals.py", "settings.py"])
    return digest(sources + json_bytes(cells))


def freeze(cfg, path="frozen.json", agent_strategy_version=None):
    """可选：评价测试之前保存配置、代码和数据哈希。"""
    cfg = load_config(cfg)
    path = (ROOT / path).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError("Freeze output must stay inside project")
    record = dict(frozen_at=utcnow(), config=cfg, config_hash=digest(json_bytes(cfg)),
                  code_hash=code_hash(), data_hash=data_hash(DATA_DIR),
                  agent_strategy_version=agent_strategy_version)
    with path.open("xb") as file:
        file.write(json_bytes(record))
    return record


def check_evaluation(cfg, stage, lock=None, allow_test=False):
    if stage not in cfg["splits"]:
        raise ValueError("Unknown split")
    if stage != "test":
        return
    if not allow_test or lock is None:
        raise ValueError("Test evaluation locked: freeze config/code/data and set ENABLE_FINAL_TEST=True")
    record = json.loads(Path(lock).read_text())
    if record["config_hash"] != digest(json_bytes(cfg)) or record["code_hash"] != code_hash():
        raise ValueError("Frozen config/code mismatch; test evaluation refused")
    if record.get("data_hash") != data_hash(DATA_DIR):
        raise ValueError("Frozen data content mismatch; test evaluation refused")
