"""Numeric final-manager output for the course project's fixed-weight backtest."""
from pydantic import Field, field_validator
from tradingagents.agents.schemas import PortfolioDecision


class BinaryDecision(PortfolioDecision):
    target_weight: float = Field(strict=True, ge=0, le=1, allow_inf_nan=False)

    @field_validator("target_weight")
    @classmethod
    def check_target(cls, weight):
        if weight not in (0., 1.):
            raise ValueError("Choose a target of 0 or 1")
        return weight


def manager_factory(variant, previous_weight):
    from tradingagents.agents.managers.portfolio_manager import create_portfolio_manager

    if variant == "position":
        from agents_position.decision import FractionalDecision, TARGET_RULE
        schema, rule = FractionalDecision, TARGET_RULE
    elif variant == "short":
        from agents_short.decision import ShortDecision, TARGET_RULE
        schema, rule = ShortDecision, TARGET_RULE
    else:
        schema, rule = BinaryDecision, "Choose 0 for cash or 1 for full long."
    repeat = ("A Hold rating must repeat the prior target." if variant != "short"
              else "Repeat the prior target if appropriate; a negative target still requires a short thesis.")
    instruction = (
        f"\nAlso output target_weight as a number for next-session open. {rule} "
        f"The previous target is {previous_weight:g}. {repeat} "
        "Turnover is measured by the absolute change from that target. "
        "The number, not the narrative rating, controls the backtest.\n"
    )

    def make(llm):
        manager = create_portfolio_manager(llm, decision_schema=schema, target_instruction=instruction)

        def decide(state):
            result = manager(state)
            if (variant != "short" and result["final_rating"] == "Hold"
                    and result["target_weight"] != previous_weight):
                raise ValueError("Hold must repeat the previous numeric weight")
            return result

        return decide

    return make
