from Decision import opposite, Decision

from Prisoner import Prisoner


class Alternate(Prisoner):

    # Changes his decision every round.
    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        return opposite(my_previous_decision)
