import json
from pathlib import Path

import pytest

from data import ROOT
from settings import check_evaluation, code_hash, load_config


def test_notebook_defaults_load_all_stocks_and_two_periods():
    import pandas as pd
    notebook = json.loads((ROOT / "analysis.ipynb").read_text())
    cell = next(c for c in notebook["cells"] if "parameters" in c.get("metadata", {}).get("tags", []))
    scope = dict(pd=pd, load_config=load_config)
    exec("".join(cell["source"]), scope)
    assert scope["TICKERS"] == ["AAPL", "GOOGL", "AMZN"]
    assert scope["periods"] == {"train": ("2024-01-01", "2026-05-31"),
                                "test": ("2026-06-01", "2026-10-09"),
                                "train_test": ("2024-01-01", "2026-10-09")}


def test_runtime_parameters_can_change_without_invalidating_code_hash(monkeypatch, tmp_path):
    import settings
    notebook = json.loads((ROOT / "analysis.ipynb").read_text())
    for name in ["data.py", "signals.py", "settings.py"]:
        (tmp_path / name).write_bytes((ROOT / name).read_bytes())
    (tmp_path / "analysis.ipynb").write_text(json.dumps(notebook))
    monkeypatch.setattr(settings, "ROOT", tmp_path)
    original = code_hash()
    params = next(c for c in notebook["cells"] if "parameters" in c.get("metadata", {}).get("tags", []))
    params["source"] = ["SPLIT = 'test'\nENABLE_FINAL_TEST = True\n"]
    (tmp_path / "analysis.ipynb").write_text(json.dumps(notebook))
    assert code_hash() == original


def test_formula_change_invalidates_code_hash(monkeypatch, tmp_path):
    import settings
    notebook = json.loads((ROOT / "analysis.ipynb").read_text())
    for name in ["data.py", "signals.py", "settings.py"]:
        (tmp_path / name).write_bytes((ROOT / name).read_bytes())
    (tmp_path / "analysis.ipynb").write_text(json.dumps(notebook))
    monkeypatch.setattr(settings, "ROOT", tmp_path)
    original = code_hash()
    definition = next(c for c in notebook["cells"] if "definitions" in c.get("metadata", {}).get("tags", []))
    definition["source"] += ["\n# Formula revision\n"]
    (tmp_path / "analysis.ipynb").write_text(json.dumps(notebook))
    assert code_hash() != original


def test_baseline_csv_is_the_input_to_backtest(tmp_path):
    """落盘后修改 CSV，回测应读到修改后的信号，而不是沿用内存表。"""
    import pandas as pd
    from signals import load_decisions, validate_decisions, decision_sessions

    notebook = json.loads((ROOT / "analysis.ipynb").read_text())
    decision = pd.DataFrame([
        dict(ticker="AAPL", decision_time=day + "T16:30:00-05:00",
             information_cutoff=day + "T16:00:00-05:00", action="BUY",
             strategy_version="buy_hold-v1", source="baseline", session=day)
        for day in ["2023-12-29", "2024-01-02"]
    ])
    namespace = dict(ROOT=tmp_path, train_start="2024-01-02", test_end="2024-01-02",
                     pd=pd, load_decisions=load_decisions,
                     validate_decisions=validate_decisions, decision_sessions=decision_sessions,
                     df_eval=pd.DataFrame(index=pd.DatetimeIndex(["2024-01-02T09:30:00-05:00"])),
                     cfg={"tickers": ["AAPL"], "timezone": "America/New_York"},
                     baseline_tables={"AAPL": {strategy: decision.copy()
                                      for strategy in ["buy_hold", "sma", "macd"]}})
    for cell in notebook["cells"]:
        if "signals-export" in cell.get("metadata", {}).get("tags", []):
            exec("".join(cell["source"]), namespace)
    path = tmp_path / "data/decisions/baseline_AAPL_train_test.csv"
    assert path.exists(), "基线信号必须先保存 CSV"
    saved = pd.read_csv(path)
    saved.loc[0, "action"] = "SELL"
    saved.to_csv(path, index=False)
    for cell in notebook["cells"]:
        if "signals-read" in cell.get("metadata", {}).get("tags", []):
            exec("".join(cell["source"]), namespace)
    assert namespace["decision_tables"]["AAPL", "buy_hold"].action.tolist() == ["SELL", "BUY"]


def test_baseline_csv_requires_every_stock_strategy_account(tmp_path):
    import pandas as pd
    from signals import load_decisions, validate_decisions, decision_sessions

    path = tmp_path / "baseline.csv"
    pd.DataFrame([
        dict(ticker="AAPL", strategy=strategy, decision_time=day + "T16:30:00-05:00",
             information_cutoff=day + "T16:00:00-05:00", action="HOLD",
             strategy_version="v1", source="baseline")
        for strategy in ["buy_hold", "macd"]  # sma 整组丢失
        for day in ["2023-12-29", "2024-01-02"]
    ]).to_csv(path, index=False)
    notebook = json.loads((ROOT / "analysis.ipynb").read_text())
    namespace = dict(pd=pd, load_decisions=load_decisions, validate_decisions=validate_decisions,
                     baseline_paths={"AAPL": path}, train_start="2024-01-02", test_end="2024-01-02")
    with pytest.raises(ValueError, match="strategies"):
        for cell in notebook["cells"]:
            if "signals-read" in cell.get("metadata", {}).get("tags", []):
                exec("".join(cell["source"]), namespace)


def test_split_excludes_return_labels_crossing_train_boundary():
    import pandas as pd
    notebook = json.loads((ROOT / "analysis.ipynb").read_text())
    index = pd.DatetimeIndex(["2026-05-28 09:30", "2026-05-29 09:30", "2026-06-01 09:30"], tz="America/New_York")
    data = pd.DataFrame({
        "date": ["2026-05-28", "2026-05-29", "2026-06-01"], "pct": [.01, .02, .03],
        "return_end": pd.DatetimeIndex(["2026-05-28 16:00", "2026-06-01 16:00", "2026-06-01 16:00"], tz="America/New_York"),
    }, index=index)
    from notebook_code import namespace
    train = namespace["select_period"](data, "2024-01-01", "2026-05-31")
    test = namespace["select_period"](data, "2026-06-01", "2026-10-09")
    full = namespace["select_period"](data, "2024-01-01", "2026-10-09")
    assert train.date.tolist() == ["2026-05-28"]
    assert test.date.tolist() == ["2026-06-01"]
    assert full.date.tolist() == ["2026-05-28", "2026-05-29", "2026-06-01"]
