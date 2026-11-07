"""Course entrypoint preflights news before constructing any LLM graph."""

import json
from types import SimpleNamespace

import pytest

from agents import batch_run, run_agents


@pytest.fixture
def offline_run(monkeypatch):
    monkeypatch.setenv("FINNHUB_API_KEY", "")
    monkeypatch.setenv("TRADINGAGENTS_NEWS_VENDOR", "finnhub")
    monkeypatch.setenv("TRADINGAGENTS_ANALYSTS", "market,news,fundamentals")
    monkeypatch.setattr(run_agents, "_snapshot_manifest", lambda *args: {"sources": {}})


def test_missing_key_stops_before_llm_import(tmp_path, monkeypatch, offline_run):
    monkeypatch.setattr(run_agents, "_import_official", lambda: pytest.fail("LLM runtime imported"))
    with pytest.raises(ValueError, match="FINNHUB_API_KEY"):
        run_agents.run_one("AAPL", "2026-07-01", logs_dir=tmp_path)
    record = json.loads((tmp_path / "runs.jsonl").read_text(encoding="utf-8"))
    assert record["status"] == "failed" and record["llm_calls"] == 0
    assert "decision_row" not in record


def test_course_config_pins_finnhub_and_historical_mode(tmp_path):
    config = run_agents._build_runtime_config({"tool_vendors": {"get_news": "yfinance"}}, ["news"], tmp_path)
    assert config["tool_vendors"]["get_news"] == "finnhub"
    assert config["data_vendors"]["news_data"] == "finnhub"
    assert config["news_previous_days_only"] and config["news_company_only"]
    assert config["news_timezone"] == "America/New_York"
    assert "news" in run_agents.DEFAULT_ANALYSTS
    assert "market-news-fundamentals" in run_agents.DEFAULT_STRATEGY


def test_batch_defers_analysts_until_dotenv_is_loaded(monkeypatch):
    monkeypatch.setenv("TRADINGAGENTS_ANALYSTS", "market,fundamentals")
    args = batch_run._parser().parse_args(["--start", "2026-07-01", "--end", "2026-08-05"])
    assert args.analysts is None


def test_news_request_failure_never_constructs_llm(tmp_path, monkeypatch, offline_run):
    from tradingagents.default_config import DEFAULT_CONFIG
    from tradingagents.dataflows.errors import VendorUnavailableError
    from tradingagents.dataflows.vendors.finnhub import news
    monkeypatch.setenv("FINNHUB_API_KEY", "dummy-secret")
    def fail(*args):
        raise VendorUnavailableError("Finnhub unavailable")
    monkeypatch.setattr(news, "prepare_news_snapshot", fail)
    monkeypatch.setattr(run_agents, "_import_official", lambda: (
        SimpleNamespace(__file__=__file__, __version__="0.6.0"), object, None,
        lambda *a, **k: pytest.fail("graph constructed after news failure"), DEFAULT_CONFIG,
    ))
    with pytest.raises(VendorUnavailableError):
        run_agents.run_one("AAPL", "2026-07-01", logs_dir=tmp_path)
    record = json.loads((tmp_path / "runs.jsonl").read_text(encoding="utf-8"))
    assert record["llm_calls"] == 0 and "decision_row" not in record


def test_prefetched_snapshot_reaches_graph_and_run_log(tmp_path, monkeypatch, offline_run):
    from tradingagents.default_config import DEFAULT_CONFIG
    from tradingagents.dataflows.vendors.finnhub import news
    monkeypatch.setenv("FINNHUB_API_KEY", "dummy-secret")
    monkeypatch.setattr(news.requests, "get", lambda *a, **k: SimpleNamespace(status_code=200, json=lambda: []))
    monkeypatch.setattr(news.time, "sleep", lambda _: None)
    def graph(*args, **kwargs):
        config = kwargs["config"]
        frozen = config["finnhub_news_snapshot"]
        assert frozen["start_date"] == "2026-06-24" and frozen["end_date"] == "2026-06-30"
        assert config["news_trade_date"] == "2026-07-01"
        assert frozen["eligible_records"] == 0
        raise RuntimeError("test stops before LLM")
    monkeypatch.setattr(run_agents, "_import_official", lambda: (
        SimpleNamespace(__file__=__file__, __version__="0.6.0"),
        lambda: SimpleNamespace(get_stats=lambda: {"tokens_in": 0, "tokens_out": 0}),
        None, graph, DEFAULT_CONFIG,
    ))
    with pytest.raises(RuntimeError, match="test stops"):
        run_agents.run_one("AAPL", "2026-07-01", logs_dir=tmp_path)
    record = json.loads((tmp_path / "runs.jsonl").read_text(encoding="utf-8"))
    snapshot = record["data_snapshot"]["sources"]["news"]
    assert len(snapshot["sha256"]) == 64 and snapshot["timezone"] == "America/New_York"
    assert snapshot["article_limit"] == 20 and snapshot["returned_records"] == 0
