import os

from reasoner import callSolver
from qianaExtension import qianaClosure
from htmlGeneration import getHtmlFromSteps, getHtmlNoContradiction
from gui import Settings

class Pipeline:
    qianaClosure : str | None
    htmlTree : str | None

    def __init__(self):
        self.variableNumber = None
        self.qianaClosure = None
        self.htmlTree = None

    def computeQianaClosure(self, input: str) -> None:
        variableNumber = Settings.getQuotedVarsNumber()
        self.qianaClosure : str = os.linesep.join(qianaClosure(input, variableNumber))

    def runCompute(self, input: str) -> None:
        """
        Takes as input the tptpt representation of a set of formulas and returns the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input.
        @param input: str - the tptp representation of a set of formulas (not necessarily closed under qiana)
        @return: str - the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input
        """
        self.computeQianaClosure(input)
        timeout = Settings.getTimeOutValue()
        foundContradiction, reasoningSteps, vampireOutput = callSolver(self.qianaClosure, timeout)
        if foundContradiction:
            self.htmlTree = getHtmlFromSteps(reasoningSteps)
        else:
            self.htmlTree = getHtmlNoContradiction(vampireOutput)

    def getHtmlTree(self) -> str:
        return self.htmlTree
    
    def getQianaClosure(self) -> str:
        return self.qianaClosure

