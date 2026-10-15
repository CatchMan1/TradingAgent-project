import csv
import json

import pytest

from agents.batch_run import _completed, _dates
from agents.run_agents import _record_stats, _safe_analysts, _session_cutoff, append_decision, run_one
from agents.recover_decision import recover_decision


def test_batch_dates_include_seed_and_all_sessions():
    assert _dates("2024-01-01", "2024-01-05") == [
        "2023-12-29",
        "2024-01-02",
        "2024-01-03",
        "2024-01-04",
        "2024-01-05",
    ]


def test_early_close_uses_actual_close_plus_thirty_minutes():
    cutoff, decision = _session_cutoff("2024-07-03")
    assert cutoff.isoformat() == "2024-07-03T13:00:00-04:00"
    assert decision.isoformat() == "2024-07-03T13:30:00-04:00"


def test_analyst_names_are_validated_and_deduplicated():
    assert _safe_analysts("market,fundamentals,market") == ["market", "fundamentals"]
    with pytest.raises(ValueError, match="Unknown analyst"):
        _safe_analysts("market,oracle")


def test_decision_append_and_resume_key(tmp_path):
    path = tmp_path / "agent.csv"
    row = {
        "ticker": "AAPL",
        "decision_time": "2024-01-02T16:30:00-05:00",
        "information_cutoff": "2024-01-02T16:00:00-05:00",
        "action": "BUY",
        "strategy_version": "v1",
        "source": "portfolio_manager",
    }
    append_decision(path, row)
    assert _completed(path, "v1") == {("AAPL", "2024-01-02", "v1")}
    with path.open(newline="", encoding="utf-8") as handle:
        assert list(csv.DictReader(handle)) == [row]


def test_dry_run_never_imports_or_calls_official_graph(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "agents.run_agents._snapshot_manifest",
        lambda ticker, cutoff, data_dir: {"cutoff": cutoff.isoformat(), "sources": {}},
    )
    monkeypatch.setattr(
        "agents.run_agents._import_official",
        lambda: pytest.fail("dry-run imported the official LLM graph"),
    )
    result = run_one("AAPL", "2024-01-02", logs_dir=tmp_path, dry_run=True)
    assert result["status"] == "dry_run"
    assert (tmp_path / "runs.jsonl").is_file()


def test_token_aliases_follow_actual_stats():
    class Stats:
        def get_stats(self):
            return {"llm_calls": 14, "tool_calls": 10, "tokens_in": 130469, "tokens_out": 46421}

    record = {"input_tokens": 0, "output_tokens": 0}
    _record_stats(record, Stats())
    assert record["input_tokens"] == record["tokens_in"] == 130469
    assert record["output_tokens"] == record["tokens_out"] == 46421


def test_recover_saved_underweight_without_model_call(tmp_path, monkeypatch):
    monkeypatch.setattr("agents.run_agents._import_official", lambda: pytest.fail("LLM import attempted"))
    logs = tmp_path / "logs"
    state_file = logs / "results/AAPL/TradingAgentsStrategy_logs/full_states_log_2024-01-02.json"
    state_file.parent.mkdir(parents=True)
    state_file.write_text(json.dumps({
        "company_of_interest": "AAPL", "trade_date": "2024-01-02",
        "final_rating": "Underweight", "final_trade_decision": "**Rating**: Underweight",
    }), encoding="utf-8")
    run_log = logs / "runs.jsonl"
    run_log.write_text(json.dumps({
        "run_id": "AAPL_2024-01-02_v1", "ticker": "AAPL", "trade_date": "2024-01-02",
        "strategy_version": "v1", "status": "failed", "error_type": "ValueError",
        "error": "Unsupported/absent final rating; Overweight/Underweight/REVIEW require explicit upstream policy",
        "tokens_in": 130469, "tokens_out": 46421,
    }) + "\n", encoding="utf-8")
    output = tmp_path / "decision.csv"
    result = recover_decision("AAPL", "2024-01-02", "v1", logs_dir=logs, output_csv=output)
    assert result["status"] == "recovered"
    assert result["final_rating"] == "UNDERWEIGHT"
    assert result["tokens_in"] == result["tokens_out"] == 0
    with output.open(newline="", encoding="utf-8") as handle:
        row, = csv.DictReader(handle)
    assert row == {
        "ticker": "AAPL", "decision_time": "2024-01-02T16:30:00-05:00",
        "information_cutoff": "2024-01-02T16:00:00-05:00", "action": "SELL",
        "strategy_version": "v1", "source": "portfolio_manager",
    }
    with pytest.raises(ValueError, match="already exists"):
        recover_decision("AAPL", "2024-01-02", "v1", logs_dir=logs, output_csv=output)


def test_recovery_requires_matching_failure_record(tmp_path):
    logs = tmp_path / "logs"
    state_file = logs / "results/AAPL/TradingAgentsStrategy_logs/full_states_log_2024-01-02.json"
    state_file.parent.mkdir(parents=True)
    state_file.write_text(json.dumps({
        "company_of_interest": "AAPL", "trade_date": "2024-01-02",
        "final_rating": "Buy", "final_trade_decision": "**Rating**: Buy",
    }), encoding="utf-8")
    (logs / "runs.jsonl").write_text("", encoding="utf-8")
    with pytest.raises(ValueError, match="No matching"):
        recover_decision("AAPL", "2024-01-02", "v1", logs_dir=logs, output_csv=tmp_path / "decision.csv")


@pytest.mark.parametrize("date, expected", [
    ("2024-01-02", "2024-01-02T16:00:00-05:00"),
    ("2024-07-03", "2024-07-03T13:00:00-04:00"),
])
def test_local_financial_tool_excludes_after_close_filings(date, expected, monkeypatch):
    import pandas as pd
    from agents import local_data_vendor as vendor
    from data import facts_asof

    close = pd.Timestamp(expected)
    facts = pd.DataFrame([
        dict(taxonomy="us-gaap", tag="Assets", unit="USD", start="", end="2023-12-31", val=100,
             accn="before", accepted_at=(close - pd.Timedelta(minutes=1)).isoformat()),
        dict(taxonomy="us-gaap", tag="Assets", unit="USD", start="", end="2023-12-31", val=999,
             accn="after", accepted_at=(close + pd.Timedelta(minutes=1)).isoformat()),
    ])
    def read_asof(ticker, kind, cutoff, **kwargs):
        assert kind == "financials"
        assert cutoff == expected
        return facts_asof(facts, cutoff)

    monkeypatch.setattr(vendor, "data_asof", read_asof)
    visible = vendor._facts("AAPL", date)
    assert visible.val.tolist() == [100]
