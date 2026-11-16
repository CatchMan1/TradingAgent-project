"""Independent research-debate switch; no other optimization is enabled."""
from dataclasses import dataclass


@dataclass(frozen=True)
class DebateOptions:
    enabled: bool = True
    rounds: int = 3

    def __post_init__(self):
        if not isinstance(self.enabled, bool):
            raise ValueError("enabled must be a boolean")
        if type(self.rounds) is not int or self.rounds < 1:
            raise ValueError("debate rounds must be a positive integer")

    @property
    def effective_rounds(self):
        return self.rounds if self.enabled else 1

    def settings(self):
        return dict(module="research_debate", enabled=self.enabled,
                    requested_rounds=self.rounds, effective_rounds=self.effective_rounds,
                    expected_research_turns=2*self.effective_rounds,
                    risk_rounds=1, fractional_position=False, short_selling=False,
                    sentiment_module=False)

    def apply(self, config):
        # Explicit isolation overrides legacy environment variables for these
        # two loops. All data, model, analyst and execution settings stay intact.
        result = dict(config)
        result.update(max_debate_rounds=self.effective_rounds, max_risk_discuss_rounds=1)
        result["max_recur_limit"] = max(config.get("max_recur_limit",100),
                                        50+2*self.effective_rounds)
        return result
