"""Validate archived metrics before publishing presentation figures; no API calls."""
import json
import shutil

import pandas as pd
import pytest

from experiments.plot_single_agent_comparison import DEFAULT_INPUT, load_results


def test_daily_ledgers_reconcile_and_use_return_end_dates():
    summary, curves = load_results(DEFAULT_INPUT)
    assert len(summary) == len(curves) == 9
    assert set(summary.ticker) == {"AAPL", "GOOGL", "AMZN"}
    assert summary.max_drawdown_pct.ge(0).all()
    for dates, nav, drawdown in curves.values():
        assert len(dates) == 71 and nav[0] == 1 and drawdown[0] == 0
        assert dates[0].date().isoformat() == "2026-07-01"
        assert dates[-1].date().isoformat() == "2026-10-09"
        assert dates.is_monotonic_increasing and not dates.has_duplicates


def test_duplicate_metrics_fail_before_charting(tmp_path):
    shutil.copy(DEFAULT_INPUT / "run.json", tmp_path / "run.json")
    metrics = pd.read_csv(DEFAULT_INPUT / "metrics.csv")
    pd.concat([metrics, metrics.iloc[:1]]).to_csv(tmp_path / "metrics.csv", index=False)
    with pytest.raises(ValueError, match="Duplicate"):
        load_results(tmp_path)


def test_tampered_nav_fails_reconciliation(tmp_path):
    for name in ("run.json", "metrics.csv"):
        shutil.copy(DEFAULT_INPUT / name, tmp_path / name)
    relative = "AAPL/agent_period/single_agent/daily.csv"
    target = tmp_path / relative
    target.parent.mkdir(parents=True)
    daily = pd.read_csv(DEFAULT_INPUT / relative)
    daily.loc[0, "net_values"] += 0.01
    daily.to_csv(target, index=False)
    with pytest.raises(ValueError, match="does not reconcile"):
        load_results(tmp_path)


@pytest.mark.parametrize("field,value", [("nav_mode", "compound"), ("exclude_periods", [["2026-07-30", "2026-08-03"]])])
def test_incompatible_protocol_is_not_silently_labelled_as_original(tmp_path, field, value):
    run = json.loads((DEFAULT_INPUT / "run.json").read_text())
    run[field] = value
    (tmp_path / "run.json").write_text(json.dumps(run))
    with pytest.raises(ValueError, match="archived full-period"):
        load_results(tmp_path)
