from typing import Tuple, List
import sys
import os
import subprocess

import json

from reasoner.vampireParser import TPTPOutputParser
from interfaceTypes import ReasoningStep

def getThree(formulas : str, timeout : int) -> Tuple[bool, List[ReasoningStep], str]:
    """
    Call solver and parse its output
    @param formulas: str - the tptp representation of a set of formulas
    @return: Tuple[bool, List[ReasoningStep], str] - a tuple containing a boolean indicating if a contradiction was found, the reasoning steps performed to find the contradiction, and the raw TPTP output of the reasoning
    """
    args = ["./reasoner/vampire", "--mode",  "portfolio", "--schedule", "casc", "--output_mode", "smtcomp", "--time_limit", str(timeout)+"s"]
    result = subprocess.run(args, input=formulas, text=True, capture_output=True)
    if result.stdout == "sat\n":
        return(False, [], result.stdout)
    elif result.stdout == "unknown\n" or result.stdout == "\n" or result.stdout == "":
        return(False, [], result.stdout)
    elif result.stdout == "unsat\n":
        args = ["./reasoner/vampire"]
        result = subprocess.run(args, input=formulas, text=True, capture_output=True)
        return(True, TPTPOutputParser(result.stdout), result.stdout)
    else:
        raise Exception("Vampire returned an unexpected result: " + result.stdout)
    