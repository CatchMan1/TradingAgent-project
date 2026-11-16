"""Paired full-graph AAPL September experiment with frozen news/memory and spend guard."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PureWindowsPath
import threading
import time

import pandas as pd
import requests
from dotenv import load_dotenv
from langchain_core.callbacks import BaseCallbackHandler

from agents.debate_config import DebateOptions
from agents.run_agents import run_one, append_decision, DEFAULT_ANALYSTS
from agents.single_agent import build_evidence, REFERENCE_LOGS
from data import ROOT
from experiments.optimization_engine import simulate

OUT=ROOT/'results/debate_aapl_sep2026_paired'

def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_suffix('.tmp')
    tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
    tmp.replace(path)

def read(path):
    return json.loads(path.read_text())

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def balance():
    r=requests.get('https://api.deepseek.com/user/balance',
                   headers={'Authorization':'Bearer '+os.environ['DEEPSEEK_API_KEY']},timeout=30)
    if r.status_code!=200:
        raise RuntimeError(f'Balance query HTTP {r.status_code}')
    d=r.json()
    amount=next(float(x['total_balance']) for x in d['balance_infos'] if x['currency']=='CNY')
    return dict(cny=amount,queried_at_utc=datetime.now(timezone.utc).isoformat())

class BudgetStop(BaseException):
    pass

class Budget:
    """Serialize read-only balance checks; reserve ¥1 per in-flight request.

    A conservative operational stop, not a provider-enforced billing limit.
    SDK retries are disabled; stop on unknown balance rather than spend blind.
    """
    def __init__(self,output,cap):
        self.output=output
        self.condition=threading.Condition()
        self.inflight=set()
        self.cap=cap
        self.stopped=False
        initial=output/'balance_start.json'
        now=balance()
        if not initial.exists():save(initial,now)
        self.start=read(initial)['cny']
        self.latest=now
        self.reservation=1.
    def acquire(self,identity):
        with self.condition:
            while True:
                if self.stopped:raise BudgetStop('Budget guard stopped new requests')
                try:self.latest=balance()
                except Exception:
                    self.stopped=True
                    self.condition.notify_all()
                    raise BudgetStop('Balance unavailable; paused without new model calls')
                spent=max(0.,self.start-self.latest['cny'])
                room=min(self.latest['cny']-1.,self.cap-spent)-len(self.inflight)*self.reservation
                save(self.output/'balance_latest.json',{**self.latest,'account_decrease_cny':spent,
                      'inflight_reserved_cny':len(self.inflight)*self.reservation,'cap_cny':self.cap})
                if room>=self.reservation:
                    self.inflight.add(identity)
                    return
                if not self.inflight:
                    self.stopped=True
                    self.condition.notify_all()
                    raise BudgetStop('Budget/remaining balance reserve reached; resume after approval')
                self.condition.wait(timeout=5.)
    def release(self,identity,record):
        with self.condition:
            self.inflight.discard(identity)
            with (self.output/'api_calls.jsonl').open('a') as f:
                f.write(json.dumps(record,ensure_ascii=False,default=str)+'\n')
            self.condition.notify_all()

class CallAudit(BaseCallbackHandler):
    raise_error=True
    def __init__(self,budget,cell):
        self.budget=budget;self.cell=cell;self.starts={}
    def on_chat_model_start(self,serialized,messages,*,run_id,**kwargs):
        key=str(run_id)
        self.budget.acquire(key)
        self.starts[key]=time.monotonic()
    def on_llm_start(self,serialized,prompts,*,run_id,**kwargs):
        self.on_chat_model_start(serialized,prompts,run_id=run_id,**kwargs)
    def on_llm_end(self,response,*,run_id,**kwargs):
        key=str(run_id)
        message=response.generations[0][0].message
        usage=message.usage_metadata or {}
        meta=message.response_metadata or {}
        raw=meta.get('token_usage',{})
        inp=usage.get('input_tokens',0);out=usage.get('output_tokens',0)
        hit=raw.get('prompt_cache_hit_tokens',usage.get('input_token_details',{}).get('cache_read',0))
        # Off-peak estimate. Account balance delta remains the billing reference.
        estimate=(max(0,inp-hit)+hit*.02+out*4)/1e6
        self.budget.release(key,dict(cell=self.cell,run_id=key,status='success',usage=usage,
            provider_usage=raw,model=meta.get('model_name') or meta.get('model'),
            finish_reason=meta.get('finish_reason'),offpeak_estimated_cny=estimate,
            elapsed_seconds=time.monotonic()-self.starts.pop(key,time.monotonic()),
            completed_at_utc=datetime.now(timezone.utc).isoformat()))
    def on_llm_error(self,error,*,run_id,**kwargs):
        key=str(run_id)
        if key in self.starts:
            self.budget.release(key,dict(cell=self.cell,run_id=key,status='failed',
                error_type=type(error).__name__,elapsed_seconds=time.monotonic()-self.starts.pop(key)))

def prepare(output):
    prices=pd.read_csv(ROOT/'data/prices/AAPL.csv')
    ix=prices.index[(prices.date>='2026-09-01')&(prices.date<='2026-09-30')]
    days=[prices.iloc[i-1].date for i in ix]
    protocol=dict(ticker='AAPL',start='2026-09-01',end='2026-09-30',signal_dates=days,
        research_rounds=[1,3],risk_rounds=1,model='deepseek-flash',temperature=0.,
        analysts=list(DEFAULT_ANALYSTS),memory='same frozen reference context resolved by each signal day',
        pipeline='full original graph; analysts regenerated in both arms',
        cutoff='market_close',fee_bps=10.,initial_cash=100000.,
        terminal_valuation='2026-10-01 open, final liquidation charged',
        data_sha256={k:digest(ROOT/f'data/{k}/AAPL.csv') for k in ['prices','financials']})
    if (output/'protocol.json').exists() and read(output/'protocol.json')!=protocol:
        raise ValueError('Protocol changed; use new output')
    save(output/'protocol.json',protocol)
    for day in days:
        path=output/'inputs'/f'{day}.json'
        if path.exists():continue
        b=build_evidence('AAPL',day,cutoff_policy='market_close')
        snap=dict(b['data_snapshot']['sources']['news'])
        snap['path']=str(REFERENCE_LOGS/'cache/finnhub'/PureWindowsPath(snap['path']).name)
        if digest(Path(snap['path']))!=snap['sha256']:raise ValueError('News changed')
        save(path,dict(day=day,news_snapshot=snap,past_context=b['evidence']['past_context'],
                       memory_sha256=b['memory']['context_sha256']))
    protocol['input_hashes']={d:digest(output/'inputs'/f'{d}.json') for d in days}
    save(output/'frozen_inputs.json',protocol['input_hashes'])
    return protocol

def run_cell(output,day,rounds,budget):
    cell=f'r{rounds}_{day}'
    result_path=output/'decisions'/f'{cell}.json'
    if result_path.exists():return cell,'skipped'
    hashes=read(output/'frozen_inputs.json')
    path=output/'inputs'/f'{day}.json'
    if digest(path)!=hashes[day]:raise ValueError('Frozen input changed')
    b=read(path)
    record=run_one('AAPL',day,analysts=list(DEFAULT_ANALYSTS),
        strategy_version=f'ta-paired-aapl-2026sep-r{rounds}-v1',
        logs_dir=output/'logs'/cell,debate_options=DebateOptions(enabled=rounds>1,rounds=rounds),
        frozen_news_snapshot=b['news_snapshot'],frozen_past_context=b['past_context'],
        extra_callbacks=[CallAudit(budget,cell)])
    save(result_path,record)
    print('CELL COMPLETE',cell,record['action'],flush=True)
    return cell,'success'

def evaluate(output):
    protocol=read(output/'protocol.json')
    p=pd.read_csv(ROOT/'data/prices/AAPL.csv')
    results=[];missing={}
    for rounds in [1,3]:
        rows=[];ratings={}
        for day in protocol['signal_dates']:
            path=output/'decisions'/f'r{rounds}_{day}.json'
            if not path.exists():missing.setdefault(str(rounds),[]).append(day);continue
            r=read(path);rows.append(r['decision_row'])
            ratings[day]=r['final_rating'].title()
        if rows:pd.DataFrame(rows).to_csv(output/f'decisions_r{rounds}.csv',index=False)
        if str(rounds) in missing:continue
        frame,metrics=simulate(p,ratings,protocol['start'],protocol['end'],fee_bps=10.)
        frame.to_csv(output/f'trades_r{rounds}.csv',index=False)
        results.append(dict(rounds=rounds,**metrics))
    calls=[]
    if (output/'api_calls.jsonl').exists():calls=[json.loads(x) for x in (output/'api_calls.jsonl').read_text().splitlines()]
    costs={}
    for n in [1,3]:
        arm=[r for r in calls if r['cell'].startswith(f'r{n}_')]
        costs[str(n)]={'recorded_calls':len(arm),'failed_calls':sum(r['status']=='failed' for r in arm),
          'input_tokens':sum(r.get('usage',{}).get('input_tokens',0) for r in arm),
          'output_tokens':sum(r.get('usage',{}).get('output_tokens',0) for r in arm),
          'offpeak_estimated_cny':sum(r.get('offpeak_estimated_cny',0) for r in arm)}
    report=dict(protocol=protocol,metrics=results,missing=missing,costs=costs,
      limitation='One stock/month, one stochastic realization. No claim of significance. Shared frozen historical memory, no new reflection settlement.')
    save(output/'report.json',report)
    if results:pd.DataFrame(results).to_csv(output/'metrics.csv',index=False)
    return report

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare',action='store_true');parser.add_argument('--live',action='store_true')
    parser.add_argument('--evaluate',action='store_true');parser.add_argument('--workers',type=int,default=8)
    parser.add_argument('--budget',type=float,default=50.);parser.add_argument('--limit',type=int)
    a=parser.parse_args();OUT.mkdir(parents=True,exist_ok=True)
    load_dotenv(ROOT/'.env',override=False)
    if a.prepare:prepare(OUT)
    if a.live:
        from tradingagents.dataflows.files import locked
        with locked(OUT/'run',wait=False) as acquired:
            if not acquired:raise RuntimeError('Experiment already running')
            # Pin both arms to identical provider settings; no hidden retry charges.
            os.environ.update(TRADINGAGENTS_LLM_PROVIDER='deepseek',TRADINGAGENTS_QUICK_THINK_LLM='deepseek-flash',
               TRADINGAGENTS_DEEP_THINK_LLM='deepseek-flash',TRADINGAGENTS_TEMPERATURE='0',
               TRADINGAGENTS_LLM_MAX_RETRIES='0',TRADINGAGENTS_MAX_TOKENS='8192')
            protocol=read(OUT/'protocol.json')
            for k,v in protocol['data_sha256'].items():
                if digest(ROOT/f'data/{k}/AAPL.csv')!=v:raise ValueError('Market source changed')
            budget=Budget(OUT,a.budget)
            cells=[(d,n) for d in protocol['signal_dates'] for n in [1,3]]
            if a.limit:cells=cells[:a.limit]
            failures=[]
            with ThreadPoolExecutor(max_workers=a.workers) as pool:
                futures={pool.submit(run_cell,OUT,d,n,budget):(d,n) for d,n in cells}
                for fut in as_completed(futures):
                    try:print(fut.result(),flush=True)
                    except (Exception,BudgetStop) as exc:
                        failures.append(dict(cell=futures[fut],error_type=type(exc).__name__,error=str(exc)))
                        print('CELL FAILED',futures[fut],type(exc).__name__,str(exc),flush=True)
            save(OUT/'failures.json',failures)
            save(OUT/'balance_end.json',balance())
            evaluate(OUT)
            if failures:raise SystemExit(1)
    elif a.evaluate:print(json.dumps(evaluate(OUT),ensure_ascii=False))

if __name__=='__main__':main()
