""" Qiana

Compute the Qiana closure of a given input theory. Both the input and the output should be in TPTP format.
"""

import sys

import FormulaParser
import Formulas
import Schemes

if len(sys.argv) != 3:
    print(
        """ Qiana

        Compute the Qiana closure of a given input theory. Both the input and the output should be in TPTP format.
        By convention, symbols starting with the letter q are quotations of the symbols that share the same name without the q.
        In this example code, the total number of variables is set to 3+the number of variables used in the input. 

        Call with "python3 Qiana.py input.p output.p".
        """
    )
    sys.exit(1)

print("Creating finite Qiana schemes...")
print(f"  Input file: {sys.argv[1]}")
print(f"  Output file: {sys.argv[2]}")
inputFormulas = FormulaParser.readFormulasFromFile(sys.argv[1])
signature = Formulas.Signature(*inputFormulas)
print("  Writing schemes... ", end="", flush=True)
with open(sys.argv[2], "wt") as outputFile:
    counter = 0
    for formula in inputFormulas:
        counter += 1
        outputFile.write(f"fof(axiom_{counter},{formula.type},{formula}).\n")
    Schemes.outputSchemes(
        lambda identifier, formula: outputFile.write(
            f"fof({identifier},axiom,{formula}).\n"
        ),
        signature,
    )
print("done\ndone")
