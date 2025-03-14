from Decision import Decision
from Prisoner import Prisoner


class Jesus(Prisoner):

    # Always cooperates.
    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        return Decision.Cooperate
