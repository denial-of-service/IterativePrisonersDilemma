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

matches_count: int = 50
rounds_count: int = 500
noise_probability: float = 0.05


def main() -> None:
    prisoner_classes: list[Prisoner] = [Alternate, AveragedTitForTat, Bully, Envy, EvilTitForTat, Evolution,
                                        ForgivingTitForTat, InverseEnvy, InverseTitForTat, Jesus, Random, Satan,
                                        TitForTat, TitForTwoTats, Vengeance]
    prisoner_total_points: dict[Prisoner, int] = dict.fromkeys(prisoner_classes, 0)

    # Each prisoner plays against himself and everyone else
    for class_a, class_b in itertools.combinations_with_replacement(prisoner_classes, 2):
        # Play matches_count matches against each opponent
        for i in range(matches_count):
            prisoner_a: Prisoner.Prisoner = class_a()
            prisoner_b: Prisoner.Prisoner = class_b()
            previous_decision_a: Decision = Decision.Cooperate
            previous_decision_b: Decision = Decision.Cooperate
            # Play rounds_count rounds per match
            for j in range(rounds_count):
                noisy_previous_decision_a: Decision = previous_decision_a
                if random.random() < noise_probability:
                    noisy_previous_decision_a = opposite(previous_decision_a)
                noisy_previous_decision_b: Decision = previous_decision_b
                if random.random() < noise_probability:
                    noisy_previous_decision_b = opposite(previous_decision_b)

                previous_decision_a = prisoner_a.decision(previous_decision_a, noisy_previous_decision_b)
                previous_decision_b = prisoner_b.decision(previous_decision_b, noisy_previous_decision_a)

                if previous_decision_a == Decision.Cooperate:
                    if previous_decision_b == Decision.Cooperate:
                        prisoner_total_points[class_a] += 3
                        prisoner_total_points[class_b] += 3
                    else:
                        prisoner_total_points[class_b] += 5
                else:
                    if previous_decision_b == Decision.Cooperate:
                        prisoner_total_points[class_a] += 5
                    else:
                        prisoner_total_points[class_a] += 1
                        prisoner_total_points[class_b] += 1

    prisoner_sorted_points: list[tuple[Prisoner, int]] = sorted(prisoner_total_points.items(), key=lambda x: x[1],
                                                                reverse=True)
    for prisoner_class, points in prisoner_sorted_points:
        average_points_per_round: float = round((points / (len(prisoner_classes) * matches_count * rounds_count)), 2)
        print(f'{prisoner_class.__name__}: total: {points}, average: {average_points_per_round}')


if __name__ == '__main__':
    main()
