from Decision import Decision


class Prisoner:

    # Receives his and his opponent's decision during the previous round.
    # Uses a defined strategy to make a decision for the current round.
    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        pass
