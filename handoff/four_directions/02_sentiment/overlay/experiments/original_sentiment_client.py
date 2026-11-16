"""Cache/billing adapter around the project's unchanged native model client."""
from copy import deepcopy
from datetime import datetime,timezone
from types import SimpleNamespace
import json,time,uuid
from langchain_core.callbacks import BaseCallbackHandler
from tradingagents.llm_clients.factory import create_llm_client
from experiments import full_position_pair as base
from agents.historical_sentiment import NewsSentimentBatch,summarize

class NativeAudit(BaseCallbackHandler):
    raise_error=True
    def __init__(self,owner,record):self.owner,self.record=owner,record
    def on_llm_end(self,response,**kwargs):
        raw=response.model_dump(mode='json')
        base.util.save(base.OUT/'responses'/f"{self.owner.identity}_{self.record['call_id']}.json",raw)
        message=response.generations[0][0].message
        usage=message.response_metadata.get('token_usage',{})
        if not usage:usage=(response.llm_output or {}).get('token_usage',{})
        hit=usage.get('prompt_cache_hit_tokens',0)
        self.record.update(usage=usage,model=message.response_metadata.get('model_name','deepseek-flash'))
        if 'prompt_tokens' in usage and 'completion_tokens' in usage:
            self.record['estimated_cny']=(usage['prompt_tokens']-hit+.02*hit+4*usage['completion_tokens'])/1e6*base.util.price_multiplier()
        if message.response_metadata.get('finish_reason')=='length':raise ValueError('Truncated original-client response')

class OriginalClient:
    def __init__(self,guard,tok,identity,stage,bundle,archive):
        self.guard,self.tok,self.identity,self.stage,self.bundle,self.archive=guard,tok,identity,stage,bundle,archive
    def with_structured_output(self,schema):return SimpleNamespace(invoke=lambda prompt:self.call(prompt,schema))
    def invoke(self,prompt):return SimpleNamespace(content=self.call(prompt,None))
    def messages(self,prompt,schema=None):
        return [dict(role='user',content=prompt)] if isinstance(prompt,str) else deepcopy(prompt)
    def call(self,prompt,schema):
        messages=self.messages(prompt);sha=base.util.sha_text(json.dumps(messages,sort_keys=True,ensure_ascii=False))
        kind=schema.__name__ if schema else 'plain'
        path=base.OUT/'native_cache'/f'{self.identity}_{kind}.json'
        fallback=base.OUT/'native_cache'/f'{self.identity}_plain.json'
        if schema and fallback.exists():
            if base.util.read(fallback)['prompt_sha256']!=sha:raise ValueError('Original fallback prompt mismatch')
            return None  # Original node follows its cached plain-text fallback, without another call.
        if path.exists():
            saved=base.util.read(path)
            if saved['prompt_sha256']!=sha:raise ValueError('Original prompt mismatch')
            return schema.model_validate_json(saved['content']) if schema else saved['content']
        if self.stage=='sentiment':
            day=self.identity.split('_')[1];source=self.archive/'decisions'/f'sentiment_{day}.json'
            prior=base.util.read(source);report=json.loads(prior['sentiment_report'])
            previous_bundle=base.util.read(self.archive/'inputs'/f'{day}.json')['bundle']
            assert self.bundle==previous_bundle
            result=NewsSentimentBatch(items=report['items']);assert summarize(self.bundle,result)==report
            content=result.model_dump_json();call_id='reused-validated-sentiment'
            base.util.save(base.OUT/'reuse'/f'{day}.json',dict(source=str(source),source_sha256=base.util.digest(source),new_api_cost=0))
        else:
            # Same provider settings as the original runner; no forced thinking/effort,
            # no prompt additions, no compact risk path, no altered JSON schema prompt.
            llm=create_llm_client('deepseek','deepseek-flash',temperature=0.,max_tokens=8192,max_retries=2,timeout=120.).get_llm()
            bound=llm.with_structured_output(schema) if schema else llm
            call_id=str(uuid.uuid4());tokens=sum(len(self.tok.encode(m['content'],add_special_tokens=False).ids) for m in messages)
            self.guard.acquire(call_id,(tokens*1.15+8192*4)/1e6*2)
            record=dict(call_id=call_id,cell=self.identity,stage=self.stage,mode=kind,prompt_sha256=sha,started_at_utc=datetime.now(timezone.utc).isoformat())
            started=time.monotonic()
            try:
                result=bound.invoke(prompt,config={'callbacks':[NativeAudit(self,record)]})
                if result is None:raise ValueError('Original structured call returned no parsed result')
                content=result.model_dump_json() if schema else result.content
                if not content:raise ValueError('Empty response')
                record['status']='success'
            except Exception as exc:
                record.update(status='failed',error_type=type(exc).__name__);raise
            finally:
                record['elapsed_seconds']=time.monotonic()-started;self.guard.release(call_id,record)
        saved=dict(content=content,prompt_sha256=sha,call_id=call_id,mode=kind)
        base.util.save(path,saved);base.util.save(base.OUT/'calls'/f'{self.identity}.json',saved)
        base.util.save(base.OUT/'prompts'/f'{self.identity}.json',messages)
        return schema.model_validate_json(content) if schema else content
