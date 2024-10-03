from typing import Tuple, List
import sys
import os
import subprocess

import json

from reasoner.vampireParser import TPTPOutputParser
from interfaceTypes import ReasoningStep

def getThree(formulas : str) -> Tuple[bool, List[ReasoningStep], str]:
    """
    Call solver and parse its output
    @param formulas: str - the tptp representation of a set of formulas
    @return: Tuple[bool, List[ReasoningStep], str] - a tuple containing a boolean indicating if a contradiction was found, the reasoning steps performed to find the contradiction, and the raw TPTP output of the reasoning
    """
    args = ["./reasoner/vampire", "--output_mode", "smtcomp"]
    result = subprocess.run(args, input=formulas, text=True, capture_output=True)
    if result.stdout == "sat\n":
        return(False, [], result.stdout)
    else:
        args = ["./reasoner/vampire"]
        result = subprocess.run(args, input=formulas, text=True, capture_output=True)
        return(True, TPTPOutputParser(result.stdout), result.stdout)

if __name__ == "__main__":
    # path = sys.argv[1]
    path = "/home/sipirate/Documents/Doc_Divers/NoRDF/Qiana/Qiana_dig-team/example/input-example-contradiction.p"
    f = open(path,"r")
    prompt = f.read()
    print(getThree(prompt))
