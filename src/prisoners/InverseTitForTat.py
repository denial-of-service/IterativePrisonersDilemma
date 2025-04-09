from Decision import opposite, Decision
from Prisoner import Prisoner


class InverseTitForTat(Prisoner):

    # Does the opposite of his opponent in the previous round.
    def decision(self, my_previous_decision: Decision,
                 opponents_previous_decision: Decision) -> Decision:
        return opposite(opponents_previous_decision)
