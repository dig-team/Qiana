from typing import List


class Formula:
    """Abstract type formula"""

    def getType(self) -> int:
        pass


class Atomic(Formula):
    def __init__(self, name: str, dbObject) -> None:
        newName = dbObject.legalizeName(name, type="ap")
        self.name = newName

    def getType(self) -> int:
        return 1

    def getName(self) -> str:
        return self.name


class Negation(Formula):
    def __init__(self, child: Formula) -> None:
        self.child = child

    def getType(self) -> int:
        return 2

    def getChild(self) -> Formula:
        return self.child


class Disjunction(Formula):
    def __init__(self, children: List[Formula]) -> None:
        if len(children) != 2:
            raise ValueError("Disjunction should have exactly 2 children.")
        self.children = children

    def getType(self) -> int:
        return 3

    def getChildren(self) -> List[Formula]:
        return self.children

class Conjunction(Formula):
    def __init__(self, children: List[Formula]) -> None:
        if len(children) != 2:
            raise ValueError("Conjunction should have exactly 2 children.")
        self.children = children

    def getType(self) -> int:
        return 5

    def getChildren(self) -> List[Formula]:
        return self.children

class Believer:
    """Anything that can occupy the left side of an "ist" statement. As of now this can only be a constant. Implemented in a way structuraly similar to Atomic"""

    def __init__(self, name: str, dbObject) -> None:
        newName = dbObject.legalizeName(name, type="bo")
        self.name = newName

    def getName(self) -> str:
        return self.name


class Belief(Formula):
    def __init__(self, believer: Believer, belief: Formula) -> None:
        self.believer = believer  # Should have type Believer
        self.belief = belief  # Should have type Formula

    def getType(self) -> int:
        return 4

    def getBeliever(self) -> Believer:
        return self.believer

    def getBelief(self) -> Formula:
        return self.belief
