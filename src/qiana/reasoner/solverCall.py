from typing import Tuple, List
import sys
import os
import subprocess

import json

from qiana.reasoner.vampireParser import TPTPOutputParser
from qiana.interfaceTypes import ReasoningStep

class SolverCall:
    """
    Class to store the result of a call to Vampire
    """

    simpleResult: str
    reasoningSteps: List[ReasoningStep]
    vampireOutput: str
    error: str

    def __init__(self, inputTPTP: str, simpleResult: str, reasoningSteps: List[ReasoningStep], vampireOutput: str, error: str = "") -> None:
        assert simpleResult in ["sat", "unsat", "unknown","error"]
        self.inputTPTP = inputTPTP
        self.simpleResult = simpleResult
        self.reasoningSteps = reasoningSteps
        self.vampireOutput = vampireOutput
        self.error = error

    @classmethod
    def callVampire(cls, formulas: str, timeout: int) -> "SolverCall":
        """
        Call Vampire and store the result in the class
        @param formulas: str - the tptp representation of a set of formulas

        @param timeout: int - the timeout value for the solver
        """
        vampirepath = os.path.join(os.path.dirname(__file__), "vampire")

        args = [vampirepath, "--mode",  "portfolio", "--schedule", "casc", "--output_mode", "smtcomp", "--time_limit", str(timeout)+"s"]
        result = subprocess.run(args, input=formulas, text=True, capture_output=True)
        if result.stdout == "sat\n":
            simpleResult = "sat"
            reasoningSteps = []
        elif result.stdout == "unknown\n" or result.stdout == "\n" or result.stdout == "":
            simpleResult = "unknown"
            reasoningSteps = []
        elif result.stdout == "unsat\n":
            args = [vampirepath, "--mode",  "portfolio", "--schedule", "casc", "--time_limit", str(timeout)+"s"]
            result = subprocess.run(args, input=formulas, text=True, capture_output=True)
            simpleResult = "unsat"
            reasoningSteps = TPTPOutputParser(result.stdout)
        elif result.stderr:
            simpleResult = "error"
            reasoningSteps = []
            raise ValueError("Vampire returned an error: " + result.stderr)
        else:
            raise ValueError("Vampire returned an unexpected result: " + result.stdout)

        return cls(formulas, simpleResult, reasoningSteps, result.stdout, result.stderr)
    
    def contradictionFound(self) -> bool:
        """
        Check if a contradiction was found
        @return: bool - True if a contradiction was found, False otherwise
        """
        return self.simpleResult == "unsat"