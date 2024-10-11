from collections.abc import Mapping
from typing import List, Dict, Iterable, Set

from qianaExtension.Formulas import Formula

class Signature:
    """Contains predicates, functions, and quoted functions each with their arity, as well as variables, constants, and quoted constants"""

    predicates : Dict[str, int]         # Dict matching predicates names to arities
    functions : Dict[str, int]          # Dict matching functions names to arities; contains all functions found, including quotations of predicates
    quotedFunctions : Dict[str, int]    # Dict matching quotation functions present in the input with their arities, including quotations of predicates
    constants : Set[int]                # Set of the text of all constants from the input
    quotedConstants : Set[str]          # Set of the text of all quotations of constants from the input
    quotedVariables : Set[str]          # Set of the text of all quoted variables from the input + those we added

    def __init__(self, formulas: Iterable[Formula], numberVariables: int = 3, verbose = False) -> None:
        """Creates a signature matching a list of formulas
        @param formulas: List of formulas
        @param numberVariables: Number of quoted variables to add on top of the ones already present in the formulas
        """
        if verbose:
            # Print formulas for user
            print(f"  Creating signature for {len(formulas)} formulas...")

        # Gather the components of the formulas
        self.predicates : Dict[str, int] = {} 
        self.quotedVariables : Set[str]= set() 
        self.functions : Dict[str, int] = {} 
        self.constants : Set[int] = set() 
        self.quotedConstants : Set[str] = set() 
        self.quotedFunctions : Dict[str, int] = {} 

        for f in formulas:
            f.getComponents(self.predicates, self.functions)

        for f in set(self.functions):
            if Formula.isQuoted(f):
                if self.functions[f] == 0: # If the function is a constant
                    if Formula.isQuotedVariable(f):
                        self.quotedVariables.add(f)
                    else:
                        self.quotedConstants.add(f)
                else:
                    self.quotedFunctions[f] = self.functions[f]
                self.functions.pop(f, None)
            elif self.functions[f] == 0:
                self.constants.add(f)
                self.functions.pop(f, None)


        # Create variable quotations, make sure we have 3 more than the total number of vars from the initial set of formulas
        #
        self.quotedVariables.update(["q_VAR_" + str(i) for i in range(numberVariables)])

        # Remove special elements
        self.predicates.pop("ist", None)
        self.functions.pop("quote", None)
        self.quotedFunctions.pop("q_Quote", None)
        self.predicates.pop("truthPredicate", None)
        for q in Formula.OPERATORS.values():
            self.quotedFunctions.pop(q, None)

        if verbose:
            print("    Quoted variables: " + str([a for a in self.quotedVariables]))
            print("    Constants: " + str([a for a in self.constants]))
            print("    Quoted constants: " + str([a for a in self.quotedConstants]))
            print("    Predicates: " + str(self.predicates))
            print("    Functions: " + str(self.functions))
            print("    Quoted functions: " + str(self.quotedFunctions))
            print("  done")