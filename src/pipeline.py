
import subprocess
import os

from reasoner import callSolver
from qianaExtension import qianaClosure
from htmlGeneration import getHtmlFromSteps, getHtmlNoContradiction

def basicTPTPtoHtml(input: str, variableNumber = None) -> str:
    """
    Takes as input the tptpt representation of a set of formulas and returns the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input.
    @param input: str - the tptp representation of a set of formulas (not necessarily closed under qiana)
    @return: str - the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input
    """
    variableNumber = 3 if variableNumber is None else variableNumber
    closureOfInput : str = os.linesep.join(qianaClosure(input, variableNumber))
    foundContradiction, reasoningSteps, vampireOutput = callSolver(closureOfInput)
    if foundContradiction:
        return getHtmlFromSteps(reasoningSteps)
    else:
        return getHtmlNoContradiction(vampireOutput)