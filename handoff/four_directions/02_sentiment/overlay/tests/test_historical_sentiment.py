from copy import deepcopy
from datetime import datetime
from types import SimpleNamespace
import pytest
from agents.historical_sentiment import (prepare_articles,summarize,NewsSentimentBatch,ArticleSentiment,
    create_historical_sentiment_node,run_sentiment_pipeline)

def article(title='AAPL demand improves',stamp='2026-08-04T12:00:00+00:00',id=1):
    return dict(id=id,datetime=datetime.fromisoformat(stamp).timestamp(),headline=title,summary='Demand improved, but costs increased.',source='test',url='https://example.test/news')
def bundle(articles=None):
    return prepare_articles(dict(symbol='AAPL',articles=articles if articles is not None else [article()]),'2026-08-04')
def result(b,score=1):
    return NewsSentimentBatch(items=[ArticleSentiment(article_id=a['article_id'],relevant=True,score=score,evidence_type='mixed',quote=a['title'],reason='正面需求与成本风险并存',confidence='low') for a in b['articles']])

def test_timezone_cutoff_and_dedup():
    b=bundle([article(),article(id=2),article('late','2026-08-05T03:59:59+00:00',3),article('future','2026-08-05T04:00:00+00:00',4),article('old','2026-07-28T12:00:00+00:00',5)])
    assert len(b['articles'])==2
    assert b['excluded']==dict(outside_window=2,invalid=0,duplicate=1)

def test_unknown_evidence_and_fabricated_quotes_fail_closed():
    b=bundle();r=result(b);r.items[0].quote='invented quote'
    with pytest.raises(ValueError,match='quote'):summarize(b,r)
    r=result(b);r.items[0].article_id='unknown'
    with pytest.raises(ValueError,match='IDs'):summarize(b,r)
    r=result(b);r.items.append(r.items[0])
    with pytest.raises(ValueError,match='IDs'):summarize(b,r)

def test_missing_is_unavailable_not_neutral_and_no_call():
    b=bundle([]);state=dict(company_of_interest='AAPL',trade_date='2026-08-04')
    report=create_historical_sentiment_node(None,b)(state)['sentiment_report']
    assert 'unavailable' in report and '"score": null' in report
    assert summarize(bundle(),result(bundle(),0))['band']=='neutral'
    assert create_historical_sentiment_node(None,bundle(),False)(state)=={'sentiment_report':''}

def test_score_and_evidence_alignment():
    b=bundle();assert summarize(b,result(b))['score']==.5
    with pytest.raises(ValueError):result(b,True)
    with pytest.raises(ValueError):result(b,3)
    with pytest.raises(ValueError,match='mismatch'):
        create_historical_sentiment_node(None,b)(dict(company_of_interest='GOOGL',trade_date='2026-08-04'))

@pytest.mark.parametrize('enabled',[False,True])
def test_real_original_pipeline_isolation_and_sentiment_before_debate(enabled):
    from tradingagents.graph.propagation import Propagator
    from tradingagents.agents.schemas import ResearchPlan,TraderProposal,PortfolioDecision
    state=Propagator().create_initial_state('AAPL','2026-08-04',past_context='past',instrument_context='US stock')
    state.update(market_report='market',news_report='news',fundamentals_report='facts')
    before=deepcopy(state);calls=[];prompts={};b=bundle()
    class Fake:
        def __init__(self,name):self.name=name
        def with_structured_output(self,schema):
            def invoke(prompt):
                calls.append(self.name);prompts[self.name]=str(prompt)
                if schema is NewsSentimentBatch:return result(b)
                if schema is ResearchPlan:return ResearchPlan(recommendation='Buy',rationale='reviewed evidence',strategic_actions='Buy')
                if schema is TraderProposal:return TraderProposal(action='Buy',reasoning='evidence',position_sizing='original')
                assert schema is PortfolioDecision
                return PortfolioDecision(rating='Buy',executive_summary='evidence',investment_thesis='evidence')
            return SimpleNamespace(invoke=invoke)
        def invoke(self,prompt):
            calls.append(self.name);prompts[self.name]=str(prompt)
            return SimpleNamespace(content='Evidence: '+('sentiment present' if enabled else 'baseline'))
    final=run_sentiment_pipeline(state,b,lambda name,s:Fake(name),enabled)
    assert calls==(['sentiment'] if enabled else [])+['bull','bear','research','trader','aggressive','conservative','neutral','portfolio']
    assert ('Archived news only' in prompts['bull'])==enabled
    assert ('Archived news only' in prompts['bear'])==enabled
    assert ('Archived news only' in prompts['aggressive'])==enabled
    assert 'target_weight_now' not in final
    assert final['final_rating']=='Buy'
    assert state==before

def test_archive_window_is_stricter_than_signal_date():
    snapshot=dict(symbol='AAPL',start_date='2026-07-28',end_date='2026-08-03',articles=[article(),article('allowed','2026-08-03T12:00:00+00:00',2)])
    b=prepare_articles(snapshot,'2026-08-04')
    assert [a['title'] for a in b['articles']]==['allowed']
    assert b['excluded']['outside_window']==1

@pytest.mark.parametrize('stage',['bull','bear','research','trader','portfolio','aggressive','conservative','neutral'])
def test_original_decision_prompts_have_no_added_execution_mandate(stage):
    from experiments.original_sentiment_client import OriginalClient
    from experiments.run_sentiment_month import OUT,ARCHIVED_OUT,RISK_RULES,COMMON
    from tradingagents.agents.schemas import PortfolioDecision
    c=OriginalClient(None,None,'offline',stage,bundle(),ARCHIVED_OUT)
    original=[dict(role='system',content='Original role instructions'),dict(role='user',content='Full original evidence '*3000)]
    assert c.messages(original,None)==original
    assert c.messages(original,PortfolioDecision)==original
    assert c.messages(original[1]['content'])==[original[1]]
    assert OUT!=ARCHIVED_OUT
    assert not RISK_RULES and not COMMON


def test_html_entity_equivalent_quote_remains_source_grounded():
    a=article();a['summary']='Company&#39;s demand rose &amp; costs fell.'
    b=bundle([a]);r=result(b);r.items[0].quote="Company's demand rose & costs fell."
    assert summarize(b,r)['status']=='available'
    r.items[0].quote="Company's demand doubled & costs fell."
    with pytest.raises(ValueError,match='quote'):summarize(b,r)

def test_invisible_news_formatting_is_not_a_fabricated_quote():
    a=article();a['summary']='Testing \u200cchips across\xa0product lines.'
    b=bundle([a]);r=result(b);r.items[0].quote='Testing chips across product lines.'
    assert summarize(b,r)['status']=='available'
    r.items[0].quote='Testing superior chips across product lines.'
    with pytest.raises(ValueError,match='quote'):summarize(b,r)

def test_typographic_quotes_are_formatting_not_changed_facts():
    a=article();a['summary']='Company’s demand rose.'
    b=bundle([a]);r=result(b);r.items[0].quote="Company's demand rose."
    assert summarize(b,r)['status']=='available'
    r.items[0].quote="Company's demand fell."
    with pytest.raises(ValueError,match='quote'):summarize(b,r)

def test_headline_capitalization_does_not_change_quote_words():
    b=bundle();r=result(b);r.items[0].quote=b['articles'][0]['title'].upper()
    assert summarize(b,r)['status']=='available'
    r.items[0].quote='AAPL demand collapses'
    with pytest.raises(ValueError,match='quote'):summarize(b,r)

def test_native_client_reuses_successful_original_fallback_without_api(tmp_path,monkeypatch):
    import json
    from experiments.original_sentiment_client import OriginalClient,base
    from tradingagents.agents.schemas import PortfolioDecision
    monkeypatch.setattr(base,'OUT',tmp_path)
    c=OriginalClient(None,None,'day_portfolio','portfolio',bundle(),tmp_path)
    prompt='original prompt';messages=c.messages(prompt)
    sha=base.util.sha_text(json.dumps(messages,sort_keys=True,ensure_ascii=False))
    base.util.save(tmp_path/'native_cache/day_portfolio_plain.json',dict(content='**Rating**: Hold',prompt_sha256=sha))
    assert c.with_structured_output(PortfolioDecision).invoke(prompt) is None
    assert c.invoke(prompt).content=='**Rating**: Hold'
