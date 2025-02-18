from typing import Dict, List, Set, Tuple

class Signature:

    # TODO: this does not handle quotations well

    predicates : Dict[str, int]         # Dict matching predicates names to arities
    functions : Dict[str, int]          # Dict matching functions names to arities; contains all functions found, including quotations of predicates
    quotedFunctions : Dict[str, int]    # Dict matching quotation functions present in the input with their arities, including quotations of predicates
    quotedPredicates : Dict[str, int]   # Dict matching quoted predicates present in the input with their arities
    constants : Set[int]                # Set of the text of all constants from the input. Constants are NOT functions of arity 0
    quotedConstants : Set[str]          # Set of the text of all quotations of constants from the input. Constants are NOT functions of arity 0
    quotableVariables: Set[str]          # Set of the text of all quotable variables
    quotedVariables : Set[str]          # Set of the text of all quoted variables from the input + those we added

    def __init__(self, predicates=None, functions=None, quotedFunctions=None, quotedPredicates=None, constants=None, quotedConstants=None, quotableVariables=None, quotedVariables=None):
        self.predicates = predicates if predicates is not None else {}
        self.functions = functions if functions is not None else {}
        self.quotedFunctions = quotedFunctions if quotedFunctions is not None else {}
        self.quotedPredicates = quotedPredicates if quotedPredicates is not None else {}
        self.constants = constants if constants is not None else set()
        self.quotedConstants = quotedConstants if quotedConstants is not None else set()
        self.quotableVariables = quotableVariables if quotableVariables is not None else set()
        self.quotedVariables = quotedVariables if quotedVariables is not None else set()

    def extendFromTptp(self, tptpFormula: str) -> None:
        pass

    def getArity(self, symbol: str) -> int:
        if symbol in self.predicates: return self.predicates[symbol]
        if symbol in self.functions: return self.functions[symbol]
        if symbol in self.quotedFunctions: return self.quotedFunctions[symbol]
        if symbol in self.quotedPredicates: return self.quotedPredicates[symbol]
        if symbol in self.constants or symbol in self.quotedConstants: return 0
        raise ValueError("Symbol not found in signature or not of a type requiring an arity")

    def addFunction(self, symbolAndArity: Tuple[str, int]) -> None:
        symbol, arity = symbolAndArity
        self.functions[symbol] = arity

    def getFunctions(self) -> List[str]:
        return self.functions.keys()

    def addPredicate(self, symbolAndArity: Tuple[str, int]) -> None:
        symbol, arity = symbolAndArity
        self.predicates[symbol] = arity

    def getPredicates(self) -> List[str]:
        return self.predicates.keys()

    def addQuotableVar(self, symbol: str) -> None:
        self.quotableVariables.add(symbol)

    def getQuotableVars(self) -> List[str]:
        return self.quotableVariables

    def addConstant(self, symbol: str) -> None:
        self.constants.add(symbol)

    def getConstants(self) -> List[str]:
        return self.constants
