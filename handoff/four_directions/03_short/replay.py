"""Reproduce all three stocks offline from compact fixtures; use project Python."""
import argparse,importlib.util,json,sys
from pathlib import Path
import pandas as pd
P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('handoff_engine',P.parent/'shared/overlay/experiments/optimization_engine.py');engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
p=argparse.ArgumentParser();p.add_argument('--ticker',choices=['AAPL','AMZN','GOOGL'],required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
prices=pd.read_csv(P/f'fixtures/{a.ticker}_prices.csv');ratings=json.loads((P/f'fixtures/{a.ticker}_ratings.json').read_text());expected=json.loads((P/f'fixtures/{a.ticker}_expected.json').read_text());result={}
for key,period in expected.items():
 start,end=period['start'],period['last_execution'];indices=prices.index[(prices.date>=start)&(prices.date<=end)];days=[prices.iloc[i-1].date for i in indices]
 mapped={d:'Sell' if r=='Underweight' else r for d,r in ratings.items()};bh={d:'Buy' if i==0 else 'Hold' for i,d in enumerate(days)};result[key]={}
 for name,rs,short in [('original',ratings,False),('underweight_short',mapped,True),('buy_hold',bh,False)]:
  frame,m=engine.simulate(prices,rs,start,end,short=short);frame['original_rating']=frame.signal_date.map(ratings);frame.to_csv(a.output/f'{key}_{name}.csv',index=False);result[key][name]=m
  for metric in ['total_return','max_drawdown','trading_cost','borrow_cost']:
   if abs(m[metric]-period['metrics'][name][metric])>1e-7:raise AssertionError(f'{key} {name} {metric}: regression differs')
(a.output/'metrics.json').write_text(json.dumps(result,indent=2));print(a.ticker,'all 5 periods x 3 strategies match; API calls: 0')
