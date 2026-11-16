from types import SimpleNamespace
import pytest
from experiments import debate_month as m


def test_budget_blocks_without_balance_and_never_reserves(tmp_path,monkeypatch):
    monkeypatch.setattr(m,'balance',lambda:{'cny':10.,'queried_at_utc':'now'})
    b=m.Budget(tmp_path,5.)
    b.acquire('first')
    b.release('first',{'status':'success'})
    monkeypatch.setattr(m,'balance',lambda:{'cny':5.5,'queried_at_utc':'later'})
    with pytest.raises(m.BudgetStop):b.acquire('second')
    assert not b.inflight


def test_frozen_memory_skips_settlement():
    from tradingagents.graph.trading_graph import TradingAgentsGraph
    fake=SimpleNamespace(config={'frozen_past_context':'Known on signal day'})
    assert TradingAgentsGraph._memory_step(fake,{})['past_context']=='Known on signal day'


def test_frozen_news_needs_no_api_key(monkeypatch):
    from tradingagents.dataflows.vendors.finnhub import news
    from tradingagents.dataflows.config import run_config
    monkeypatch.setattr(news,'get_api_key',lambda:pytest.fail('Frozen news requested API key'))
    monkeypatch.setattr(news,'_window',lambda *a:({'articles':[]},{'timezone':'America/New_York'}))
    with run_config({'finnhub_news_snapshot':{'path':'offline'}}):
        assert news.prepare_news_snapshot('AAPL','2026-09-01')['eligible_records']==0
