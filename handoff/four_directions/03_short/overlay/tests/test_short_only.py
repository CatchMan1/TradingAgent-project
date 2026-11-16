import pandas as pd
import pytest
from experiments.optimization_engine import simulate

def prices(next_price=90,dividend=0):
    return pd.DataFrame([dict(date='2026-08-01',open=100,split=1,dividend=0),dict(date='2026-08-03',open=100,split=1,dividend=0),dict(date='2026-08-04',open=next_price,split=1,dividend=dividend),dict(date='2026-08-05',open=next_price,split=1,dividend=0)])

def test_short_sale_is_liability_not_immediate_profit():
    f,m=simulate(prices(),{'2026-08-01':'Underweight'},'2026-08-03','2026-08-03',short=True,short_authorizations={'2026-08-01':True},fee_bps=0,borrow_apr=0)
    assert m['total_return']==pytest.approx(.1)
    assert f.iloc[-1].shares==0 and f.iloc[-1]['cash']==pytest.approx(110000)

def test_short_loses_on_rise_and_pays_dividend_and_borrow():
    f,m=simulate(prices(110,2),{'2026-08-01':'Sell'},'2026-08-03','2026-08-03',short=True,short_authorizations={'2026-08-01':True},fee_bps=0,borrow_apr=.0365)
    assert m['final_equity']==pytest.approx(87990)
    assert f.iloc[0].dividend_cash==-2000 and m['borrow_cost']==pytest.approx(10)

def test_off_switch_preserves_original_and_unapproved_hold_covers_short():
    ratings={'2026-08-01':'Underweight','2026-08-03':'Hold'};auth={'2026-08-01':True,'2026-08-03':False}
    off,m=simulate(prices(),ratings,'2026-08-03','2026-08-04',short_authorizations=auth,fee_bps=0)
    assert m['total_return']==0 and m['short_days']==0
    on,m=simulate(prices(),ratings,'2026-08-03','2026-08-04',short=True,short_authorizations=auth,fee_bps=0,borrow_apr=0)
    assert list(on.actual_weight)==[-1,0]

def test_short_requires_affirmative_review_and_cannot_override_buys():
    with pytest.raises(ValueError,match='exit'):
        simulate(prices(),{'2026-08-01':'Buy'},'2026-08-03','2026-08-03',short=True,short_authorizations={'2026-08-01':True})

def test_adverse_gap_triggers_margin_cover_at_next_open():
    f,m=simulate(prices(160),{'2026-08-01':'Sell','2026-08-03':'Sell'},'2026-08-03','2026-08-04',short=True,short_authorizations={'2026-08-01':True,'2026-08-03':True},fee_bps=0,borrow_apr=0)
    assert bool(f.iloc[1].margin_cover) and f.iloc[1].actual_weight==0
    assert m['final_equity']==pytest.approx(40000)
