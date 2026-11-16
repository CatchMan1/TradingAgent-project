"""AAPL sentiment experiment using original decision prompts and separate execution."""
import argparse
from concurrent.futures import ThreadPoolExecutor,as_completed
from copy import deepcopy
import json
import os
from types import SimpleNamespace
from pydantic import model_validator
from dotenv import load_dotenv
from openai import OpenAI
from tokenizers import Tokenizer
import pandas as pd
from agents.historical_sentiment import NewsSentimentBatch,summarize,run_sentiment_pipeline,PROMPT
from experiments import full_position_pair as base

from experiments.fixed_position_comparison import simulate,metrics
from tradingagents.graph.propagation import Propagator

ARCHIVED_OUT=base.ROOT/'results/sentiment_aapl_aug2026_paired'
OUT=base.ROOT/'results/sentiment_aapl_aug2026_original_prompts'
EVIDENCE=base.ROOT/'results/sentiment_aapl_aug2026_offline'
REFERENCE=base.ROOT/'results/full_pipeline_position_2026aug_sep'
RISK_RULES=''
COMMON=''
from experiments.original_sentiment_client import OriginalClient


def prepare():
    OUT.mkdir(exist_ok=True)
    coverage=base.util.read(EVIDENCE/'coverage.json');days=[x['day'] for x in coverage['days']];sources={}
    for day in days:
        bundle=base.util.read(EVIDENCE/'inputs'/f'{day}.json')
        if base.util.digest(__import__('pathlib').Path(bundle['source_path']))!=bundle['source_sha256']:raise ValueError('News source changed')
        frozen=base.util.read(REFERENCE/'inputs'/f'AAPL_08_{day}.json')
        payload=dict(bundle=bundle,reports={k:frozen['state'][k] for k in ['market_report','news_report','fundamentals_report']},past_context=frozen['past_context'])
        target=OUT/'inputs'/f'{day}.json'
        if target.exists() and base.util.read(target)!=payload:raise ValueError('Input changed')
        base.util.save(target,payload);sources[day]=base.util.digest(target)
    p=dict(ticker='AAPL',month='2026-08',signal_dates=days,input_hashes=sources,model='deepseek-flash',
        arms=['sentiment'],debate_rounds=1,risk_rounds=1,fractional=False,short=False,
        initial_cash=100000,fee_bps=10,execution='next open; final liquidation next-month first open',
        common_rules=COMMON,risk_rules=RISK_RULES,sentiment_prompt=PROMPT,
        prices_sha256=base.util.digest(base.ROOT/'data/prices/AAPL.csv'),
        code_hashes={str(p.relative_to(base.ROOT)):base.util.digest(p) for p in [base.ROOT/'agents/historical_sentiment.py',base.ROOT/'experiments/run_sentiment_month.py',base.ROOT/'experiments/full_position_pair.py',base.ROOT/'experiments/original_sentiment_client.py']},
        limitation='Original full risk prompts and native model client; only sentiment report added. Archived original comparison, same model alias but separate stochastic invocations; retrospective news and one stock-month limit inference.')
    if (OUT/'protocol.json').exists() and base.util.read(OUT/'protocol.json')!=p:raise ValueError('Protocol changed')
    base.util.save(OUT/'protocol.json',p);return p

def run_arm(arm,protocol,guard,only_day=None):
    tok=Tokenizer.from_file(str(base.util.TOKENIZER));decisions=[]
    with OpenAI(api_key=os.environ['DEEPSEEK_API_KEY'],base_url='https://api.deepseek.com',max_retries=0,timeout=180.) as api:
        for day in ([only_day] if only_day else protocol['signal_dates']):
            path=OUT/'inputs'/f'{day}.json'
            if base.util.digest(path)!=protocol['input_hashes'][day]:raise ValueError('Input changed')
            payload=base.util.read(path)
            state=Propagator().create_initial_state('AAPL',day,past_context=payload['past_context'],instrument_context='')
            state.update(payload['reports'])
            def client(name,current):
                return OriginalClient(guard,tok,f'{arm}_{day}_{name}',name,payload['bundle'],ARCHIVED_OUT)
            state=run_sentiment_pipeline(state,payload['bundle'],client,enabled=arm=='sentiment')
            base.util.save(OUT/'decisions'/f'{arm}_{day}.json',state)
            decisions.append({'Buy':1.,'Overweight':1.,'Hold':None,'Underweight':0.,'Sell':0.}[state['final_rating']])
            print('COMPLETE',arm,day,state['final_rating'],flush=True)
    if only_day:return
    prices=pd.read_csv(base.ROOT/'data/prices/AAPL.csv')
    if base.util.digest(base.ROOT/'data/prices/AAPL.csv')!=protocol['prices_sha256']:raise ValueError('Prices changed')
    rows=simulate(prices,protocol['signal_dates'],decisions)
    pd.DataFrame(rows).to_csv(OUT/f'trades_{arm}.csv',index=False)
    base.util.save(OUT/f'metrics_{arm}.json',metrics(rows))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--live',action='store_true');ap.add_argument('--budget',type=float,default=8.)
    ap.add_argument('--arm',choices=['sentiment'],default='sentiment')
    args=ap.parse_args();p=prepare();selected=p['arms'] if args.arm=='both' else [args.arm]
    print('SELECTED',selected,'21 days',flush=True)
    if not args.live:return
    base.OUT=OUT;base.util.OUT=OUT;load_dotenv(base.ROOT/'.env',override=False)
    from tradingagents.dataflows.files import locked
    with locked(OUT/'run',wait=False) as acquired:
        if not acquired:raise RuntimeError('Already running')
        guard=base.IndependentSpendGuard(args.budget);failures=[]
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures={pool.submit(run_arm,arm,p,guard,day):(arm,day) for day in p['signal_dates'] for arm in selected}
            for f in as_completed(futures):
                try:f.result()
                except Exception as exc:
                    failure=dict(arm=futures[f],type=type(exc).__name__,error=str(exc)[:300]);failures.append(failure);print('FAILED',failure,flush=True)
        if not failures:
            for arm in selected:run_arm(arm,p,guard)  # validated cached replay; no new API calls
        base.util.save(OUT/'failures.json',failures);base.util.save(OUT/'balance_end.json',base.util.balance())
        if failures:raise SystemExit(1)
if __name__=='__main__':main()
