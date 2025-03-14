from Decision import Decision
from Prisoner import Prisoner


class InverseEnvy(Prisoner):
    wins_delta_to_opponent: int = 0

    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        if my_previous_decision == Decision.Cooperate:
            if opponents_previous_decision == Decision.Defect:
                self.wins_delta_to_opponent -= 1
        elif opponents_previous_decision == Decision.Cooperate:
            self.wins_delta_to_opponent += 1
        # Defect as long as we have won at least as much as our opponent.
        if self.wins_delta_to_opponent >= 0:
            return Decision.Defect
        return Decision.Cooperate
