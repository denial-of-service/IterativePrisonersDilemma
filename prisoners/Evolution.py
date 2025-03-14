import random

from Decision import Decision, opposite
from Prisoner import Prisoner


class Evolution(Prisoner):
    points: int = 0
    round_count_using_strategy: int = 0

    def decision(self, my_previous_decision: Decision, opponents_previous_decision: Decision) -> Decision:
        self.round_count_using_strategy += 1
        if my_previous_decision == Decision.Cooperate:
            if opponents_previous_decision == Decision.Cooperate:
                self.points += 3
        else:
            if opponents_previous_decision == Decision.Cooperate:
                self.points += 5
            else:
                self.points += 1

        # The fewer points we earn, the higher the likelihood we change our strategy.
        if random.random() * 5 >= self.points / self.round_count_using_strategy:
            self.round_count_using_strategy = 0
            self.points = 0
            return opposite(my_previous_decision)
        return my_previous_decision
