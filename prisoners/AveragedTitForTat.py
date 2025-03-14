from Decision import Decision
from Prisoner import Prisoner


class AveragedTitForTat(Prisoner):
    is_first_round: bool = True
    opponent_cooperation_to_defection_delta: int = 0

    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        if self.is_first_round:
            self.is_first_round = False
        else:
            if opponents_previous_decision == Decision.Cooperate:
                self.opponent_cooperation_to_defection_delta += 1
            else:
                self.opponent_cooperation_to_defection_delta -= 1
        if self.opponent_cooperation_to_defection_delta >= 0:
            return Decision.Cooperate
        return Decision.Defect
