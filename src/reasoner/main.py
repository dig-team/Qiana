from typing import Tuple, List
import sys
import os
import subprocess

import json

from reasoner.vampireParser import TPTPOutputParser
from interfaceTypes import ReasoningStep

def main(inputJson):
    """Main function. Should receive json text as string and outputs a pair. The first element is a boolean true if the set of formulas is SAT. The second is the corresponding full vampire output, in JSON format following the standard set by test/exampleOutput.json. """
    dbo = Dbo()
    inputData = json.loads(inputJson)
    dbo.update(inputData)
    isCoherent = dbo.testCoherence()
    if isCoherent:
        return isCoherent, "{ \"NodeList\":[],\n \"finalNode\":\"\"}" # No Json output if we did not find a contradiction
    return (isCoherent,dbo.fullCallVampire()) # Currently twice as slow as it needs to be

def getThree(formulas : str) -> Tuple[bool, List[ReasoningStep]]:
    args = ["./reasoner/vampire", "--output_mode", "smtcomp"]
    result = subprocess.run(args, input=formulas, text=True, capture_output=True)
    if result.stdout == "sat\n":
        return(False, [])
    else:
        args = ["./reasoner/vampire"]
        result = subprocess.run(args, input=formulas, text=True, capture_output=True)
        return(True, TPTPOutputParser(result.stdout))

if __name__ == "__main__":
    # path = sys.argv[1]
    path = "/home/sipirate/Documents/Doc_Divers/NoRDF/Qiana/Qiana_dig-team/example/input-example-contradiction.p"
    f = open(path,"r")
    prompt = f.read()
    print(getThree(prompt))
