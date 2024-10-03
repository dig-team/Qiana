
import subprocess
import os

from reasoner import callSolver
from qianaExtension import qianaClosure
from htmlGeneration import getHtml

def basicTPTPtoHtml(input: str, variableNumber = None) -> str:
    """
    Takes as input the tptpt representation of a set of formulas and returns the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input.
    @param input: str - the tptp representation of a set of formulas (not necessarily closed under qiana)
    @return: str - the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input
    """
    variableNumber = 3 if variableNumber is None else variableNumber
    closureOfInput : str = os.linesep.join(qianaClosure(input, variableNumber))
    foundContradiction, reasoningSteps = callSolver(closureOfInput)
    return getHtml(reasoningSteps)

if __name__ == "__main__":
    # path = sys.argv[1]
    with open("/home/sipirate/Documents/Doc_Divers/NoRDF/Qiana/Qiana_dig-team/example/input-example.p", "r") as f:
        prompt = f.read()
    htmlOutput = basicTPTPtoHtml(prompt)
    with open("/home/sipirate/Documents/Doc_Divers/NoRDF/Qiana/Qiana_dig-team/example/output-example.html", "w") as f:
        f.write(htmlOutput)
