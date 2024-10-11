"""  Qiana FormulaParser

This module provides methods to parse a TPTP formula into an internal representation
"""

from __future__ import annotations

from typing import List

from qianaExtension.Formulas import Formula, Atom, Forall, Formula, Not, Term, Variable

###########################################################################################
#                       Parsing terms                                                     #
###########################################################################################

# Maps Latex and TPTP operators to the ones we use in the code.
niceOperators = {
    "∨": Formula.OR,
    "∧": Formula.AND,
    "→": Formula.IMPLIES,
    "↔": Formula.EQV,
    "¬": Formula.NOT,
    "~": Formula.NOT,
    "&": Formula.AND,
}


def readItem(s: str, pos: list[int]) -> str:
    """Parses the next item out of the string, updates the position"""
    while pos[0] < len(s) and s[pos[0]].isspace():
        pos[0] += 1
    if pos[0] >= len(s):
        return None
    if s[pos[0]] == "%":
        while pos[0] < len(s) and s[pos[0]] != "\n":
            pos[0] += 1
        return readItem(s, pos)
    if Formula.isIdentifier(s[pos[0]]):
        start = pos[0]
        while pos[0] < len(s) and Formula.isIdentifier(s[pos[0]]):
            pos[0] += 1
        return s[start : pos[0]]
    pos[0] += 1
    return s[pos[0] - 1]


def readGivenItem(s: str, pos: list[int], item: str):
    """Parses the next item out of the string, updates the position, checks if the item is as given"""
    read = readItem(s, pos)
    if item != read:
        raise Exception(
            f"Expected {item}, not {read}\nat position {s[:pos[0]]}***{s[pos[0]:]}"
        )


def readTerm(s: str, pos: list[int]) -> Term:
    """Parses the next term out of the string, updates the position"""
    predicate = readItem(s, pos)
    Formula.checkIdentifier(predicate)
    if predicate == "ist":
        readGivenItem(s, pos, "(")
        context = readTerm(s, pos)
        readGivenItem(s, pos, ",")
        formula = readFormula(s, pos)
        readGivenItem(s, pos, ")")
        return Term("ist", context, formula.quote())
    posBefore = pos[0]
    nextItem = readItem(s, pos)
    args = []
    if nextItem == "(":
        while True:
            posBefore = pos[0]
            arg = readItem(s, pos)
            if arg == ")":
                break
            if arg == ",":
                continue
            pos[0] = posBefore
            args.append(readTerm(s, pos))
    else:
        pos[0] = posBefore
        if Formula.isVariable(predicate):
            return Variable(predicate)
    return Term(predicate, *args)


###########################################################################################
#                       Parsing formulas                                                  #
###########################################################################################


def readFormula(s: str, pos: list[int]) -> Formula:
    """Parses the string into a formula"""
    posBefore = pos[0]
    item = readItem(s, pos)
    if not item:
        return None
    if item == "∀":
        variables = []
        while True:
            item = readItem(s, pos)
            if not item:
                raise Exception("Expected '.', not end of input")
            if item == ".":
                break
            if item == ",":
                continue
            variables.append(item)
        return Forall(variables, readFormula(s, pos))
    if item == "!":
        readGivenItem(s, pos, "[")
        variables = []
        while True:
            item = readItem(s, pos)
            if not item:
                raise Exception("Expected '.', not end of input")
            if item == "]":
                break
            if item == ",":
                continue
            variables.append(item)
        readGivenItem(s, pos, ":")
        return Forall(variables, readFormula(s, pos))
    if item == "¬" or item == "~":
        return Not(readFormula(s, pos))
    if item == "fof":
        readGivenItem(s, pos, "(")
        readItem(s, pos)
        readGivenItem(s, pos, ",")
        formulaType = readItem(s, pos)
        readGivenItem(s, pos, ",")
        formula = readFormula(s, pos)
        formula.setType(formulaType)
        readGivenItem(s, pos, ")")
        readGivenItem(s, pos, ".")
        return formula
    if item == "(":
        firstFormula = readFormula(s, pos)
        readGivenItem(s, pos, ")")
    else:
        pos[0] = posBefore
        firstTerm = readTerm(s, pos)
        firstFormula = Atom(firstTerm.function, *firstTerm.args)
    operator = readItem(s, pos)
    if operator is None:
        return firstFormula
    if operator == ")":
        pos[0] -= 1
        return firstFormula
    if operator == "=":
        readGivenItem(s, pos, ">")
        operator = "→"
        # Fall through
    if operator == "<":
        readGivenItem(s, pos, "=")
        readGivenItem(s, pos, ">")
        operator = "↔"
        # Fall through
    if operator not in niceOperators:
        raise Exception(f"Expected operator, not {operator}")
    secondFormula = readFormula(s, pos)
    return Formula(niceOperators[operator], firstFormula, secondFormula)


def parse(s: str) -> Formula:
    """Parses a string as a formula"""
    return readFormula(s, [0])

def readFormulasFromData(data: str) -> List[Formula]:
    """Reads the formulas from the file"""
    result = []
    pos = [0]
    while True:
        formula = readFormula(data, pos)
        if formula == None:
            break
        result.append(formula)
    print(f"    Found {len(result)} formulas")
    print("  done")
    return result


def readFormulasFromFile(fileName: str) -> List[Formula]:
    """Reads the formulas from the file"""
    print(f"  Reading formulas from {fileName}...")
    with open(fileName, "rt") as file:
        data = file.read()
    return readFormulasFromData(data)