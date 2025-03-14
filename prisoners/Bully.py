from Decision import Decision, opposite
from Prisoner import Prisoner


class Bully(Prisoner):
    opponent_has_defected: bool = False

    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        if self.opponent_has_defected:
            # If the opponent is not a pushover, use the Tit for Tat strategy
            return opponents_previous_decision
        else:
            if opponents_previous_decision == Decision.Cooperate:
                # Continue defecting every other move
                return opposite(my_previous_decision)
            else:
                # Don't defect after the first retaliatory defection of our opponent
                self.opponent_has_defected = True
                return Decision.Cooperate