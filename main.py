import itertools
import random

from Decision import opposite, Decision
import Prisoner
from prisoners.Alternate import Alternate
from prisoners.AveragedTitForTat import AveragedTitForTat
from prisoners.Bully import Bully
from prisoners.Envy import Envy
from prisoners.EvilTitForTat import EvilTitForTat
from prisoners.Evolution import Evolution
from prisoners.ForgivingTitForTat import ForgivingTitForTat
from prisoners.InverseEnvy import InverseEnvy
from prisoners.InverseTitForTat import InverseTitForTat
from prisoners.Random import Random
from prisoners.Jesus import Jesus
from prisoners.Satan import Satan
from prisoners.TitForTat import TitForTat
from prisoners.TitForTwoTats import TitForTwoTats
from prisoners.Vengeance import Vengeance

matches_per_pair_of_opponents: int = 50
rounds_per_match: int = 500
misunderstanding_probability: float = 0.05


def main() -> None:
    prisoner_classes: list[Prisoner] = [Alternate, AveragedTitForTat, Bully, Envy, EvilTitForTat, Evolution,
                                        ForgivingTitForTat, InverseEnvy, InverseTitForTat, Jesus, Random, Satan,
                                        TitForTat, TitForTwoTats, Vengeance]
    # Total points earned by each prisoner.
    prisoners_to_points: dict[Prisoner, int] = dict.fromkeys(prisoner_classes, 0)

    # Each prisoner plays against himself and everyone else.
    for class_a, class_b in itertools.combinations_with_replacement(prisoner_classes, 2):
        # Play 'matches_per_pair_of_opponents' matches against each opponent.
        for i in range(matches_per_pair_of_opponents):
            # The two participants in the match.
            prisoner_a: Prisoner.Prisoner = class_a()
            prisoner_b: Prisoner.Prisoner = class_b()
            # Cooperation is the default decision.
            decision_a: Decision = Decision.Cooperate
            decision_b: Decision = Decision.Cooperate
            # Play 'rounds_per_match' rounds per match.
            for j in range(rounds_per_match):
                perceived_decision_a: Decision = decision_a
                # There is a 'misunderstanding_probability' probability that a prisoner misunderstands his opponents choice.
                if random.random() < misunderstanding_probability:
                    # Prisoner b has misunderstood Prisoner a's decision
                    perceived_decision_a = opposite(decision_a)
                perceived_decision_b: Decision = decision_b
                # There is a 'misunderstanding_probability' probability that a prisoner misunderstands his opponents choice.
                if random.random() < misunderstanding_probability:
                    # Prisoner a has misunderstood Prisoner b's decision
                    perceived_decision_b = opposite(decision_b)
                # The Prisoners are told about their opponents choice int the previous round and make their decision.
                decision_a = prisoner_a.decision(decision_a, perceived_decision_b)
                decision_b = prisoner_b.decision(decision_b, perceived_decision_a)
                # Evaluate how many points each prisoner earned this round and add them to their respective total.
                if decision_a == Decision.Cooperate:
                    if decision_b == Decision.Cooperate:
                        prisoners_to_points[class_a] += 3
                        prisoners_to_points[class_b] += 3
                    else:
                        prisoners_to_points[class_b] += 5
                else:
                    if decision_b == Decision.Cooperate:
                        prisoners_to_points[class_a] += 5
                    else:
                        prisoners_to_points[class_a] += 1
                        prisoners_to_points[class_b] += 1

    # Sort prisoners by points in descending order.
    prisoner_sorted_points: list[tuple[Prisoner, int]] = sorted(
        prisoners_to_points.items(),
        key=lambda pair: pair[1],
        reverse=True
    )
    # Print the results of the competition, rank prisoners from best to worst.
    for prisoner_class, points in prisoner_sorted_points:
        average_points_per_round: float = round(
            (points / (len(prisoner_classes) * matches_per_pair_of_opponents * rounds_per_match)), 2)
        print(f'{prisoner_class.__name__} | total: {points} | average: {average_points_per_round}')


if __name__ == '__main__':
    main()
