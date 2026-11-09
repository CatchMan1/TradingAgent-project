"""Offline control: never call a real model, news API, or write reference memory."""
import copy
import csv
import json
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import pytest

from agents import single_agent as single
from data import ROOT
from experiments.run_experiments import _completed, load_manifest, run_manifest
from signals import validate_decisions


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    import requests
    import httpx
    def blocked(*args, **kwargs):
        raise AssertionError("Tests must never access the network")
    monkeypatch.setattr(requests.sessions.Session, "request", blocked)
    monkeypatch.setattr(httpx.Client, "send", blocked)


@pytest.fixture(scope="module")
def archived_bundle():
    return single.build_evidence("AAPL", "2026-08-03")


def test_shared_memory_news_and_cutoff_are_frozen(archived_bundle):
    from tradingagents.memory import TradingMemoryLog
    b = archived_bundle
    memory = single.REFERENCE_LOGS / "memory/trading_memory.md"
    before = memory.read_bytes()
    assert b["evidence"]["past_context"] == TradingMemoryLog(
        {"memory_log_path": str(memory)}).get_past_context("AAPL", as_of="2026-08-03")
    assert b["information_cutoff"] == "2026-08-03T23:59:59-04:00"
    news = b["data_snapshot"]["sources"]["news"]
    assert single._sha((single.REFERENCE_LOGS / news["path"]).read_bytes()) == news["sha256"]
    assert "fundamentals_report" not in b["evidence"]
    assert not b["alignment"]["original_prompt_identity_verified"]
    assert memory.read_bytes() == before


def test_seed_has_no_immature_memory():
    from tradingagents.memory import TradingMemoryLog
    memory = TradingMemoryLog({"memory_log_path": str(single.REFERENCE_LOGS / "memory/trading_memory.md")})
    assert memory.get_past_context("AAPL", as_of="2026-06-30") == ""
    assert memory.get_past_context("AAPL", as_of="2026-07-08")


@pytest.mark.parametrize("text", [
    '{"action":"REVIEW","reason":"unclear","risks":[]}',
    '{"action":"BUY","reason":"","risks":[]}',
    '{"action":"SELL","reason":"x","risks":"x"}',
    'BUY', '{"action":"BUY","reason":"x","risks":[]} extra',
    '{"action":"BUY","reason":"x","risks":[],"extra":"SELL"}',
])
def test_invalid_response_is_not_silently_hold(text):
    with pytest.raises(ValueError):
        single.parse_decision(text)


def test_response_recovery_makes_no_second_paid_call(monkeypatch, tmp_path, archived_bundle):
    monkeypatch.setattr(single, "build_evidence", lambda *a, **k: archived_bundle)
    monkeypatch.setenv("DEEPSEEK_API_KEY", "fake-key-for-unit-test-only")
    calls = []
    def fake(bundle, config, stats):
        calls.append(1)
        stats.llm_calls = 1
        stats.tokens_in, stats.tokens_out = 100, 20
        assert config["deep_think_llm"] == "deepseek-flash"
        return SimpleNamespace(content='{"action":"HOLD","reason":"Uncertain evidence","risks":["volatility"]}',
                               usage_metadata={"input_tokens":100,"output_tokens":20},
                               response_metadata={"model_name":"test-model"},additional_kwargs={})
    monkeypatch.setattr(single, "_call_model", fake)
    first = single.run_one("AAPL", "2026-08-03", logs_dir=tmp_path)
    assert first["status"] == "success" and first["input_tokens"] == 100
    assert first["decision_row"]["source"] == "single_agent"
    monkeypatch.delenv("DEEPSEEK_API_KEY")
    recovered = single.run_one("AAPL", "2026-08-03", logs_dir=tmp_path)
    assert recovered["status"] == "recovered"
    assert recovered["llm_calls"] == recovered["input_tokens"] == recovered["output_tokens"] == 0
    assert recovered["decision_row"] == first["decision_row"]
    assert len(calls) == 1
    changed = copy.deepcopy(archived_bundle)
    changed["evidence"]["news"] += " changed"
    monkeypatch.setattr(single, "build_evidence", lambda *a, **k: changed)
    with pytest.raises(ValueError, match="changed"):
        single.run_one("AAPL", "2026-08-03", logs_dir=tmp_path)
    assert len(calls) == 1


def test_dry_run_cannot_call_model(monkeypatch, tmp_path, archived_bundle):
    monkeypatch.setattr(single, "build_evidence", lambda *a, **k: archived_bundle)
    def forbidden(*args):
        pytest.fail("Dry run called a model")
    monkeypatch.setattr(single, "_call_model", forbidden)
    r = single.run_one("AAPL", "2026-08-03", logs_dir=tmp_path, dry_run=True)
    assert r["status"] == "dry_run" and r["llm_calls"] == 0
    assert "decision_row" not in r


def test_source_tampering_fails_before_model(monkeypatch, tmp_path):
    from shutil import copytree
    for name in ["prices", "financials"]:
        copytree(ROOT / "data" / name, tmp_path / name)
    (tmp_path / "sources.json").write_bytes((ROOT / "data/sources.json").read_bytes())
    price = tmp_path / "prices/AAPL.csv"
    price.write_bytes(price.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="source file hash"):
        single.build_evidence("AAPL", "2026-08-03", data_dir=tmp_path)


def test_matched_manifest_and_source_aware_resume(tmp_path):
    main = load_manifest(ROOT / "experiments/manifests/main_2026jul_oct_v1.csv")
    control = load_manifest(ROOT / "experiments/manifests/single_2026jul_oct_v1.csv")
    assert [(r["ticker"],r["trade_date"]) for r in control] == [(r["ticker"],r["trade_date"]) for r in main]
    assert len(control) == 216 and {r["analysts"] for r in control} == {"single_agent"}
    output = tmp_path / "partial.csv"
    with output.open("w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=["ticker","information_cutoff","source","strategy_version"])
        writer.writeheader();writer.writerow(dict(ticker="AAPL",information_cutoff="2026-06-30T16:00:00-04:00",source="portfolio_manager",strategy_version="test"))
    assert _completed(output,"test",source="single_agent") == set()
    with pytest.raises(ValueError,match="mode"):
        run_manifest(ROOT / "experiments/manifests/single_2026jul_oct_v1.csv",dry_run=True,mode="multi_agent")


def test_single_manifest_resumes_its_own_source(monkeypatch,tmp_path):
    import experiments.run_experiments as runner
    rows=load_manifest(ROOT/"experiments/manifests/single_2026jul_oct_v1.csv")[:3]
    manifest=tmp_path/"manifest.csv"
    with manifest.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    monkeypatch.setattr(runner,"DATA_DIR",tmp_path/"data")
    monkeypatch.setattr(runner,"ROOT",tmp_path)
    monkeypatch.setattr(runner,"_strategy_logs_dir",lambda s:tmp_path/"logs")
    monkeypatch.setattr(runner,"rebuild_audit_tables",lambda:(0,0))
    calls=[]
    def fake(ticker,trade_date,**kwargs):
        calls.append((ticker,trade_date))
        return dict(status="success",action="HOLD",input_tokens=10,output_tokens=3,elapsed_seconds=1,
            decision_row=dict(ticker=ticker,decision_time=trade_date+"T23:59:59.000001-04:00",
                information_cutoff=trade_date+"T23:59:59-04:00",action="HOLD",source="single_agent",strategy_version=kwargs["strategy_version"]))
    monkeypatch.setattr(single,"run_one",fake)
    first=run_manifest(manifest,mode="single_agent")
    second=run_manifest(manifest,mode="single_agent")
    assert first["success"]==3 and second["skipped"]==3 and len(calls)==3
    assert first["input_tokens"]==30 and second["input_tokens"]==0


def test_end_of_day_signals_need_explicit_policy():
    from signals import decision_sessions
    sessions=decision_sessions("2026-07-01","2026-07-02").index.strftime("%Y-%m-%d")
    rows=pd.DataFrame([dict(ticker="AAPL",decision_time=d+"T23:59:59.000001-04:00",
        information_cutoff=d+"T23:59:59-04:00",action="HOLD",strategy_version="test",source="single_agent") for d in sessions])
    with pytest.raises(ValueError):validate_decisions(rows,"AAPL","2026-07-01","2026-07-02",source="single_agent")
    assert len(validate_decisions(rows,"AAPL","2026-07-01","2026-07-02",source="single_agent",cutoff_policy="end_of_day"))==3
    rows.loc[0,"information_cutoff"]="2026-07-01T08:00:00-04:00"
    with pytest.raises(ValueError):validate_decisions(rows,"AAPL","2026-07-01","2026-07-02",source="single_agent",cutoff_policy="end_of_day")


def test_notebook_imports_both_strategies_with_same_formula(tmp_path):
    from signals import load_decisions
    nb=json.loads((ROOT/"analysis.ipynb").read_text())
    original=pd.read_csv(ROOT/"data/decisions"/(single.REFERENCE_STRATEGY+".csv"))
    control=original.copy()
    control["source"]="single_agent";control["strategy_version"]="test-single"
    target=tmp_path/"single.csv";control.to_csv(target,index=False)
    cell=next(c for c in nb["cells"] if "strategy_names = {" in "".join(c.get("source",[])) and "imported = load_decisions" in "".join(c.get("source",[])))
    scope=dict(pd=pd,Path=Path,cfg={"tickers":["AAPL","GOOGL","AMZN"],"sma":{"fast":20,"slow":50},"macd":{"fast":12,"slow":26,"signal":9}},
        TICKERS=["AAPL","GOOGL","AMZN"],AGENT_CSV=ROOT/"data/decisions"/(single.REFERENCE_STRATEGY+".csv"),AGENT_NAME="multi",
        SINGLE_AGENT_CSV=target,load_decisions=load_decisions,validate_decisions=validate_decisions,
        decision_tables={},backtest_start="2026-07-01",backtest_end="2026-10-09")
    exec("".join(cell["source"]),scope)
    assert {s for _,s in scope["decision_tables"]}=={"agent","single_agent"}
    assert all(len(r)==72 for r in scope["decision_tables"].values())
