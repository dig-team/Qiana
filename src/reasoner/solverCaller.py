import subprocess

from reasoner.tptpWriter import listToPrompt

def testCoherence(formulaList):
    prompt = listToPrompt(formulaList)
    args = ["./reasoner/vampire", "--output_mode", "smtcomp"]
    result = subprocess.run(args, input=prompt, text=True, capture_output=True)
    return result.stdout == "sat\n"

def fullCallVampire(formulaList):
    prompt = listToPrompt(formulaList)
    args = ["./reasoner/vampire"]
    result = subprocess.run(args, input=prompt, text=True, capture_output=True)
    return result.stdout