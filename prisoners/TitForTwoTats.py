from Decision import Decision
from Prisoner import Prisoner


class TitForTwoTats(Prisoner):
    opponents_decision_two_rounds_ago: Decision = Decision.Cooperate

    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        decision: Decision = Decision.Cooperate
        # Opponent defected in the previous two rounds
        if opponents_previous_decision == Decision.Defect and self.opponents_decision_two_rounds_ago == Decision.Defect:
            decision = Decision.Defect
        self.opponents_decision_two_rounds_ago = opponents_previous_decision
        return decision
