"""Discrete long, cash, or short decision."""
from pydantic import Field, field_validator
from tradingagents.agents.schemas import PortfolioDecision


class ShortDecision(PortfolioDecision):
    target_weight: float = Field(strict=True, ge=-1, le=1, allow_inf_nan=False)

    @field_validator("target_weight")
    @classmethod
    def check_target(cls, weight):
        if weight not in (-1., 0., 1.):
            raise ValueError("Choose a target of -1, 0 or 1")
        return weight


TARGET_RULE = (
    "Choose -1 for full short, 0 for cash, or 1 for full long. Require affirmative "
    "downside evidence for a short and weigh upside/squeeze risk. A weak long thesis "
    "alone is insufficient. Explicitly reconsider any short each day."
)
