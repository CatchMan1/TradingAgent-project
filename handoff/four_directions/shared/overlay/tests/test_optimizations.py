import pandas as pd
import pytest

from experiments.optimization_engine import rebalance, simulate, target_weight


def market(opens, dividends=None, splits=None):
    return pd.DataFrame(dict(date=pd.bdate_range("2026-09-01",periods=len(opens)).strftime("%Y-%m-%d"),
                             open=opens, split=splits or [1.]*len(opens),
                             dividend=dividends or [0.]*len(opens)))


def test_fractional_target_and_hold():
    assert target_weight("Overweight",0,True)==.5
    assert target_weight("Underweight",0,True)==0
    assert target_weight("Underweight",.8,True)==.25
    assert target_weight("Hold",.8,True) is None
    assert target_weight("Sell",0,short=True)==-1
    with pytest.raises(ValueError):
        target_weight("REVIEW",0)


def test_reversal_cost_uses_both_sides_and_post_fee_equity():
    notional,cost=rebalance(100.,100.,-1.,.01)
    assert cost==pytest.approx(2/1.01)
    assert notional==pytest.approx(-(100-cost))
    assert cost==pytest.approx(.01*abs(notional-100))


def test_next_open_and_partial_gain():
    p=market([10.,100.,110.])
    frame,m=simulate(p,{"2026-09-01":"Overweight"},"2026-09-02","2026-09-02",fractional=True,fee_bps=0)
    assert m["total_return"]==pytest.approx(.05)
    assert frame.execution_date.iloc[0]=="2026-09-02"


def test_hold_retains_shares_and_does_not_rebalance_weight():
    p=market([100.,100.,200.,300.])
    f,m=simulate(p,{"2026-09-01":"Overweight","2026-09-02":"Hold"},"2026-09-02","2026-09-03",fractional=True,fee_bps=0)
    assert f.actual_weight.iloc[1]==pytest.approx(2/3)
    assert m["total_return"]==pytest.approx(1.)


def test_short_profit_and_dividend_liability():
    p=market([100.,100.,90.],dividends=[0.,0.,2.])
    _,m=simulate(p,{"2026-09-01":"Sell"},"2026-09-02","2026-09-02",short=True,fee_bps=0,borrow_apr=0)
    assert m["total_return"]==pytest.approx(.08)
    assert m["short_days"]==1


def test_short_loss_and_weekend_borrow():
    p=pd.DataFrame(dict(date=["2026-09-03","2026-09-04","2026-09-07"],open=[100.,100.,110.],split=[1.,1.,1.],dividend=[0.,0.,0.]))
    _,m=simulate(p,{"2026-09-03":"Sell"},"2026-09-04","2026-09-04",short=True,fee_bps=0,borrow_apr=.365)
    assert m["total_return"]==pytest.approx(-.103)
    assert m["borrow_cost"]==pytest.approx(300.)


def test_split_does_not_create_gain():
    p=market([100.,100.,50.],splits=[1.,1.,2.])
    _,m=simulate(p,{"2026-09-01":"Buy"},"2026-09-02","2026-09-02",fee_bps=0)
    assert m["total_return"]==pytest.approx(0)


def test_entry_exit_fees_and_initial_drawdown():
    p=market([100.,100.,100.])
    _,m=simulate(p,{"2026-09-01":"Buy"},"2026-09-02","2026-09-02",fee_bps=100)
    assert m["total_return"]==pytest.approx(.99/1.01-1)
    assert m["max_drawdown"]==pytest.approx(m["total_return"])


def test_missing_signal_and_bankruptcy_fail_closed():
    p=market([100.,100.,250.])
    with pytest.raises(ValueError,match="Missing decision"):
        simulate(p,{},"2026-09-02","2026-09-02")
    with pytest.raises(ValueError,match="Insolvent"):
        simulate(p,{"2026-09-01":"Sell"},"2026-09-02","2026-09-02",short=True)


def test_pipeline_rounds_sentiment_isolation_and_resume(tmp_path, monkeypatch):
    """Exercise the real experiment orchestrator with deterministic local nodes."""
    from experiments import run_optimizations as runner
    from agents import single_agent
    import tradingagents.agents as agents
    import tradingagents.llm_clients as clients
    from tradingagents.agents.schemas import SentimentReport

    calls=[]
    class FakeLLM:
        def get_llm(self):
            return self
        def with_structured_output(self, schema):
            return self
        def invoke(self,prompt):
            calls.append("sentiment")
            return SentimentReport(overall_band="Bullish",overall_score=7.,confidence="low",narrative="A dated news headline.")
    monkeypatch.setattr(clients,"create_tier_client",lambda *a,**kw:FakeLLM())
    monkeypatch.setattr(single_agent,"_runtime_config",lambda p:{})
    def factory(name):
        def make(llm):
            def node(state):
                calls.append(name)
                if name in {"bull","bear"}:
                    return {"investment_debate_state":{**state["investment_debate_state"],
                            "count":state["investment_debate_state"]["count"]+1}}
                if name=="portfolio":
                    count=state["investment_debate_state"]["count"]
                    assert count in {2,6}
                    rating="Sell" if count==6 else "Buy" if state["sentiment_report"] else "Overweight"
                    return dict(final_rating=rating,final_trade_decision=f"Rating: {rating}")
                return {}
            return node
        return make
    for exported,name in [("create_bull_researcher","bull"),("create_bear_researcher","bear"),
                          ("create_research_manager","research"),("create_trader","trader"),
                          ("create_aggressive_debator","aggressive"),("create_conservative_debator","conservative"),
                          ("create_neutral_debator","neutral"),("create_portfolio_manager","portfolio")]:
        monkeypatch.setattr(agents,exported,factory(name))
    day="2026-08-31"
    payload=dict(ticker="AAPL",trade_date=day,past_context="past",news="dated news",
                 reports=dict(market_report="market",news_report="news",fundamentals_report="facts"))
    runner.save(tmp_path/"inputs"/f"{day}.json",dict(payload=payload,sha256=runner.sha(payload)))
    runner.run_cell(tmp_path,day,{"model":"deepseek-flash"})
    assert len(calls)==37
    for name,rating in [("baseline","Overweight"),("sentiment","Buy"),("debate_3","Sell"),("combined","Sell")]:
        assert runner.read(tmp_path/"cells"/day/f"decision_{name}.json")["rating"]==rating
    calls.clear()
    runner.run_cell(tmp_path,day,{"model":"deepseek-flash"})
    assert calls==[]
    payload["news"]="changed"
    runner.save(tmp_path/"inputs"/f"{day}.json",dict(payload=payload,sha256=runner.sha(payload)))
    with pytest.raises(ValueError,match="Stale checkpoint"):
        runner.run_cell(tmp_path,day,{"model":"deepseek-flash"})
