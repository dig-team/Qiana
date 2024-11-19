from collections.abc import Mapping
from typing import List, Dict, Iterable, Set

import qianaExtension.Formulas as Formulas
from qianaExtension.Formulas import Formula, Term, Variable

class Signature:
    """Contains predicates, functions, and quoted functions each with their arity, as well as variables, constants, and quoted constants"""

    predicates : Dict[str, int]         # Dict matching predicates names to arities
    functions : Dict[str, int]          # Dict matching functions names to arities; contains all functions found, including quotations of predicates
    quotedFunctions : Dict[str, int]    # Dict matching quotation functions present in the input with their arities, including quotations of predicates
    quotedPredicates : Dict[str, int]   # Dict matching quoted predicates present in the input with their arities
    constants : Set[int]                # Set of the text of all constants from the input. Constants are NOT functions of arity 0
    quotedConstants : Set[str]          # Set of the text of all quotations of constants from the input. Constants are NOT functions of arity 0
    quotedVariables : Set[str]          # Set of the text of all quoted variables from the input + those we added

    def __init__(self, formulas: Iterable[Formula], numberVariables: int = 3, verbose = True) -> None:
        """Creates a signature matching a list of formulas
        @param formulas: List of formulas
        @param numberVariables: Number of quoted variables to add on top of the ones already present in the formulas
        """
        if verbose:
            # Print formulas for user
            print(f"  Creating signature for {len(formulas)} formulas...")

        self.predicates = {} 
        self.functions = {} 
        self.quotedFunctions = {} 
        self.quotedPredicates = {}
        self.constants = set() 
        self.quotedConstants = set() 
        self.quotedVariables = set() 

        # Read formulas and gather signature elements
        for f in formulas:
            self._readFormula(f)

        # Add special symbols to the signature
        self.predicates["ist"] = 2
        self.quotedVariables.update(["q_VAR_" + str(i) for i in range(numberVariables)])


        # Remove special symbols from the signature
        self.quotedConstants = self.quotedConstants - self.quotedVariables 
        self.functions.pop("quote",None) 
        self.quotedFunctions.pop("quote",None) 
        self.predicates.pop("truthPredicate",None) 

        # Quote and unquote what was found so all quoted / unquoted counterparts exist as needed
        self.functions.update({Formula.unquoteStr(f): a for f, a in self.quotedFunctions.items()})
        self.quotedFunctions.update({Formula.quoteStr(f): a for f, a in self.functions.items()})
        self.predicates.update({Formula.unquoteStr(f): a for f, a in self.quotedPredicates.items()})
        self.quotedPredicates.update({Formula.quoteStr(f): a for f, a in self.predicates.items()})
        self.constants.update({Formula.unquoteStr(f) for f in self.quotedConstants})
        self.quotedConstants.update({Formula.quoteStr(f) for f in self.constants})

        if verbose:
            print("    Quoted variables: " + str([a for a in self.quotedVariables]))
            print("    Constants: " + str([a for a in self.constants]))
            print("    Quoted constants: " + str([a for a in self.quotedConstants]))
            print("    Predicates: " + str(self.predicates))
            print("    Functions: " + str(self.functions))
            print("    Quoted functions: " + str(self.quotedFunctions))
            print("  done")

    def _readFormula(self, formula: Formula) -> None:
        """Reads a formula and updates the signature."""
        if isinstance(formula, Formulas.Atom) and formula.operator == "ist":
            self._readTerm(formula.args[0])
            self._readQuotedFormula(formula.args[1])
            return
        if isinstance(formula, Formulas.Atom):
            self.predicates[formula.operator] = formula.getArity()
            for t in formula.args:
                self._readTerm(t)
            return
        if isinstance(formula, Formulas.Forall):
            for v in formula.variables:
                self.quotedVariables.add(Formula.quoteStr(v.function))
            assert len(formula.args) == 1
            self._readFormula(formula.args[0])
            return
        if formula.operator in Formula.OPERATORS:
            for f in formula.args:
                self._readFormula(f)
            return
        raise Exception("Unexpected operator in formula: " + formula.operator)

    def _readTerm(self, term: Term) -> None:
        """Reads a term and updates the signature."""
        if isinstance(term, Variable):
            self.quotedVariables.add(Formula.quoteStr(term.function))
            return
        if Formula.isQuoted(term.function):
            self._readQuotedTerm(term)
            return
        if not term.args:
            self.constants.add(term.function)
            return
        self.functions[term.function] = term.getArity()
        for t in term.args:
            self._readTerm(t)

    def _readQuotedFormula(self, term : Term) -> None:
        """Reads a term that is a quoted formula and updates the signature witht the logic symbols found"""
        if isinstance(term, Variable):
            self.quotedVariables.add(Formula.quoteStr(term.function))
            return
        if Signature._isAtomicQuotedFormula(term):
            self.quotedPredicates[term.function] = term.getArity()
            for t in term.args:
                self._readQuotedTerm(t)
            return
        if term.function == "q_Forall":
            self.quotedVariables.add(term.args[0].function)
            self._readQuotedFormula(term.args[1])
            return
        for t in term.args:
            self._readQuotedFormula(t)

    @staticmethod
    def _isAtomicQuotedFormula(term : Term) -> bool:
        """Takes a term that is a quoted formula and returns whether the quoted formula in question is a predicate application. No side effects."""
        return not term.function in Formula.OPERATORS.values() # Check if the function is a quotation of logic operator. If not, term is a quotation of an atom

    def _readQuotedTerm(self, term : Term) -> None:
        """Reads a quoted term and updates the signature"""
        if isinstance(term, Variable):
            self.quotedVariables.add(Formula.quoteStr(term.function))
            return
        if term.function == "q_quote":
            return  # Pass at quote operator, we do not know whether to expect a variable, a quoted term, or a quoted formula
        if not term.args:
            self.quotedConstants.add(term.function)
            return
        self.quotedFunctions[term.function] = term.getArity()
        for t in term.args:
            self._readQuotedTerm(t)
        