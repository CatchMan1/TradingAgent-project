"""Reproduce published position-sizing results with no external dependencies."""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(p):
    with p.open() as f:return list(csv.DictReader(f))

def run(records,arm):
    p=0.;nav=peak=1.;rows=[]
    for x in records:
        r=x['rating']
        if arm=='original_fractional':w=float(x['manager_target'])
        elif arm=='buy_hold':w=1.
        elif arm=='rating_25pp':
            w={'Buy':1.,'Sell':0.,'Hold':p,'Overweight':min(1.,p+.25),'Underweight':max(0.,p-.25)}[r]
        else:w=1. if r in ['Buy','Overweight'] else 0. if r in ['Sell','Underweight'] else p
        asset=float(x['asset_return']);turn=abs(w-p);fee=.001*turn;net=w*asset-fee
        nav+=net;peak=max(peak,nav)
        rows.append(dict(signal_date=x['signal_date'],return_end=x['return_end'],target_weight=w,asset_return=asset,turnover=turn,fee=fee,net_return=net,nav=nav,drawdown=nav/peak-1));p=w
    return rows

for folder,arms in [('fixed_25pp_full',['binary','rating_25pp','buy_hold']),('manager_aapl_aug',['original_binary','original_fractional','buy_hold'])]:
    root=ROOT/folder;inputs=load(root/'replay_inputs.csv');metrics=load(root/'metrics.csv')
    for ticker in sorted({x['ticker'] for x in inputs}):
        records=[x for x in inputs if x['ticker']==ticker]
        for arm in arms:
            rows=run(records,arm);saved=load(root/f'{ticker}_{arm}_daily.csv');assert len(rows)==len(saved)
            for a,b in zip(rows,saved):
                for k,v in a.items():
                    assert v==b[k] if isinstance(v,str) else abs(v-float(b[k]))<1e-10,(folder,ticker,arm,k)
            m=next(x for x in metrics if x['ticker']==ticker and x['strategy']==arm)
            result={'net_return_pct':(rows[-1]['nav']-1)*100,'max_drawdown_pct':-min(0.,*(r['drawdown'] for r in rows))*100,'mean_exposure_pct':sum(x['target_weight'] for x in rows)/len(rows)*100,'fee_pp':sum(x['fee'] for x in rows)*100}
            for k,v in result.items():assert abs(v-float(m[k]))<1e-10,(folder,ticker,arm,k)
            print(f'{folder}/{ticker}/{arm}: return {result["net_return_pct"]:+.4f}%, MDD {result["max_drawdown_pct"]:.4f}%')
print('PASS: all 12 stock/strategy combinations reconcile daily and aggregate results.')
