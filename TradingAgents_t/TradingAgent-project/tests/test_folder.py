import json
import pandas as pd
import pytest

from data import DataFolder, data_hash, read_sources
from notebook_code import namespace


def test_fixed_folder_preserves_source_and_rejects_failed_collection(tmp_path):
    folder = DataFolder(tmp_path)
    folder.write_json("raw/example.json", {"value": 1}, "https://example.com")
    folder.finish()
    record = read_sources(tmp_path)
    assert record["files"]["raw/example.json"]["source"] == "https://example.com"
    assert "snapshot_id" not in record
    folder.finish("failed")
    with pytest.raises(ValueError, match="failed"):
        read_sources(tmp_path)


def test_data_hash_tracks_actual_csv_not_only_source_note(tmp_path):
    (tmp_path / "prices").mkdir()
    file = tmp_path / "prices/AAPL.csv"
    file.write_text("date,close\n2024-01-02,100\n")
    before = data_hash(tmp_path)
    file.write_text("date,close\n2024-01-02,200\n")
    assert data_hash(tmp_path) != before


def test_actions_are_not_positions_and_hold_preserves_state():
    from test_engine import prices, decisions
    table = namespace["prepare_backtest"](
        prices([100., 110., 120., 130., 140.]),
        decisions(["BUY", "HOLD", "SELL", "HOLD", "BUY", "HOLD"]))
    assert table.signal.tolist() == [1, 1, 0, 0]
    assert table.position.tolist() == [1, 1, 0, 0]
    assert table.signal_session.iloc[0] == "2023-12-29"


def test_missing_decision_cannot_be_filled_as_hold():
    from test_engine import prices, decisions
    with pytest.raises(ValueError, match="decisions"):
        namespace["prepare_backtest"](prices([100., 110.]), decisions(["BUY", "HOLD"]))


def test_extra_decision_columns_cannot_override_market_or_position():
    from test_engine import prices, decisions
    d = decisions(["BUY", "HOLD", "HOLD"])
    d["close"] = 99999.
    d["position"] = -1.
    table = namespace["prepare_backtest"](prices([100., 110.]), d)
    assert table.close.tolist() == [100.]
    assert table.position.tolist() == [1.]
