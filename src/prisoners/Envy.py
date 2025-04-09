from Decision import Decision
from Prisoner import Prisoner


class Envy(Prisoner):
    wins_to_losses_delta: int = 0

    # Defects as long as he has fewer points than his opponent.
    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        if my_previous_decision == Decision.Cooperate:
            if opponents_previous_decision == Decision.Defect:
                self.wins_to_losses_delta -= 1
        elif opponents_previous_decision == Decision.Cooperate:
            self.wins_to_losses_delta += 1
        # Cooperate as long as our opponent hasn't won more often than us.
        if self.wins_to_losses_delta >= 0:
            return Decision.Cooperate
        return Decision.Defect
