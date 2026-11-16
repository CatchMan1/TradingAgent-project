import json
from types import SimpleNamespace
import pytest
from tradingagents.agents.schemas import ResearchPlan,TraderProposal,PortfolioDecision
from agents.position_full_pipeline import SizedPortfolioDecision,run_pipeline
from experiments.full_position_pair import initial_state
from experiments.position_account import Account,execute_interval

@pytest.mark.parametrize('target',[-.1,1.1,True,'0.4',float('nan')])
def test_invalid_final_target(target):
    with pytest.raises(ValueError):SizedPortfolioDecision(rating='Buy',executive_summary='x',investment_thesis='x',execution_action='rebalance',target_weight_now=target)

def test_full_original_roles_and_final_authority():
    calls=[];prompts={}
    class Fake:
        final_sized_decision=None
        def __init__(self,name):self.name=name
        def with_structured_output(self,schema):
            def invoke(prompt):
                calls.append(self.name);prompts[self.name]=str(prompt)
                if schema is ResearchPlan:return ResearchPlan(recommendation='Buy',rationale='bull evidence',strategic_actions='suggest 80%')
                if schema is TraderProposal:return TraderProposal(action='Buy',reasoning='suggest 60%',position_sizing='60%')
                assert schema is PortfolioDecision
                result=SizedPortfolioDecision(rating='Overweight',executive_summary='risk adjusted to 25%',investment_thesis='reviewed all risk roles',execution_action='rebalance',target_weight_now=.25)
                self.final_sized_decision=result;return result
            return SimpleNamespace(invoke=invoke)
        def invoke(self,prompt):
            calls.append(self.name);prompts[self.name]=prompt
            return SimpleNamespace(content=f'{self.name} risk evidence')
    frozen={'state':dict(company_of_interest='AAPL',trade_date='2026-08-03',market_report='market',news_report='news',fundamentals_report='fundamentals',sentiment_report='',investment_debate_state={'history':'bull and bear','bull_history':'bull','bear_history':'bear'}),'past_context':'dated prior lesson'}
    state=run_pipeline(initial_state(frozen,Account().snapshot('2026-08-03',100.,[])),lambda name,s:Fake(name))
    assert calls==['research','trader','aggressive','conservative','neutral','portfolio']
    assert state['risk_debate_state']['count']==3
    for term in ['aggressive risk evidence','conservative risk evidence','neutral risk evidence','dated prior lesson','suggest 80%','suggest 60%']:
        assert term in prompts['portfolio']
    final=state['final_position'];a=Account()
    d=dict(action=final['execution_action'],target_weight_now=final['target_weight_now'],rationale='x',why_change_from_current='x',increase_condition='x',reduce_condition='x')
    r=execute_interval(a,d,'2026-08-03',dict(date='2026-08-04',open=100,split=1,dividend=0),dict(date='2026-08-05',open=101,split=1,dividend=0))
    assert r['actual_weight']==pytest.approx(.25)

def test_hold_keeps_shares_requires_null():
    with pytest.raises(ValueError):SizedPortfolioDecision(rating='Hold',executive_summary='x',investment_thesis='x',execution_action='rebalance',target_weight_now=.25)
    with pytest.raises(ValueError):SizedPortfolioDecision(rating='Buy',executive_summary='x',investment_thesis='x',execution_action='keep_shares',target_weight_now=.25)

def test_truncated_risk_response_retries_with_more_capacity(tmp_path,monkeypatch):
    from experiments import full_position_pair as m
    monkeypatch.setattr(m,'OUT',tmp_path)
    requested=[];released=[]
    class Client:
        def create(self,**kwargs):
            requested.append(kwargs['max_tokens'])
            raw=dict(model='test',usage={'prompt_tokens':10,'completion_tokens':8192 if len(requested)==1 else 20},
                choices=[{'finish_reason':'length' if len(requested)==1 else 'stop','message':{'content':'risk evidence'}}])
            return SimpleNamespace(model_dump=lambda **k:raw)
    api=SimpleNamespace(chat=SimpleNamespace(completions=Client()))
    guard=SimpleNamespace(acquire=lambda *a:None,release=lambda identity,r:released.append(r))
    tok=SimpleNamespace(encode=lambda *a,**k:SimpleNamespace(ids=[1]))
    stage=m.StageClient(api,guard,tok,'test_risk',{},'conservative')
    assert stage.call('original risk prompt',None)=='risk evidence'
    assert requested==[8192,12288]
    assert [r['status'] for r in released]==['failed','success']
    assert stage.call('original risk prompt',None)=='risk evidence'
    assert len(requested)==2

def test_compact_risk_bounds_and_preserves_account_and_opponents():
    from experiments.compact_risk_position import CompactStageClient,RISK_RULES
    class Tok:
        def encode(self,text,**kw):return SimpleNamespace(ids=list(text))
        def decode(self,ids):return ''.join(ids)
    account={'cash':123,'shares':7,'current_weight':.42}
    client=CompactStageClient(None,None,Tok(),'offline',account,'neutral')
    client.state={'trade_date':'2026-08-03','company_of_interest':'AAPL','trader_investment_plan':'T'*20000,
        'market_report':'M'*20000,'news_report':'N'*20000,'fundamentals_report':'F'*20000,
        'risk_debate_state':{'current_aggressive_response':'Aggressive Analyst: add to 60%',
                            'current_conservative_response':'Conservative Analyst: keep 20%'}}
    messages=client.messages('Neutral role. Here is the trader full repeated inputs',None)
    payload=json.loads(messages[1]['content'])
    assert len(messages[1]['content'])<4000
    assert '中间内容省略' in payload['trader_plan']
    assert '60%' in payload['previous_risk_views']['current_aggressive_response']
    assert '20%' in payload['previous_risk_views']['current_conservative_response']
    assert json.dumps(account,ensure_ascii=False) in messages[0]['content']
    assert RISK_RULES in messages[0]['content']
    assert client.request_options()['extra_body']['thinking']['type']=='disabled'
    client.stage='portfolio'
    assert client.request_options()['extra_body']['thinking']['type']=='enabled'
    assert client.messages('complete original evidence',None)[1]['content']=='complete original evidence'
