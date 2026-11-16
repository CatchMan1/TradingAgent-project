"""Opt-in continuous sizing extension around the ORIGINAL downstream agents.

Original factories and role prompts remain untouched. The only added mandate
specifies the authoritative account, continuous sizing and execution semantics.
"""
import json
import math
from typing import Literal
from pydantic import Field, field_validator, model_validator
from tradingagents.agents.schemas import PortfolioDecision
from tradingagents.agents.managers.research_manager import create_research_manager
from tradingagents.agents.trader.trader import create_trader
from tradingagents.agents.risk_mgmt.aggressive_debator import create_aggressive_debator
from tradingagents.agents.risk_mgmt.conservative_debator import create_conservative_debator
from tradingagents.agents.risk_mgmt.neutral_debator import create_neutral_debator
from tradingagents.agents.managers.portfolio_manager import create_portfolio_manager

STAGES=(('research',create_research_manager),('trader',create_trader),
        ('aggressive',create_aggressive_debator),('conservative',create_conservative_debator),
        ('neutral',create_neutral_debator),('portfolio',create_portfolio_manager))
SIZING_RULES='''Continuous-position module (the original role and evidence-weighing responsibilities remain unchanged):
The account below is authoritative. Size against TOTAL account equity in this single-stock/cash simulation, not a fraction of an unspecified standard allocation or a confidence score. Consider current holdings, average cost, cash, realized/unrealized P&L and the marginal add/cut; cost basis alone is not a reason to wait for break-even. Research and Trader may recommend a numeric target; the three risk analysts review it and the Portfolio Manager alone authorizes the final executable target.
Daily sizing requirements:
1. Reassess a reasonable TOTAL target exposure from today's supplied evidence before choosing a trade. Yesterday's small holding is an execution starting point, not a sizing anchor: do not mechanically apply another percentage discount to it. Current holdings, cost basis and fees inform the marginal transaction, but do not replace an independent assessment of the appropriate total exposure. Reassessment does not require a daily trade.
2. Explicitly weigh both downside loss from holding stock and the opportunity cost of holding cash if the stock rises. Discuss plausible upside/downside scenarios using only available evidence; do not invent calibrated probabilities or precise expected returns. Neither risk avoidance nor cash opportunity cost automatically overrides the other.
3. Explain why the chosen total exposure is appropriate, and compare it with a concrete higher and a concrete lower allocation (where feasible within [0,1]). Identify the evidence and trade-offs that favor the chosen allocation. At 0 or 1 explain the boundary choice and the feasible alternative. When keeping shares, state the current signal-day percentage being retained and why its exposure remains reasonable; target_weight_now must still be null.
4. If retaining a very small allocation, explain its practical economic purpose, its potential contribution to total-account return/loss, and why that purpose is preferable to zero exposure after fees. An unspecified 'observation position' is not sufficient: observing evidence does not require holding stock. Explicit liquidation to target_weight_now=0 is allowed when no useful exposure is justified. Do not impose a minimum holding or increase exposure merely to avoid a small percentage.
Research and Trader must address these sizing trade-offs in their existing rationale/reasoning and sizing fields. Risk analysts must challenge both excessive stock exposure and unjustified idle cash, including any repeated proportional trimming without a fresh total-target justification. The final Portfolio Manager must include the chosen/retained total percentage, the higher/lower comparison, cash opportunity cost, and any tiny-position justification in executive_summary/investment_thesis, resolving disagreement before authorizing execution.
Targets may be any finite number from 0 to 1. No forced minimum, bullish bias, shorting, leverage or new information collection. Other optimization modules are OFF. Cash earns no interest. Actual trades occur at the next session open with 10-bps fees; that open is unknown. Stops/limits and conditional future adds are narrative conditions only, not implemented orders. Separate a target to execute now from those conditions. For no transaction use execution_action=keep_shares and target_weight_now=null; this preserves shares rather than rebalancing daily. For an actual next-open adjustment use execution_action=rebalance and target_weight_now in [0,1]. Keep the original rating and explanation as well. A Hold rating requires keep_shares; other ratings may express direction, but the executable target determines the actual trade. Do not treat a suggested partial trim as full liquidation. Use only dated supplied evidence; no future outcomes are provided.
'''

class SizedPortfolioDecision(PortfolioDecision):
    execution_action: Literal['keep_shares','rebalance']
    target_weight_now: float | None = Field(description='Final unconditional next-open target as fraction of total equity, 0 to 1; null only for keep_shares.')
    @field_validator('target_weight_now',mode='before')
    @classmethod
    def strict_target(cls,v):
        if v is not None and (isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or not 0<=v<=1):
            raise ValueError('Invalid continuous target')
        return v
    @model_validator(mode='after')
    def consistency(self):
        if (self.execution_action=='keep_shares') != (self.target_weight_now is None):raise ValueError('Action/target mismatch')
        if self.rating.value=='Hold' and self.execution_action!='keep_shares':raise ValueError('Hold must preserve shares')
        return self

def run_pipeline(state, llm_for_stage):
    """Execute original nodes in original order; clients add account/format only."""
    state=dict(state)
    for name,factory in STAGES:
        llm=llm_for_stage(name,state)
        update=factory(llm)(state)
        state.update(update)
        if name=='portfolio':
            result=llm.final_sized_decision
            if not isinstance(result,SizedPortfolioDecision):raise ValueError('Missing valid final sized decision')
            state['final_position']=result.model_dump(mode='json')
        if hasattr(llm,'save_stage'):llm.save_stage(update)
    assert state['risk_debate_state']['count']==3
    return state

def portfolio_block(account):
    return 'Authoritative simulated account (signal-day close):\n'+json.dumps(account,ensure_ascii=False)
