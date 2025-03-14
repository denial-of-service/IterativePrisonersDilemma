from Decision import Decision
from Prisoner import Prisoner


class TitForTat(Prisoner):

    # Uses his opponents decision in the previous round.
    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        return opponents_previous_decision
