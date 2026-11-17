"""Long-only fractional sizing decision."""
from pydantic import Field
from tradingagents.agents.schemas import PortfolioDecision


class FractionalDecision(PortfolioDecision):
    target_weight: float = Field(strict=True, ge=0, le=1, allow_inf_nan=False)


TARGET_RULE = (
    "Choose any total long exposure from 0 to 1. Weigh downside risk against the "
    "opportunity cost of cash, and compare with higher and lower exposures. "
    "Size against total equity, not yesterday's allocation."
)
