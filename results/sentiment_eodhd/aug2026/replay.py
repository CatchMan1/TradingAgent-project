"""Offline replay of all published arms. Standard library only; no API calls."""
import json
from pathlib import Path
from datetime import date
from statistics import mean, stdev

ROOT=Path(__file__).resolve().parent
RATING={'Buy':1.,'Overweight':1.,'Sell':0.,'Underweight':0.,'Hold':None}

def simulate(records,arm):
    pos=0.;nav=peak=1.;rows=[]
    key={'news_plus_eodhd':'news_plus_eodhd_rating','original_multi_agent_archived':'original_multi_agent_rating','news_only_archived':'news_only_rating'}.get(arm)
    for x in records:
        rating=x[key] if key else 'Overweight';target=RATING[rating]
        target=pos if target is None else target
        ret=x['next_close']/x['signal_close']-1;turnover=abs(target-pos);cost=.001*turnover
        net=target*ret-cost;nav+=net;peak=max(peak,nav);pos=target
        rows.append(dict(signal_date=x['signal_date'],return_end=x['return_end'],rating=rating,target_position=target,
            turnover=turnover,cost=cost,asset_return=ret,strategy_return=net,additive_nav=nav,drawdown=nav/peak-1))
    return dict(net_return_pct=(nav-1)*100,max_drawdown_pct=-min(x['drawdown'] for x in rows)*100,
        mean_exposure=mean(x['target_position'] for x in rows),turnover=sum(x['turnover'] for x in rows),n_intervals=len(rows),rows=rows)

def main():
    for ticker in ['AAPL','AMZN']:
        records=json.loads((ROOT/ticker/'replay_inputs.json').read_text())
        expected=json.loads((ROOT/ticker/'evaluation.json').read_text())
        assert len(records)==21 and len({x['signal_date'] for x in records})==21
        assert records[0]['signal_date']=='2026-07-31' and records[-1]['return_end']=='2026-08-31'
        for arm,archived in expected.items():
            result=simulate(records,arm)
            for key in ['net_return_pct','max_drawdown_pct','mean_exposure','turnover','n_intervals']:
                assert abs(result[key]-archived[key])<1e-10,(ticker,arm,key)
            for a,b in zip(result['rows'],archived['rows']):
                for key in a:
                    if isinstance(a[key],(float,int)):assert abs(a[key]-b[key])<1e-10
                    else:assert a[key]==b[key]
            print(f"{ticker:4} {arm:30} return {result['net_return_pct']:+.4f}%  MDD {result['max_drawdown_pct']:.4f}%")
    print('PASS: every daily return, fee, position and metric matches the archive.')

if __name__=='__main__':main()
