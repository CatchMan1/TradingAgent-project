from pathlib import Path

import pytest

from experiments.run_experiments import (
    DEFAULT_MANIFEST,
    _cumulative_round_limit,
    _strategy_logs_dir,
    load_manifest,
)


def test_pilot_manifest_has_twenty_unique_cells():
    rows = load_manifest(DEFAULT_MANIFEST)
    cells = {(row["strategy_version"], row["ticker"], row["trade_date"]) for row in rows}
    assert len(rows) == len(cells) == 20
    assert {row["ticker"] for row in rows} == {"AAPL", "GOOGL", "AMZN"}
    assert {row["analysts"] for row in rows} == {"market,news,fundamentals"}


def test_strategy_log_path_is_stable_and_short():
    strategy = "ta-v0.6.0-deepseek-flash-3agent-pilot20-v1"
    first = _strategy_logs_dir(strategy)
    assert first == _strategy_logs_dir(strategy)
    longest_cache_file = first / "cache" / "finnhub" / ("x" * 64 + "." + "y" * 32 + ".tmp")
    assert len(str(longest_cache_file)) < 260


def test_2024q1_uses_six_equal_cumulative_rounds():
    assert [_cumulative_round_limit(186, n, 6) for n in range(1, 7)] == [31, 62, 93, 124, 155, 186]


def test_round_validation_rejects_out_of_range_values():
    with pytest.raises(ValueError):
        _cumulative_round_limit(186, 0, 6)
    with pytest.raises(ValueError):
        _cumulative_round_limit(186, 7, 6)


def test_2026_main_manifest_has_216_three_analyst_cells():
    manifest = Path(__file__).parents[1] / "experiments" / "manifests" / "main_2026jul_oct_v1.csv"
    rows = load_manifest(manifest)
    cells = {(row["strategy_version"], row["ticker"], row["trade_date"]) for row in rows}
    assert len(rows) == len(cells) == 216
    assert rows[0]["trade_date"] == "2026-06-30"
    assert rows[-1]["trade_date"] == "2026-10-09"
    assert {row["analysts"] for row in rows} == {"market,news,fundamentals"}
    assert [_cumulative_round_limit(len(rows), n, 6) for n in range(1, 7)] == [36, 72, 108, 144, 180, 216]

