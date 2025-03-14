import random

from Decision import Decision
from Prisoner import Prisoner


class ForgivingTitForTat(Prisoner):

    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        if opponents_previous_decision == Decision.Cooperate:
            return Decision.Cooperate
        else:
            # 15% probability to not retaliate against a defection
            if random.random() < 0.15:
                return Decision.Cooperate
            else:
                return Decision.Defect
