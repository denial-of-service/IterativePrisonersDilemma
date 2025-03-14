import random

from Decision import Decision
from Prisoner import Prisoner


class Random(Prisoner):
    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        return random.choice([Decision.Cooperate, Decision.Defect])
