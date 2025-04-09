import random

from Decision import Decision
from Prisoner import Prisoner


class EvilTitForTat(Prisoner):

    # Plays Tit for Tat but occasionally defects against a cooperating opponent.
    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        if opponents_previous_decision == Decision.Defect:
            return Decision.Defect
        else:
            # 15% probability to defect on a cooperative opponent
            if random.random() < 0.15:
                return Decision.Defect
            else:
                return Decision.Cooperate