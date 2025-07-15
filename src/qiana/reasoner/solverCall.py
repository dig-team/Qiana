from typing import List
import os
import subprocess


from qiana.reasoner.vampireParser import TPTPOutputParser
from qiana.interfaceTypes import ReasoningStep

class SolverCall:
    """
    Class to store the result of a call to the integrated solver (Vampire).
    To call the solver, use the class method `call_solver`, which will return an instance of this class.
    """

    simpleResult: str
    """The simple result of the solver call, can be 'sat', 'unsat', 'unknown', or 'error'."""
    reasoningSteps: List[ReasoningStep]
    """The reasoning steps obtained from the solver, if any."""
    vampireOutput: str
    """The raw output from the solver."""
    error: str
    """Any error message from the solver, if applicable. If an error occures not ouput by the solver, an exception is raised instead of this being set."""

    @classmethod
    def call_solver(cls, formulas: str, timeout: int, compute_steps : bool = True) -> "SolverCall":
        """
        Call Vampire and store the result in the class
        @param formulas: str - the tptp representation of a set of formulas
        @param timeout: int - the timeout value for the solver
        @param compute_steps: bool - whether to compute the reasoning steps or not, if a contradiction is found
        """
        vampirepath = os.path.join(os.path.dirname(__file__), "vampire")

        args = [vampirepath, "--mode",  "portfolio", "--schedule", "casc", "--output_mode", "smtcomp", "--time_limit", str(timeout)+"s"]
        result = subprocess.run(args, input=formulas, text=True, capture_output=True)
        if result.stdout == "sat\n":
            simpleResult = "sat"
            reasoningSteps = []
        elif result.stdout == "unknown\n":
            simpleResult = "unknown"
            reasoningSteps = []
        elif result.stdout == "unsat\n" and compute_steps:
            simpleResult = "unsat"
            args = [vampirepath, "--mode",  "portfolio", "--schedule", "casc", "--time_limit", str(timeout)+"s"]
            result = subprocess.run(args, input=formulas, text=True, capture_output=True)
            reasoningSteps = TPTPOutputParser(result.stdout)
        elif result.stdout == "unsat\n" and not compute_steps:
            simpleResult = "unsat"
            reasoningSteps = []
        elif result.stderr:
            simpleResult = "error"
            reasoningSteps = []
        else:
            raise ValueError("Vampire returned an unexpected result: " + result.stdout)

        return cls(formulas, simpleResult, reasoningSteps, result.stdout, result.stderr)
    
    def __init__(self, inputTPTP: str, simpleResult: str, reasoningSteps: List[ReasoningStep], vampireOutput: str, error: str = "") -> None:
        assert simpleResult in ["sat", "unsat", "unknown", "error"]
        self.inputTPTP = inputTPTP
        self.simpleResult = simpleResult
        self.reasoningSteps = reasoningSteps
        self.vampireOutput = vampireOutput
        self.error = error
