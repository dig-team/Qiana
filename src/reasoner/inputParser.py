from typing import Dict, List
from reasoner.formulas import Atomic, Belief, Believer, Disjunction, Conjunction, Negation


def update(dbObj, input_json: Dict[str, List]) -> None:
    """Adds all formulas required in the database from json input"""
    # add NameLookup values to inputNameDict
    for name in input_json["AtoNameLookup"]:
        dbObj.inputNameDict.update(name)
    for name in input_json["BelieverNameLookup"]:
        dbObj.inputNameDict.update(name)
    # add Formulas to formulaList
    for raw_formula in input_json["FormulaList"]:
        dbObj.addFormula(parse_formula(dbObj, raw_formula))
    for raw_formula in input_json["BasicFormulaList"]:
        a = Atomic(raw_formula[1][0], dbObj)
        if not raw_formula[1][1]:
            a = Negation(a)
        b = Atomic(raw_formula[2][0], dbObj)
        if not raw_formula[2][1]:
            b = Negation(b)

        entailment = Disjunction([Negation(a), b])
        contradiction = Disjunction([Negation(a), Negation(b)])

        formula = None
        if raw_formula[3] == "entailment":
            # (P → Q) ↔ (¬P ∨ Q)
            formula = entailment
        elif raw_formula[3] == "contradiction":
            # (P → ¬Q) ↔ (¬P ∨ ¬Q)
            formula = contradiction
        else:
            continue # What followed is very weirdly powerful.
            # not an entailment and not a contradiction
            formula = Negation(
                Disjunction([Negation(entailment), Negation(contradiction)])
            )
        # if formula is a belief, we use quoted formulas for each believer
        if raw_formula[0]:
            for believer in raw_formula[0]:
                dbObj.addFormula(Belief(Believer(believer, dbObj), formula))
        else:
            dbObj.addFormula(formula)


def parse_formula(dbObj, json_formula):
    if "atomic" in json_formula:
        return Atomic(json_formula["atomic"], dbObj)
    elif "neg" in json_formula:
        child_formula = parse_formula(dbObj, json_formula["neg"])
        return Negation(child_formula)
    elif "or" in json_formula:
        children = [
            parse_formula(dbObj, child) for child in json_formula["or"]["children"]
        ]
        # we need to get the cumulative children by pairs if there are more than 2
        conjunctions = [Disjunction(children[:2])]
        if len(children) > 2:
            for i in range(2, len(children)):
                child = children[i]
                conjunctions.append(Disjunction([conjunctions[-1], child]))

        return conjunctions[-1]
    elif "and" in json_formula:
        children = [
            parse_formula(dbObj, child) for child in json_formula["and"]["children"]
        ]
        # we need to get the cumulative children by pairs if there are more than 2
        conjunctions = [Conjunction(children[:2])]
        if len(children) > 2:
            for i in range(2, len(children)):
                child = children[i]
                conjunctions.append(Conjunction([conjunctions[-1], child]))

        return conjunctions[-1]
    elif "imply" in json_formula:
        left = parse_formula(dbObj, json_formula["imply"]["left"])
        right = parse_formula(dbObj, json_formula["imply"]["right"])
        imply = lambda antecedent, consequent: Disjunction(
            [Negation(antecedent), consequent]
        )
        return imply(left, right)
    elif "ist" in json_formula:
        believer = Believer(json_formula["ist"]["believer"], dbObj)
        belief = parse_formula(dbObj, json_formula["ist"]["belief"])
        return Belief(believer, belief)
    else:
        raise ValueError("Invalid formula format")
