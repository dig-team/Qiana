import os
from os.path import join, dirname

from qiana.reasoner import SolverCall
from qiana.qianaExtension import Signature, getAllSchemesInstances, applyMacros
from qiana.htmlGeneration import getHtmlFromSteps, getHtmlNoContradiction
from qiana.dotGeneration import getDotFromSteps
from qiana.extendsimplifiedsyntax import extend_simplified_syntax

def run_qiana(input : str, quotedVariableNumber: int = 5, simplified_input: bool = False, expand_macros: bool = False, timeout: int = 5) -> str:
    """Compute the qiana closure of the input and run the solver on it.

    Only returns the result of the solver. If you need more granular control
    or detailed results, use the QianaPipeline class instead.

    Args:
        input: The tptp representation of a set of formulas, either full
            first-order TPTP formulas or simplified syntax.
        quotedVariableNumber: Number of quoted variables to use in the qiana
            closure. Defaults to 5.
        simplified_input: If True, the headers on formulas will be
            automatically added. Defaults to False.
        expand_macros: If True, the qiana specific macros will be expanded
            before computing the qiana closure. Defaults to False.
        timeout: The timeout value for the solver in seconds. Defaults to 5.

    Returns:
        Either "sat", "unsat", "unknown", or "timeout" depending on the result
        of the solver. Note that "timeout" is estimated from the time it took
        the solver to answer "unknown" and therefore may in rare cases be
        output where "unknown" would be more appropriate.

    Raises:
        ValueError: If the solver returns an error or if the input is not a
            valid tptp representation of a set of formulas.
    """
    pipeline = QianaPipeline()
    pipeline.compute_qiana_closure(input, quotedVariableNumber, simplified_input, expand_macros)
    pipeline.run_compute(timeout, compute_steps=False)
    if pipeline.get_solver_result().simpleResult == "error":
        raise ValueError(f"Vampire returned an error: {pipeline.get_solver_result().error} \n \n The standard output of the solver was: {pipeline.get_solver_result().vampireOutput}")
    return pipeline.get_solver_result().simpleResult

class QianaPipeline:
    """
    Class to handle the entire Qiana pipeline: compute the qiana closure, call the solver, and return the result.
    """
    qianaClosure : str | None
    htmlTree : str | None
    reasoningSteps : list[str] | None
    foundContradiction : bool | None
    simpleResult : str | None
    vampireOutput : str | None
    solver_call : SolverCall | None

    def __init__(self) -> None:
        self.qianaClosure = None
        self.htmlTree = None

    def compute_qiana_closure(self, input: str, quotedVariableNumber: int | None = 5, simplified_input : bool = False, expand_macros : bool = False) -> None:
        """Compute the qiana closure of the input and store it in self.qianaClosure.

        Args:
            input: The tptp representation of a set of formulas.
            quotedVariableNumber: The number of quoted variables to use in the
                qiana closure. Defaults to 5. This argument should ideally
                always be specified when calling from the CLI as otherwise the
                value stored in Settings will be used.
            simplified_input: If True, the headers on formulas will be
                automatically added. Defaults to False.
            expand_macros: If True, the qiana specific macros will be expanded
                before computing the qiana closure. Defaults to False.
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

    def run_compute(self, timeout : int = 5, compute_steps : bool = True) -> None:
        """Run the solver on the already computed qiana closure.

        Updates the internal state with the result.

        Args:
            timeout: The timeout value for the solver in seconds. Defaults to 5.
            compute_steps: Whether to compute the reasoning steps or not when
                a contradiction is found. Defaults to True.
        """
        self._callSolver(timeout, compute_steps)

    def run_pipeline(self, input: str, quotedVariableNumber: int | None = 5, simplified_input : bool = False, expand_macros : bool = False, timeout: int = 5) -> str:
        """Run the entire pipeline: compute the qiana closure, call the solver, and return the result.

        Equivalent to running compute_qiana_closure(), run_compute(), and
        get_solver_result().simpleResult in sequence.

        Args:
            input: The tptp representation of a set of formulas.
            quotedVariableNumber: The number of quoted variables to use in the
                qiana closure. Defaults to 5. This argument should ideally
                always be specified when calling from the CLI as otherwise the
                value stored in Settings will be used.
            simplified_input: If True, the headers on formulas will be
                automatically added. Defaults to False.
            expand_macros: If True, the qiana specific macros will be expanded
                before computing the qiana closure. Defaults to False.
            timeout: The timeout value for the solver in seconds. Defaults to 5.

        Returns:
            Either "sat", "unsat", "unknown", or "timeout" depending on the
            result of the solver.
        """
        self.compute_qiana_closure(input, quotedVariableNumber, simplified_input, expand_macros)
        self._callSolver(timeout)
        return self.simpleResult

    def get_solver_result(self) -> SolverCall:
        """Get a SolverCall object corresponding to calling the solver.

        Must be called after running the solver.

        Returns:
            The result of the solver call.
        """
        return self.solver_call

    def contradiction(self) -> bool:
        """Check if a contradiction was found in the qiana closure.

        Must be called after running the solver.

        Returns:
            True if a contradiction was found, False otherwise.
        """
        return self.foundContradiction
    
    def unknown_result(self) -> bool:
        """Check if the solver returned an unknown result.

        Must be called after running the solver.

        Returns:
            True if the solver returned an unknown result, False otherwise.
        """
        return self.simpleResult == "unknown"
    
    def timeout(self) -> bool:
        """Check if the solver timed out.

        Must be called after running the solver.

        Returns:
            True if the solver timed out, False otherwise.
        """
        return self.simpleResult == "timeout"

    def getHtmlTree(self) -> str:
        return self.htmlTree
    
    def get_qiana_closure(self) -> str:
        return self.qianaClosure
    
    def get_graphdot(self) -> str:
        return getDotFromSteps(self.reasoningSteps)
    
    def get_vampire_output(self) -> str:
        return self.vampireOutput

    def runCompute_GUI(self, input: str) -> None:
        """Compute and run the solver for GUI usage.

        Takes as input the tptp representation of a set of formulas and computes
        the html representation of the reasoning steps performed to find a
        contradiction on the qiana closure of input. Uses the timeout value
        from the settings.

        Args:
            input: The tptp representation of a set of formulas (not
                necessarily closed under qiana).
        """
        self.compute_qiana_closure(input)
        from qiana.gui import Settings
        timeout = Settings.getTimeOutValue()
        self._callSolver(timeout)

    def _callSolver(self, timeout: int, get_reasonin_steps : bool) -> None:
        """Call the solver and store the result in self.reasoningSteps.

        Assumes the qiana closure has already been computed and stored in
        self.qianaClosure.

        Args:
            timeout: The timeout value for the solver.
            get_reasonin_steps: Whether to compute the reasoning steps or not
                when a contradiction is found.

        Raises:
            ValueError: If the qiana closure has not been computed yet.
        """
        if not self.qianaClosure: raise ValueError("Qiana closure has not been computed yet. Please call computeQianaClosure() before running the solver.")
        self.solver_call : SolverCall = SolverCall.call_solver(self.qianaClosure, timeout, get_reasonin_steps)
        self.foundContradiction = self.solver_call.simpleResult == "unsat"
        self.simpleResult = self.solver_call.simpleResult
        self.reasoningSteps = self.solver_call.reasoningSteps
        self.vampireOutput = self.solver_call.vampireOutput
        self.htmlTree = getHtmlFromSteps(self.reasoningSteps) if self.foundContradiction else getHtmlNoContradiction(self.vampireOutput)


    
    

