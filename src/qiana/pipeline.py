import os
from os.path import join, dirname

from qiana.reasoner import SolverCall
from qiana.qianaExtension import Signature, getAllSchemesInstances, applyMacros
from qiana.htmlGeneration import getHtmlFromSteps, getHtmlNoContradiction
from qiana.dotGeneration import getDotFromSteps
from qiana.extendsimplifiedsyntax import extend_simplified_syntax


class Pipeline:
    qianaClosure : str | None
    htmlTree : str | None

    def __init__(self) -> None:
        self.qianaClosure = None
        self.htmlTree = None

    def computeQianaClosure(self, input: str, quotedVariableNumber: int | None = 5, simplified_input : bool = False, expand_macros : bool = False) -> None:
        """
        Compute the qiana closure of the input and store it in self.qianaClosure

        @param input: str - the tptp representation of a set of formulas
        @param QuotedVariableNumber: int | None - the number of quoted variables to use in the qiana closure, default is 5. This argument should ideally always be specified when calling for the CLI as otherwise the value stored in Settings will be used.
        @param simplified_input: bool - if true the headers on formulas will be automatically added. 
        @param expand_macros: bool - if true the qiana specific macros will be expanded before computing the qiana closure
        """
        if simplified_input: input = extend_simplified_syntax(input)
        if expand_macros: input = applyMacros(input)

        path_to_schemes = join(dirname(__file__), "qianaExtension/qianaAxio.schemes")
        with open(path_to_schemes, "r") as f: schemeLines = f.readlines()
        if not quotedVariableNumber:
            from gui import Settings
            quotedVariableNumber = Settings.getQuotedVarsNumber()
        signature = Signature(nbrQuotedVars=quotedVariableNumber)
        signature.extendFromTptps(input)
        # self.qianaClosure : str = os.linesep.join(qianaClosure(input, variableNumber))
        self.qianaClosure = input + os.linesep + os.linesep.join(getAllSchemesInstances(schemeLines, signature))

    def runCompute_CLI(self, timeout : int = 5) -> None:
        """
        Run the solver on the already computed qiana closure and stores the html representation of the proof tree in self.htmlTree
        This is for use in the CLI therefore requires the timeout value as an argument

        @param timeout: int - the timeout value for the solver, default is 5 seconds
        """
        self._callSolver(timeout)

    def runCompute_GUI(self, input: str) -> None:
        """
        Takes as input the tptpt representation of a set of formulas and returns the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input. This is for use in the GUI and therefore uses the timeout value from the settings.
        @param input: str - the tptp representation of a set of formulas (not necessarily closed under qiana)
        @return: str - the html representation of the reasoning steps performed to find a contradiction on the qiana closure of input
        """
        self.computeQianaClosure(input)
        from qiana.gui import Settings
        timeout = Settings.getTimeOutValue()
        self._callSolver(timeout)

    def _callSolver(self, timeout: int) -> None:
        """
        Call the solver and store the result in self.reasoningSteps. Assumes the qiana closure has already been computed and stored in self.qianaClosure.
        @param timeout: int - the timeout value for the solver
        """
        if not self.qianaClosure: raise ValueError("Qiana closure has not been computed yet. Please call computeQianaClosure() before running the solver.")
        solverCall : SolverCall = SolverCall.callVampire(self.qianaClosure, timeout)
        self.foundContradiction = solverCall.simpleResult == "unsat"
        self.simpleResult = solverCall.simpleResult
        self.reasoningSteps = solverCall.reasoningSteps
        self.vampireOutput = solverCall.vampireOutput
        self.htmlTree = getHtmlFromSteps(self.reasoningSteps) if self.foundContradiction else getHtmlNoContradiction(self.vampireOutput)

    def contradiction(self) -> bool:
        return self.foundContradiction
    
    def unknownResult(self) -> bool:
        """
        Check if the solver returned an unknown result
        @return: bool - True if the solver returned an unknown result, False otherwise
        """
        return self.simpleResult == "unknown"
    
    def timeout(self) -> bool:
        """
        Check if the solver timed out
        @return: bool - True if the solver timed out, False otherwise
        """
        return self.simpleResult == "timeout"

    def getHtmlTree(self) -> str:
        return self.htmlTree
    
    def getQianaClosure(self) -> str:
        return self.qianaClosure
    
    def getGraphDot(self) -> str:
        return getDotFromSteps(self.reasoningSteps)
    
    def getVampireOutput(self) -> str:
        return self.vampireOutput
    
    
    

