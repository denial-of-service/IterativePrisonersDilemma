from Decision import Decision
from Prisoner import Prisoner


class Vengeance(Prisoner):
    opponent_always_cooperates: bool = True

    # Cooperates until his opponent defects, the defects for the remainder of the match.
    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        if opponents_previous_decision == Decision.Defect:
            self.opponent_always_cooperates = False
        if self.opponent_always_cooperates:
            return Decision.Cooperate
        else:
            return Decision.Defect
