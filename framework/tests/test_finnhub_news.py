"""Finnhub integration tests use only mocked HTTP and a scripted local model."""

from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

import pytest
import requests
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.runnables import RunnableLambda
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode

from tradingagents.agents import tools
from tradingagents.agents.analysts.news_analyst import create_news_analyst
from tradingagents.dataflows.config import run_config
from tradingagents.dataflows.date_window import previous_news_window
from tradingagents.dataflows.errors import VendorUnavailableError
from tradingagents.dataflows.router import route_to_vendor
from tradingagents.dataflows.vendors.finnhub import news
from tradingagents.graph.analyst_execution import build_analyst_execution_plan
from tradingagents.graph.setup import _analyst_graph


def article(when, headline, identity=1):
    return {"id": identity, "datetime": int(datetime.fromisoformat(when).timestamp()),
            "headline": headline, "summary": "evidence", "source": "test-source",
            "url": f"https://example.test/{identity}"}


@pytest.fixture
def config(tmp_path, monkeypatch):
    monkeypatch.setenv("FINNHUB_API_KEY", "dummy-secret")
    monkeypatch.setattr(news.time, "sleep", lambda _: None)
    return {"data_cache_dir": str(tmp_path), "news_previous_days_only": True,
            "news_company_only": True, "news_trade_date": "2026-07-01",
            "news_timezone": "America/New_York", "news_article_limit": 20,
            "data_vendors": {"news_data": "finnhub"}, "tool_vendors": {"get_news": "finnhub"}}


def mock_http(monkeypatch, payload, status=200):
    calls = []

    def respond(url, **kwargs):
        calls.append((url, kwargs))
        return SimpleNamespace(status_code=status, json=lambda: payload)

    monkeypatch.setattr(news.requests, "get", respond)
    return calls


def test_ny_boundaries_header_auth_and_routed_vendor(config, monkeypatch):
    payload = [
        article("2026-06-24T03:59:59+00:00", "too early", 1),
        article("2026-06-24T04:00:00+00:00", "first eligible", 2),
        article("2026-07-01T03:59:59+00:00", "last eligible", 3),
        article("2026-07-01T04:00:00+00:00", "same NY day", 4),
        {"datetime": "invalid", "headline": "undated"},
    ]
    calls = mock_http(monkeypatch, payload)
    with run_config(config):
        report = route_to_vendor("get_news", "AAPL", "2026-06-24", "2026-06-30")
    assert "first eligible" in report and "last eligible" in report
    assert all(text not in report for text in ("too early", "same NY day", "undated", "dummy-secret"))
    assert len(calls) == 1
    url, kwargs = calls[0]
    assert url == news.API_BASE_URL
    assert kwargs["params"] == {"symbol": "AAPL", "from": "2026-06-24", "to": "2026-07-01"}
    assert kwargs["headers"] == {"X-Finnhub-Token": "dummy-secret"}
    assert kwargs["timeout"] == 30


@pytest.mark.parametrize("trade,expected", [
    ("2026-07-01", ("2026-06-24", "2026-06-30")),
    ("2026-08-06", ("2026-07-30", "2026-08-05")),
    ("2026-01-02", ("2025-12-26", "2026-01-01")),
])
def test_previous_seven_calendar_days(trade, expected):
    assert previous_news_window(None, None, trade) == expected


@pytest.mark.parametrize("start,end", [
    ("2026-07-01", "2026-07-02"), ("2026-06-01", "2026-06-23"),
    ("2026-06-30", "2026-06-24"), ("2026-6-24", "2026-06-30"),
    ("invalid", "2026-06-30"),
])
def test_invalid_or_outside_window_is_not_requested(config, monkeypatch, start, end):
    calls = mock_http(monkeypatch, [])
    with run_config(config):
        with pytest.raises(ValueError):
            news.get_news("AAPL", start, end)
    assert not calls


def test_cache_frozen_subwindow_dedup_cap_and_hash(config, monkeypatch):
    first = article("2026-06-24T20:00:00+00:00", "older", 1)
    newest = article("2026-06-30T20:00:00+00:00", "newest", 2)
    calls = mock_http(monkeypatch, [first, newest, newest])
    config["news_article_limit"] = 1
    with run_config(config):
        snapshot = news.prepare_news_snapshot("AAPL", "2026-07-01")
        repeated = news.prepare_news_snapshot("AAPL", "2026-07-01")
    assert len(calls) == 1
    assert repeated["sha256"] == snapshot["sha256"]
    assert snapshot["returned_records"] == 3 and snapshot["eligible_records"] == 2
    config["finnhub_news_snapshot"] = snapshot
    with run_config(config):
        report = news.get_news("AAPL", "2026-06-29", "2026-06-30")
    assert "newest" in report and "older" not in report
    assert "supplied: 1" in report and len(calls) == 1
    path = Path(snapshot["path"])
    assert "dummy-secret" not in path.read_text(encoding="utf-8")
    path.write_text("{}", encoding="utf-8")
    with run_config(config), pytest.raises(VendorUnavailableError, match="snapshot"):
        news.get_news("AAPL", "2026-06-24", "2026-06-30")
    assert len(calls) == 1


def test_empty_window_is_explicit_and_cached(config, monkeypatch):
    calls = mock_http(monkeypatch, [])
    with run_config(config):
        report = news.get_news("AAPL", "2026-06-24", "2026-06-30")
        news.get_news("AAPL", "2026-06-24", "2026-06-30")
    assert len(calls) == 1
    assert "no eligible timestamped news" in report
    assert "do not infer" in report


@pytest.mark.parametrize("status,error,attempts", [
    (401, news.FinnhubNotConfiguredError, 1),
    (403, news.FinnhubNotConfiguredError, 1),
    (429, news.FinnhubRateLimitError, 3),
    (503, VendorUnavailableError, 3),
])
def test_http_failure_never_cached_or_leaks_secret(config, monkeypatch, tmp_path, status, error, attempts):
    calls = mock_http(monkeypatch, {"error": "dummy-secret"}, status)
    with run_config(config), pytest.raises(error) as exc:
        news.prepare_news_snapshot("AAPL", "2026-07-01")
    assert "dummy-secret" not in str(exc.value)
    assert len(calls) == attempts
    assert not list(tmp_path.rglob("*.json"))


@pytest.mark.parametrize("payload", [{"error": "dummy-secret"}, [{"datetime": "invalid"}], [None]])
def test_invalid_payload_does_not_become_no_news(config, monkeypatch, payload, tmp_path):
    mock_http(monkeypatch, payload)
    with run_config(config), pytest.raises(VendorUnavailableError) as exc:
        news.prepare_news_snapshot("AAPL", "2026-07-01")
    assert "dummy-secret" not in str(exc.value)
    assert not list(tmp_path.rglob("*.json"))


def test_network_exception_is_sanitized(config, monkeypatch):
    def fail(*args, **kwargs):
        raise requests.RequestException("dummy-secret")
    monkeypatch.setattr(news.requests, "get", fail)
    with run_config(config), pytest.raises(VendorUnavailableError) as exc:
        news.get_news("AAPL", "2026-06-24", "2026-06-30")
    assert "dummy-secret" not in str(exc.value)


def test_new_york_dst_boundary_is_calendar_based():
    lower, upper = news._bounds("2026-03-07", "2026-03-08", "America/New_York")
    assert lower.isoformat() == "2026-03-07T05:00:00+00:00"
    assert upper.isoformat() == "2026-03-09T04:00:00+00:00"


def test_toolnode_injects_symbol_and_clamps_previous_days(config, monkeypatch):
    class State(MessagesState):
        company_of_interest: str
        trade_date: str
    captured = []
    monkeypatch.setattr(tools, "route_to_vendor", lambda *args: captured.append(args) or "ok")
    graph = StateGraph(State)
    graph.add_node("tools", ToolNode([tools.get_news]))
    graph.add_edge(START, "tools")
    graph.add_edge("tools", END)
    with run_config(config):
        graph.compile().invoke({"company_of_interest": "AAPL", "trade_date": "2026-07-01",
            "messages": [AIMessage("", tool_calls=[{"name": "get_news", "id": "1", "args": {
                "ticker": "AMZN", "trade_date": "2026-08-01",
                "start_date": "2026-01-01", "end_date": "2026-12-31"}}])]})
    assert captured == [("get_news", "AAPL", "2026-06-24", "2026-06-30")]


def test_news_analyst_receives_prefetched_evidence_without_tool_history(config, monkeypatch):
    calls = mock_http(monkeypatch, [article("2026-06-30T20:00:00+00:00", "eligible event")])
    turns = []

    def respond(prompt):
        messages = prompt.to_messages()
        turns.append(messages)
        assert not any(isinstance(m, ToolMessage) for m in messages)
        assert not any(getattr(m, "tool_calls", None) for m in messages)
        supplied = [m.content for m in messages if isinstance(m, HumanMessage)]
        assert any("eligible event" in content for content in supplied)
        return AIMessage(content="News report based on eligible event")

    with run_config(config):
        config["finnhub_news_snapshot"] = news.prepare_news_snapshot("AAPL", "2026-07-01")
    with run_config(config):
        spec = build_analyst_execution_plan(["news"]).specs[0]
        assert spec.tools == ()
        result = _analyst_graph(spec, create_news_analyst(RunnableLambda(respond)), 4).invoke({
            "company_of_interest": "AAPL", "trade_date": "2026-07-01", "asset_type": "stock",
            "messages": [HumanMessage(content="Analyze the historical company news")],
        })
    assert result["news_report"] == "News report based on eligible event"
    assert len(turns) == 1
    assert len(calls) == 1
