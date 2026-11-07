import json
import pandas as pd
import pytest
from settings import load_config, freeze, check_evaluation
from data import ROOT
from notebook_code import signals
from data import schedule


def test_test_evaluation_requires_freeze_and_explicit_enable(tmp_path):
    cfg = load_config()
    with pytest.raises(ValueError):
        check_evaluation(cfg, "test", None, False)
    lock = ROOT / (".test-" + tmp_path.name + ".json")
    try:
        freeze(cfg, lock)
        with pytest.raises(ValueError):
            check_evaluation(cfg, "test", lock, False)
        check_evaluation(cfg, "test", lock, True)
        cfg["sma"]["slow"] = 100
        with pytest.raises(ValueError):
            check_evaluation(cfg, "test", lock, True)
    finally:
        lock.unlink(missing_ok=True)


@pytest.mark.parametrize("strategy",["buy_hold","sma","macd"])
def test_baseline_signals_unchanged_by_future_prices(strategy):
    s=schedule("2023-01-01","2024-01-10")
    p=pd.DataFrame(dict(date=s.index.strftime("%Y-%m-%d"),close=[100+i*.1 for i in range(len(s))],split=1.,dividend=0.))
    cfg=load_config()
    a=signals(p,"AAPL",strategy,"2024-01-02","2024-01-05",cfg)
    p.loc[p.date>"2024-01-05","close"]=99999
    b=signals(p,"AAPL",strategy,"2024-01-02","2024-01-05",cfg)
    pd.testing.assert_frame_equal(a,b)


def test_frozen_data_content_mismatch_rejected(tmp_path, monkeypatch):
    import settings
    cfg = load_config()
    lock = ROOT / (".test-" + tmp_path.name + ".json")
    try:
        freeze(cfg, lock)
        monkeypatch.setattr(settings, "data_hash", lambda folder: "modified")
        with pytest.raises(ValueError, match="data"):
            check_evaluation(cfg, "test", lock, True)
    finally:
        lock.unlink(missing_ok=True)


def test_macd_config_key_order_does_not_change_signals():
    s=schedule("2023-01-01","2024-01-10")
    import numpy as np
    p=pd.DataFrame(dict(date=s.index.strftime("%Y-%m-%d"),close=100+np.sin(np.arange(len(s))*.3)*10,split=1.,dividend=0.))
    cfg=load_config()
    a=signals(p,"AAPL","macd","2023-04-03","2024-01-10",cfg)
    cfg["macd"]={"slow":26,"fast":12,"signal":9}
    b=signals(p,"AAPL","macd","2023-04-03","2024-01-10",cfg)
    pd.testing.assert_frame_equal(a,b)
