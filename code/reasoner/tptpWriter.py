from reasoner.formulas import Atomic, Negation, Disjunction, Belief
import os

def listToPrompt(formulaList):
    prompt = ""
    for i, formula in enumerate(formulaList):
        prompt = prompt + writeFullFormula("fo" + str(i), formula) + "\n"
    prompt = addPrelude(prompt)
    # print(prompt)
    return prompt

def writeFullFormula(formulaName, formula):
    """Writes the full corresponding TPTP formula, with header and footer."""
    # formulaName is required because TPTP wants each formula to have a unic name.
    return "fof(" + formulaName + ",axiom," + writeRecuFormula(formula) + ")."

def writeRecuFormula(formula):
    """Writes the formula localy in a way suitable for recusrive calls."""
    ftype = formula.getType()
    if ftype == 1:
        return writeRecuAtomic(formula)
    elif ftype == 2:
        return writeRecuNegation(formula)
    elif ftype == 3:
        return writeRecuDisjunction(formula)
    elif ftype == 4:
        return writeRecuBelief(formula)
    elif ftype == 5:
        return writeRecuConjunction(formula)
    else:
        # print("Error while generating TPTP syntax. Formula has none of the possible types.")
        assert(False)

def writeRecuAtomic(formula):
    return formula.getName()

def writeRecuNegation(formula):
    return "~(" + writeRecuFormula(formula.getChild()) + ")"

def writeRecuDisjunction(formula):
    chil = formula.getChildren()
    f1, f2 = chil[0], chil[1]
    return "(" + writeRecuFormula(f1) + " | " + writeRecuFormula(f2) + ")"

def writeRecuBelief(formula):
    return "ist(" + formula.getBeliever().getName() + "," + writeQuoteFormula(formula.getBelief()) + ")"

def writeRecuConjunction(formula):
    chil = formula.getChildren()
    f1, f2 = chil[0], chil[1]
    return "(" + writeRecuFormula(f1) + " & " + writeRecuFormula(f2) + ")"

def writeQuoteFormula(formula):
    """Writes the formula localy in a way suitable for recusrive calls."""
    ftype = formula.getType()
    if ftype == 1:
        return writeQuoteAtomic(formula)
    elif ftype == 2:
        return writeQuoteNegation(formula)
    elif ftype == 3:
        return writeQuoteDisjunction(formula)
    elif ftype == 4:
        return writeQuoteBelief(formula)
    elif ftype == 5:
        return writeQuoteConjunction(formula)
    else:
        # print("Error while generating TPTP syntax. Formula has none of the possible types.")
        assert(False)

def writeQuoteAtomic(formula):
    return "quote" + formula.getName()

def writeQuoteNegation(formula):
    return "quoteNeg(" + writeQuoteFormula(formula.getChild()) + ")"

def writeQuoteDisjunction(formula):
    chil = formula.getChildren()
    f1, f2 = chil[0], chil[1]
    return "quoteDisj(" + writeQuoteFormula(f1) + "," + writeQuoteFormula(f2) + ")"

def writeQuoteBelief(formula):
    return "quoteIst(" + "quote" + formula.getBeliever().getName() + "," + writeQuoteFormula(formula.getBelief()) + ")"

def writeQuoteConjunction(formula):
    chil = formula.getChildren()
    f1, f2 = chil[0], chil[1]
    return "quoteConj(" + writeQuoteFormula(f1) + "," + writeQuoteFormula(f2) + ")"

def addPrelude(text):
    with open(os.path.join("reasoner", "prelude.p")) as f:
        return text + f.read()