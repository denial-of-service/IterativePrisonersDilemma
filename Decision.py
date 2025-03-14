from enum import Enum


class Decision(Enum):
    Defect = -1
    Cooperate = 1


def opposite(decision: Decision) -> Decision:
    match decision:
        case Decision.Defect:
            return Decision.Cooperate
        case _:
            return Decision.Defect
