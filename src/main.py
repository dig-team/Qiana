import subprocess
import os

from reasoner import callSolver
from qianaExtension import qianaClosure

if __name__ == "__main__":
    # path = sys.argv[1]
    with open("/home/sipirate/Documents/Doc_Divers/NoRDF/Qiana/Qiana_dig-team/example/input-example.p", "r") as f:
        prompt = f.read()
    closureOfInput : str = os.linesep.join(qianaClosure(prompt))
    jsonOutput = "".join([step.toJson() for step in callSolver(closureOfInput)[1]])
    with open("/home/sipirate/Documents/Doc_Divers/NoRDF/Qiana/Qiana_dig-team/example/output-example.json", "w") as f:
        f.write(jsonOutput)
    # path = "/home/sipirate/Documents/Doc_Divers/NoRDF/Qiana/Qiana_dig-team/example/input-example-contradiction.p"
    # f = open(path,"r")
    # prompt = f.read()
    # args = ["./reasoner/vampire", "--output_mode", "smtcomp"]
    # result = subprocess.run(args, input=prompt, text=True, capture_output=True)
    # print("\n \n", result.stdout, "\n \n")
    # if result.stdout == "sat\n":
    #     print("{ \"NodeList\":[],\n \"finalNode\":\"\"}")
    # else:
    #     args = ["./reasoner/vampire"]
    #     result = subprocess.run(args, input=prompt, text=True, capture_output=True)
    #     print(result.stdout,"\n \n")
    #     print(TPTPOutputParser(result.stdout))