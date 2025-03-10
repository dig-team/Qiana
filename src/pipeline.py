import os

from reasoner import callSolver
from qianaExtension import Signature, getAllSchemesInstances
from htmlGeneration import getHtmlFromSteps, getHtmlNoContradiction
from dotGeneration import getDotFromSteps


class Pipeline:
    qianaClosure : str | None
    htmlTree : str | None

    def __init__(self) -> None:
        self.qianaClosure = None
        self.htmlTree = None

    def computeQianaClosure(self, input: str, quotedVariableNumber: int | None = 5) -> None:
        """
        Compute the qiana closure of the input and store it in self.qianaClosure

        @param input: str - the tptp representation of a set of formulas
        @param QuotedVariableNumber: int | None - the number of quoted variables to use in the qiana closure, default is 5. This argument should ideally always be specified when calling for the CLI as otherwise the value stored in Settings will be used.
        """
        with open("qianaExtension/qianaAxio.schemes", "r") as f:
            schemeLines = f.readlines()
        if not quotedVariableNumber:
            from gui import Settings
            quotedVariableNumber = Settings.getQuotedVarsNumber()
        signature = Signature(nbrQuotedVars=quotedVariableNumber)
        signature.extendFromTptpFormulas(input)
        # self.qianaClosure : str = os.linesep.join(qianaClosure(input, variableNumber))
        self.qianaClosure = input + os.linesep + os.linesep.join(getAllSchemesInstances(schemeLines, signature))

    def computeProofTree(self, timeout : int = 5) -> None:
        """
        Run the solver on the already computed qiana closure and stores the html representation of the proof tree in self.htmlTree
        This is for use in the CLI therefore requires the timeout value as an argument

        @param timeout: int - the timeout value for the solver, default is 5 seconds
        """
        self.foundContradiction, self.reasoningSteps, self.vampireOutput = callSolver(self.qianaClosure, timeout)
        if self.foundContradiction:
            self.htmlTree = getHtmlFromSteps(self.reasoningSteps)
        else:
            self.htmlTree = getHtmlNoContradiction(self.vampireOutput)

    def runCompute(self, input: str) -> None:
        """
        Takes as input the tptpt representation of a set of formulas and returns the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input. This is for use in the GUI and therefore uses the timeout value from the settings.
        @param input: str - the tptp representation of a set of formulas (not necessarily closed under qiana)
        @return: str - the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input
        """
        self.computeQianaClosure(input)
        from gui import Settings
        timeout = Settings.getTimeOutValue()
        self.foundContradiction, self.reasoningSteps, self.vampireOutput = callSolver(self.qianaClosure, timeout)
        if self.foundContradiction:
            self.htmlTree = getHtmlFromSteps(self.reasoningSteps)
        else:
            self.htmlTree = getHtmlNoContradiction(self.vampireOutput)

    def getHtmlTree(self) -> str:
        return self.htmlTree
    
    def getQianaClosure(self) -> str:
        return self.qianaClosure
    
    def getGraphDot(self) -> str:
        return getDotFromSteps(self.reasoningSteps)
    

