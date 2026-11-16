"""No-network tests for the independent module and the actual graph routing."""
import socket
from types import SimpleNamespace

import pytest
from langchain_core.messages import AIMessage

from agents.debate_config import DebateOptions


@pytest.fixture(autouse=True)
def prohibit_network(monkeypatch):
    def blocked(*args, **kwargs):
        pytest.fail("Offline test attempted network access")
    monkeypatch.setattr(socket.socket,"connect",blocked)
    monkeypatch.setattr(socket.socket,"connect_ex",blocked)
    monkeypatch.setattr(socket,"create_connection",blocked)


def test_default_three_and_disable_restores_one_without_mutation():
    original=dict(max_debate_rounds=9,max_risk_discuss_rounds=5,max_recur_limit=100,
                  temperature=0.,data_vendors={"news_data":"finnhub"})
    enabled=DebateOptions().apply(original)
    disabled=DebateOptions(enabled=False,rounds=8).apply(original)
    assert enabled["max_debate_rounds"]==3
    assert disabled["max_debate_rounds"]==1
    assert enabled["max_risk_discuss_rounds"]==disabled["max_risk_discuss_rounds"]==1
    assert original["max_debate_rounds"]==9
    for key in ("temperature","data_vendors"):
        assert enabled[key]==disabled[key]==original[key]


@pytest.mark.parametrize("bad",[0,-1,1.5,True,"3"])
def test_invalid_rounds_rejected(bad):
    with pytest.raises(ValueError,match="positive integer"):
        DebateOptions(rounds=bad)


@pytest.mark.parametrize("enabled,rounds,expected",[(True,3,3),(False,3,1),(True,2,2)])
def test_real_graph_turns_and_context(monkeypatch,enabled,rounds,expected):
    from tradingagents.graph.setup import GraphSetup
    from tradingagents.graph.conditional_logic import ConditionalLogic
    from tradingagents.graph.propagation import Propagator
    from tradingagents.dataflows.config import run_config
    prompts=[]
    class OfflineModel:
        def with_structured_output(self,*args,**kwargs):
            raise NotImplementedError("Offline free-text test double")
        def invoke(self,prompt):
            prompts.append(prompt)
            return AIMessage(content=f"Offline argument {len(prompts)}.\n**Rating**: Hold")
    def analyst(llm):
        return lambda state:dict(messages=[AIMessage(content="Frozen technical evidence")],
                                  market_report="Frozen technical evidence")
    monkeypatch.setattr("tradingagents.graph.setup.create_market_analyst",analyst)
    options=DebateOptions(enabled=enabled,rounds=rounds)
    config=options.apply({"max_recur_limit":100,"output_language":"English"})
    llm=OfflineModel()
    logic=ConditionalLogic(config["max_debate_rounds"],config["max_risk_discuss_rounds"])
    graph=GraphSetup(llm,llm,logic,max_tool_rounds=2).setup_graph(["market"]).compile()
    with run_config(config):
        result=graph.invoke(Propagator().create_initial_state("AAPL","2026-09-01"),
                            config={"recursion_limit":100})
    assert result["investment_debate_state"]["count"]==2*expected
    assert result["risk_debate_state"]["count"]==3
    assert result["final_rating"]=="Hold"
    assert len(prompts)==2*expected+6  # research manager, trader, three risk roles, PM
    for i in range(2*expected):
        assert ("You are a Bull Analyst" if i%2==0 else "You are a Bear Analyst") in prompts[i]
        if i:
            assert f"Offline argument {i}." in prompts[i]
    manager_prompt=prompts[2*expected]
    for i in range(1,2*expected+1):
        assert f"Offline argument {i}." in manager_prompt
    assert result["sentiment_report"]==""


def test_module_preview_does_not_import_model_graph(tmp_path,monkeypatch):
    from agents import run_agents
    monkeypatch.setattr(run_agents,"_snapshot_manifest",lambda *a,**kw:{"sources":{}})
    monkeypatch.setattr(run_agents,"_import_official",lambda:pytest.fail("Model graph imported"))
    result=run_agents.run_one("AAPL","2026-09-01",logs_dir=tmp_path,dry_run=True,
                              debate_options=DebateOptions())
    assert result["max_debate_rounds"]==3
    assert result["debate_module"]["expected_research_turns"]==6
    assert result["llm_calls"]==0


def test_entry_defaults_offline_and_isolates_output(monkeypatch):
    from agents import debate_agent
    captured=[]
    monkeypatch.setattr(debate_agent,"run_one",lambda *a,**kw:captured.append(kw) or {"status":"dry_run"})
    monkeypatch.setattr(debate_agent,"append_decision",lambda *a:pytest.fail("Preview wrote a decision"))
    debate_agent.main(["--ticker","AAPL","--date","2026-09-01"])
    debate_agent.main(["--ticker","AAPL","--date","2026-09-01","--no-multi-round"])
    assert all(c["dry_run"] for c in captured)
    assert captured[0]["debate_options"].effective_rounds==3
    assert captured[1]["debate_options"].effective_rounds==1
    assert captured[0]["strategy_version"]!=captured[1]["strategy_version"]
    assert captured[0]["logs_dir"]!=captured[1]["logs_dir"]
    assert all(c["analysts"]==["market","news","fundamentals"] for c in captured)
