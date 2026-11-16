from copy import deepcopy
import json
import pandas as pd
import pytest
from experiments.position_account import Account, execute_interval, validate_decision, metrics
from experiments.optimization_engine import simulate


def decision(weight):
    return dict(action='keep_shares' if weight is None else 'rebalance', target_weight_now=weight,
                rationale='evidence', why_change_from_current='account', increase_condition='confirm', reduce_condition='invalidate')

def test_add_reduce_basis_fees_and_pnl_identity():
    a=Account(100000.)
    a.trade(100.,.2,10.)
    assert a.shares*100/a.equity(100)==pytest.approx(.2)
    assert a.average_cost==pytest.approx(100.1)
    prior=deepcopy(a)
    t=a.trade(110.,.35,10.)
    assert t['traded_shares']>0
    assert a.shares*110/a.equity(110)==pytest.approx(.35)
    assert a.average_cost>prior.average_cost
    basis=a.average_cost
    a.trade(120.,.1,10.)
    assert a.average_cost==pytest.approx(basis)
    snapshot=a.snapshot('day',120.,[])
    assert snapshot['unrealized_pnl']+a.realized_pnl==pytest.approx(a.equity(120.)-100000.)
    a.trade(120.,0.,10.)
    assert a.shares==a.average_cost==0.
    assert a.realized_pnl==pytest.approx(a.cash-100000.)

def test_keep_shares_is_not_constant_weight():
    a=Account(100.);a.trade(10.,.2,0.)
    before=vars(a).copy();a.trade(20.,None,0.)
    assert vars(a)==before
    assert a.snapshot('day',20.,[])['current_weight']==pytest.approx(1/3)

def test_future_valuation_does_not_leak_into_live_account():
    a=Account(100.)
    execution=dict(date='2026-09-01',open=10.,split=1.,dividend=0.)
    following=dict(date='2026-09-02',open=5.,split=2.,dividend=1.)
    row=execute_interval(a,decision(1.),'2026-08-31',execution,following,terminal=True,fee_bps=0.)
    assert row['equity']==pytest.approx(120.)
    assert a.shares==pytest.approx(10.)
    assert a.average_cost==pytest.approx(10.)
    assert a.dividends==0.
    # Actions are applied to the real account only when that execution day arrives.
    a.corporate_actions(following)
    assert a.shares==20. and a.average_cost==5. and a.cash==20.

@pytest.mark.parametrize('weight',[-.1,1.1,float('nan'),float('inf'),True,'0.5'])
def test_bad_model_weight_rejected(weight):
    with pytest.raises(ValueError):validate_decision(decision(weight))

def test_missing_reason_or_invalid_hold_is_rejected():
    d=decision(.3);del d['rationale']
    with pytest.raises(ValueError):validate_decision(d)
    d=decision(None);d['target_weight_now']=.3
    with pytest.raises(ValueError):validate_decision(d)

@pytest.mark.parametrize('rounds',[1,3])
def test_replay_old_binary_decisions_matches_original_engine(rounds):
    from experiments.position_month import ROOT,SOURCE
    p=pd.read_csv(ROOT/'data/prices/AAPL.csv');protocol=json.loads((SOURCE/'protocol.json').read_text())
    account=Account();rows=[];ratings={}
    for j,day in enumerate(protocol['signal_dates']):
        r=json.loads((SOURCE/'decisions'/f'r{rounds}_{day}.json').read_text())['final_rating'].title()
        ratings[day]=r
        target={'Overweight':1.,'Buy':1.,'Underweight':0.,'Sell':0.,'Hold':None}[r]
        i=p.index[p.date==day][0]
        rows.append(execute_interval(account,decision(target),day,p.iloc[i+1],p.iloc[i+2],terminal=j==20))
    old,old_metrics=simulate(p,ratings,protocol['start'],protocol['end'])
    assert [r['equity'] for r in rows]==pytest.approx(old.equity.tolist())
    new_metrics=metrics(rows)
    for k in ['total_return','max_drawdown','trading_cost','turnover','sharpe']:
        assert new_metrics[k]==pytest.approx(old_metrics[k])

def test_guard_counts_unknown_failed_request_and_blocks(tmp_path,monkeypatch):
    from experiments import position_month as m
    monkeypatch.setattr(m,'OUT',tmp_path)
    monkeypatch.setattr(m,'balance',lambda:dict(cny=10.,queried_at_utc='now'))
    g=m.SpendGuard(.3);g.acquire('one',.2);g.release('one',{'status':'api_error'})
    assert g.charged_estimate==.2
    with pytest.raises(m.SpendStop):g.acquire('two',.2)

@pytest.mark.parametrize('ticker',['AAPL','GOOGL'])
@pytest.mark.parametrize('include_history',[False,True])
def test_sequential_runner_passes_updated_account_not_future_valuation(tmp_path,monkeypatch,include_history,ticker):
    from experiments import position_month as m
    root=tmp_path/'root';out=tmp_path/'result'
    (root/'data/prices').mkdir(parents=True);(out/'inputs').mkdir(parents=True)
    prices=pd.DataFrame(dict(date=['2026-08-31','2026-09-01','2026-09-02','2026-09-03'],
        open=[90.,100.,130.,150.],close=[95.,120.,140.,155.],split=[1.]*4,dividend=[0.]*4))
    prices.to_csv(root/f'data/prices/{ticker}.csv',index=False)
    days=prices.date.tolist()[:2];sources={}
    for day in days:
        path=out/'inputs'/f'r1_{day}.json';m.save(path,{'signal_date':day,'debate_history':'frozen'})
        sources[f'r1_{day}']={'context_sha256':m.digest(path)}
    class FakeClient:
        def __init__(self,**kwargs):pass
        def close(self):pass
    seen=[]
    def fake_decision(client,guard,tok,cell,messages):
        seen.append(json.loads(messages[1]['content']))
        return decision(.2 if len(seen)==1 else None)
    monkeypatch.setattr(m,'ROOT',root);monkeypatch.setattr(m,'OUT',out)
    from types import SimpleNamespace
    monkeypatch.setattr(m,'Tokenizer',SimpleNamespace(from_file=lambda path:object()))
    monkeypatch.setattr(m,'OpenAI',FakeClient);monkeypatch.setattr(m,'get_decision',fake_decision)
    monkeypatch.setenv('DEEPSEEK_API_KEY','offline-test-not-a-key')
    m.run_arm(1,{'initial_cash':100000.,'signal_dates':days,'sources':sources,'fee_bps':10.,'include_previous_decisions':include_history,'ticker':ticker},None)
    a=Account();a.trade(100.,.2,10.)
    assert seen[0]['current_account']['shares']==0.
    state=seen[1]['current_account']
    assert state['shares']==pytest.approx(a.shares)
    assert state['average_cost_including_buy_fees']==pytest.approx(a.average_cost)
    assert state['total_equity']==pytest.approx(a.equity(120.))
    assert state['current_weight']==pytest.approx(a.shares*120./a.equity(120.))
    assert 'valuation_date' not in json.dumps(state)
    assert 'equity' not in state['recent_trades'][0]

    if include_history:
        assert seen[0]['previous_decisions']==[]
        assert seen[1]['previous_decisions']==[{'signal_date':days[0],**decision(.2)}]
    else:
        assert 'previous_decisions' not in seen[1]

def test_independent_stock_budget_does_not_count_other_runs(tmp_path,monkeypatch):
    from experiments import position_month as m
    from experiments.position_other_stocks import IndependentSpendGuard
    monkeypatch.setattr(m,'OUT',tmp_path)
    monkeypatch.setattr(m,'balance',lambda:dict(cny=20.,queried_at_utc='now'))
    guard=IndependentSpendGuard(.3)
    monkeypatch.setattr(m,'balance',lambda:dict(cny=18.,queried_at_utc='later'))
    guard.acquire('ours',.2)
    guard.release('ours',{'status':'api_error'})
    assert guard.charged_estimate==.2
    with pytest.raises(m.SpendStop):guard.acquire('next',.2)
