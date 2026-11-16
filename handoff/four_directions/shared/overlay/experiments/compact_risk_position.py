"""Opt-in bounded risk-review rerun; original six-node order stays intact."""
import json
from copy import deepcopy
from experiments import full_position_pair as base

OUT=base.ROOT/'results/full_position_compact_risk_aapl_aug2026'
RISK_STAGES={'aggressive','conservative','neutral'}
RISK_RULES='''Concise risk-review mode: respond in Chinese, at most 450 Chinese characters, with five short items: proposed TOTAL target percentage; two decisive evidence points; downside versus cash opportunity cost; one substantive disagreement with prior reviewers (if any); why not a higher/lower allocation and whether any tiny holding has practical value. Do not retell all reports. State any missing information. These are excerpts, not complete source reports; do not claim omitted evidence is absent. Keep the original risk perspective; the final portfolio manager decides. No invented data.'''

def excerpt(text,tok,limit):
    ids=tok.encode(str(text),add_special_tokens=False).ids
    if len(ids)<=limit:return str(text)
    # Explicitly marked deterministic excerpts; no extra summarization API call.
    first=limit*2//3
    return tok.decode(ids[:first])+'\n[中间内容省略；完整证据仍由研究经理、交易员和最终组合经理审阅]\n'+tok.decode(ids[-(limit-first):])

class CompactStageClient(base.StageClient):
    def messages(self,prompt,schema):
        if self.stage in RISK_STAGES:
            s=self.state
            role=str(prompt).split('Here is the trader')[0]
            payload={'role':excerpt(role,self.tok,220),'date':s['trade_date'],'ticker':s['company_of_interest'],
                'trader_plan':excerpt(s['trader_investment_plan'],self.tok,1400),
                'reports':{k:excerpt(s.get(k,''),self.tok,400) for k in ['market_report','news_report','fundamentals_report']},
                'previous_risk_views':{k:excerpt(s['risk_debate_state'].get(k,''),self.tok,550) for k in ['current_aggressive_response','current_conservative_response','current_neutral_response']}}
            prompt=json.dumps(payload,ensure_ascii=False)
        messages=super().messages(prompt,schema)
        if self.stage in RISK_STAGES:messages[0]['content']+='\n'+RISK_RULES
        return messages
    def request_options(self):
        if self.stage in RISK_STAGES:
            return dict(max_tokens=1200,extra_body={'thinking':{'type':'disabled'}})
        return super().request_options()

original_pipeline=base.run_pipeline
def compact_pipeline(state,factory):
    def wrapped(name,current):
        client=factory(name,current);client.state=deepcopy(current);return client
    return original_pipeline(state,wrapped)

original_prepare=base.prepare
def prepare():
    p=original_prepare()
    settings=dict(risk_input='bounded marked source excerpts; trader plan; unique prior risk views',
        risk_output_tokens=1200,risk_thinking='disabled',risk_instructions=RISK_RULES,
        limitation='Risk input compression and disabled risk thinking may change decisions; this is not a sizing-only ablation.')
    path=OUT/'compact_risk_protocol.json'
    if path.exists():assert base.util.read(path)==settings
    base.util.save(path,settings)
    return p

def configure():
    base.OUT=OUT;base.StageClient=CompactStageClient;base.run_pipeline=compact_pipeline;base.prepare=prepare

if __name__=='__main__':
    configure();base.main()
