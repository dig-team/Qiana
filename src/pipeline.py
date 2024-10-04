import subprocess
import os

from reasoner import callSolver
from qianaExtension import qianaClosure
from htmlGeneration import getHtmlFromSteps, getHtmlNoContradiction

class Pipeline:
    variableNumber : int | None
    qianaClosure : str | None
    htmlTree : str | None

    def __init__(self):
        self.variableNumber = None
        self.qianaClosure = None
        self.htmlTree = None

    def runCompute(self, input: str) -> None:
        """
        Takes as input the tptpt representation of a set of formulas and returns the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input.
        @param input: str - the tptp representation of a set of formulas (not necessarily closed under qiana)
        @return: str - the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input
        """
        variableNumber = 3 if self.variableNumber is None else self.variableNumber
        self.qianaClosure : str = os.linesep.join(qianaClosure(input, variableNumber))
        foundContradiction, reasoningSteps, vampireOutput = callSolver(self.qianaClosure)
        if foundContradiction:
            self.htmlTree = getHtmlFromSteps(reasoningSteps)
        else:
            self.htmlTree = getHtmlNoContradiction(vampireOutput)

    def setVariableNumber(self, number : str | None) -> None:
        if number is None: return
        try:
            number = number.strip()
            self.variableNumber = int(number)
        except ValueError:
            pass

    def getHtmlTree(self) -> str:
        return self.htmlTree
    
    def getQianaClosure(self) -> str:
        return self.qianaClosure

