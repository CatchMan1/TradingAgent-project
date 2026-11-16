"""Full original downstream pipeline plus sizing, six independent stock-months.

Archive ratings supply the exact original binary baseline. Analyst reports,
one-round debate and point-in-time memory are frozen, not regenerated.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor,as_completed
from copy import deepcopy
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import re
import time
import uuid
from types import SimpleNamespace
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from tokenizers import Tokenizer
from tradingagents.memory import TradingMemoryLog
from tradingagents.agents.schemas import PortfolioDecision
from agents.position_full_pipeline import STAGES,SIZING_RULES,SizedPortfolioDecision,run_pipeline,portfolio_block
from experiments import position_month as util
from experiments.position_other_stocks import IndependentSpendGuard
from experiments.position_account import Account,execute_interval,metrics
ROOT=util.ROOT
OUT=ROOT/'results/full_pipeline_position_2026aug_sep'
ARCHIVE=ROOT/'agents/logs/e/f6e0d4240635'

class StageClient:
    def __init__(self, client,guard,tok,identity,account,stage):
        self.client,self.guard,self.tok=client,guard,tok
        self.identity,self.account,self.stage=identity,account,stage
        self.schema=None;self.final_sized_decision=None
    def with_structured_output(self,schema):
        self.schema=SizedPortfolioDecision if schema is PortfolioDecision else schema
        return SimpleNamespace(invoke=lambda prompt:self.call(prompt,self.schema))
    def invoke(self,prompt):
        if self.schema is not None:raise ValueError('Structured stage failed; stop rather than bypass validated output')
        return SimpleNamespace(content=self.call(prompt,None))
    def messages(self,prompt,schema):
        messages=([{'role':'user','content':prompt}] if isinstance(prompt,str) else deepcopy(prompt))
        rules=SIZING_RULES+'\n'+portfolio_block(self.account)
        if schema:
            spec=schema.model_json_schema()
            # Original ResearchPlan description assumes no account; opt-in module supplies one.
            if schema.__name__=='ResearchPlan':
                spec['properties']['strategic_actions']['description']='Concrete steps and proposed target fraction for the trader, using the supplied account. Portfolio Manager makes the final decision.'
            rules+='\nReturn a JSON object matching this schema; retain original role reasoning:\n'+json.dumps(spec)
        messages.insert(0,{'role':'system','content':rules})
        return messages
    def request_options(self):
        return dict(max_tokens=8192,reasoning_effort="high",extra_body={"thinking":{"type":"enabled"}})
    def call(self,prompt,schema):
        messages=self.messages(prompt,schema);sha=util.sha_text(json.dumps(messages,sort_keys=True,ensure_ascii=False))
        file=OUT/'calls'/f'{self.identity}.json'
        if file.exists():
            saved=util.read(file)
            if saved['prompt_sha256']!=sha:raise ValueError('Resume prompt/account mismatch')
            content=saved['content']
        else:
            util.save(OUT/'prompts'/f'{self.identity}.json',messages)
            tokens=sum(len(self.tok.encode(m['content'],add_special_tokens=False).ids) for m in messages)+64
            content=None
            options=self.request_options()
            max_output=options["max_tokens"]
            output_ceiling=getattr(self,'output_token_ceiling',16384) if options["extra_body"]["thinking"]["type"]=="enabled" else max_output
            for previous in (OUT/'responses').glob(f'{self.identity}_*.json'):
                prior=util.read(previous)
                if prior['choices'][0]['finish_reason']=='length':
                    max_output=max(max_output,min(output_ceiling,prior['usage']['completion_tokens']+4096))
            for attempt in range(2):
                call_id=str(uuid.uuid4());mult=util.price_multiplier()
                self.guard.acquire(call_id,(tokens*1.15+max_output*4)/1e6*max(2,mult))
                record=dict(call_id=call_id,cell=self.identity,stage=self.stage,attempt=attempt+1,
                    started_at_utc=datetime.now(timezone.utc).isoformat(),prompt_sha256=sha,max_output_tokens=max_output)
                started=time.monotonic()
                try:
                    kwargs=dict(model='deepseek-flash',messages=messages,**options)
                    kwargs['max_tokens']=max_output
                    if schema:kwargs['response_format']={'type':'json_object'}
                    response=self.client.chat.completions.create(**kwargs)
                    raw=response.model_dump(mode='json');util.save(OUT/'responses'/f'{self.identity}_{call_id}.json',raw)
                    u=raw['usage'];hit=u.get('prompt_cache_hit_tokens',0)
                    record.update(usage=u,model=raw['model'],estimated_cny=(u['prompt_tokens']-hit+.02*hit+4*u['completion_tokens'])/1e6*mult)
                    if raw['choices'][0]['finish_reason']!='stop':
                        if raw['choices'][0]['finish_reason']=='length':max_output=min(output_ceiling,max_output+4096)
                        raise ValueError('Incomplete model output')
                    content=raw['choices'][0]['message']['content']
                    if schema:schema.model_validate_json(content)
                    elif not content or not content.strip():raise ValueError('Empty risk argument')
                    record['elapsed_seconds']=time.monotonic()-started
                    record['status']='success';self.guard.release(call_id,record)
                    util.save(file,dict(content=content,prompt_sha256=sha,call_id=call_id));break
                except Exception as exc:
                    record.update(status='failed',error_type=type(exc).__name__,elapsed_seconds=time.monotonic()-started)
                    self.guard.release(call_id,record)
                    if attempt==1:raise
                    print('RETRY',self.identity,type(exc).__name__,flush=True)
            if content is None:raise RuntimeError('No response')
        result=schema.model_validate_json(content) if schema else content
        if schema is SizedPortfolioDecision:self.final_sized_decision=result
        return result
    def save_stage(self,update):
        # Preserve actual original-node output; AIMessage is represented as text.
        util.save(OUT/'stages'/f'{self.identity}.json',update)

def initial_state(frozen,account):
    state=deepcopy(frozen['state'])
    state['investment_debate_state']['count']=2
    state['risk_debate_state']=dict(history='',aggressive_history='',conservative_history='',neutral_history='',
        latest_speaker='',current_aggressive_response='',current_conservative_response='',current_neutral_response='',count=0)
    state['portfolio_context']=portfolio_block(account)
    state['past_context']=frozen['past_context']
    return state

def prepare():
    OUT.mkdir(exist_ok=True)
    memory=TradingMemoryLog({'memory_log_path':str(ARCHIVE/'memory/trading_memory.md')})
    groups={}
    for ticker in ['AAPL','GOOGL','AMZN']:
        prices=pd.read_csv(ROOT/f'data/prices/{ticker}.csv')
        for month in ['08','09']:
            indices=prices.index[prices.date.str.startswith(f'2026-{month}-')].tolist()
            days=[str(prices.iloc[i-1].date) for i in indices];group=f'{ticker}_{month}';sources={}
            for day in days:
                path=ARCHIVE/f'results/{ticker}/TradingAgentsStrategy_logs/full_states_log_{day}.json'
                old=util.read(path);debate=old['investment_debate_state']
                assert old['run_settings']['max_debate_rounds']==1 and old['run_settings']['max_risk_discuss_rounds']==1
                assert len(re.findall(r'(?m)^Bull Analyst:',debate['history']))==len(re.findall(r'(?m)^Bear Analyst:',debate['history']))==1
                state={k:old[k] for k in ['company_of_interest','trade_date','market_report','fundamentals_report','news_report','sentiment_report','investment_debate_state']}
                assert not state['sentiment_report']
                value=dict(state=state,past_context=memory.get_past_context(ticker,n_same=5,n_cross=3,as_of=day),original_rating=old['final_rating'])
                target=OUT/'inputs'/f'{group}_{day}.json'
                if target.exists():assert util.read(target)==value
                util.save(target,value);sources[day]=dict(archive_sha256=util.digest(path),input_sha256=util.digest(target))
            groups[group]=dict(ticker=ticker,month=month,signal_dates=days,sources=sources,prices_sha256=util.digest(ROOT/f'data/prices/{ticker}.csv'))
    p=dict(groups=groups,fee_bps=10.,initial_cash=100000.,model='deepseek-flash',thinking='enabled',max_tokens=8192,
        stages=[name for name,_ in STAGES],memory_sha256=util.digest(ARCHIVE/'memory/trading_memory.md'),
        sizing_rules=SIZING_RULES,baseline='Original archived full-pipeline final ratings, replayed with Buy/Overweight=1, Sell/Underweight=0, Hold=keep shares.',
        limitation='Original archived binary decisions versus newly sampled sizing decisions; same upstream evidence and original downstream role code, but model run dates and stochastic outputs differ. Not a freshly randomized paired causal estimate.')
    if (OUT/'protocol.json').exists():assert util.read(OUT/'protocol.json')==p
    util.save(OUT/'protocol.json',p)
    return p

def run_group(group,p,guard):
    config=p['groups'][group];ticker=config['ticker'];prices=pd.read_csv(ROOT/f'data/prices/{ticker}.csv')
    assert util.digest(ROOT/f'data/prices/{ticker}.csv')==config['prices_sha256']
    indices={r.date:i for i,r in prices.iterrows()};account=Account();rows=[];recent=[]
    tok=Tokenizer.from_file(str(util.TOKENIZER))
    with OpenAI(api_key=os.environ['DEEPSEEK_API_KEY'],base_url='https://api.deepseek.com',max_retries=0,timeout=180.) as client:
        for j,day in enumerate(config['signal_dates']):
            cell=f'{group}_{day}';path=OUT/'inputs'/f'{cell}.json'
            assert util.digest(path)==config['sources'][day]['input_sha256']
            frozen=util.read(path);i=indices[day];snapshot=account.snapshot(day,float(prices.iloc[i].close),recent)
            state=initial_state(frozen,snapshot)
            state=run_pipeline(state,lambda name,s:StageClient(client,guard,tok,f'{cell}_{name}',snapshot,name))
            final=state['final_position'];decision=dict(action=final['execution_action'],target_weight_now=final['target_weight_now'],
                rationale=final['investment_thesis'],why_change_from_current=final['executive_summary'],increase_condition='See final thesis',reduce_condition='See final thesis')
            row=execute_interval(account,decision,day,prices.iloc[i+1],prices.iloc[i+2],terminal=j==len(config['signal_dates'])-1)
            rows.append(row);recent.append({k:row[k] for k in ['execution_date','action','target_weight','traded_shares','trading_cost']})
            util.save(OUT/'decisions'/f'{cell}.json',dict(final=final,account_before=snapshot,row=row))
            pd.DataFrame(rows).to_csv(OUT/f'trades_{group}.csv',index=False)
            print('COMPLETE',cell,final['rating'],final['execution_action'],final['target_weight_now'],flush=True)
    util.save(OUT/f'metrics_{group}.json',metrics(rows))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--live',action='store_true');parser.add_argument('--budget',type=float,default=22.)
    parser.add_argument('--group',choices=['AAPL_08','AAPL_09','GOOGL_08','GOOGL_09','AMZN_08','AMZN_09'])
    args=parser.parse_args();p=prepare();selected=[args.group] if args.group else list(p['groups'])
    print('SELECTED',selected,'days',sum(len(p['groups'][g]['signal_dates']) for g in selected),flush=True)
    if not args.live:return
    from tradingagents.dataflows.files import locked
    load_dotenv(ROOT/'.env',override=False);util.OUT=OUT
    with locked(OUT/'run',wait=False) as acquired:
        if not acquired:raise RuntimeError('Already running')
        guard=IndependentSpendGuard(args.budget);failures=[]
        with ThreadPoolExecutor(max_workers=len(selected)) as pool:
            futures={pool.submit(run_group,g,p,guard):g for g in selected}
            for f in as_completed(futures):
                try:f.result()
                except Exception as exc:
                    failure=dict(group=futures[f],error_type=type(exc).__name__,error=str(exc)[:300]);failures.append(failure);print('FAILED',failure,flush=True)
        util.save(OUT/'failures.json',failures);util.save(OUT/'balance_end.json',util.balance())
        if failures:raise SystemExit(1)

if __name__=='__main__':main()
