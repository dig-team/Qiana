from typing import Dict, List, Set, Tuple

class Signature:

    baseFunctions : Dict[str,int] # Dict macthing function names to arity, corresponds to functions from F_b
    basePredicates : Dict[str,int]
    quotableVariables : Set[str]

    def __init__(self, functions: Dict[str,int] = {}, predicates: Dict[str,int] = {}, quotableVariables: Set[str] = set()):
        self.baseFunctions = functions
        self.basePredicates = predicates
        self.quotableVariables = quotableVariables
        

    def extendFromTptp(self, tptpFormula: str) -> None:
        pass

    def extendFromSignature(self, signature: 'Signature') -> 'Signature':
        """
        Extend and return the signature this is applied, which becomes the union of itself and the signature passed as argument
        """
        self.baseFunctions.update(signature.baseFunctions)
        self.basePredicates.update(signature.basePredicates)
        self.quotableVariables.update(signature.quotableVariables)
        return self
    
    def addFunction(self, symbol: str, arity: int) -> None:
        self.baseFunctions[symbol] = arity

    def addPredicate(self, symbol: str, arity: int) -> None:
        self.basePredicates[symbol] = arity

    def getArity(self, symbol: str) -> int:
        symbol = Signature.unquoteSymbol(symbol) or symbol
        if symbol in self.baseFunctions: return self.baseFunctions[symbol]
        if symbol in self.basePredicates: return self.basePredicates[symbol]
        if symbol in self.quotableVariables: return 0
        if symbol == self.getTruthPredicate(): return 1
        if symbol in self._getSpecialFunctions(): return self._getSpecialFunctions()[symbol]
        raise ValueError("Symbol not found in signature")
    
    @classmethod
    def quoteSymbol(cls, symbol: str) -> str:
        return f"q_{symbol}"
    
    @classmethod
    def unquoteSymbol(cls, symbol: str) -> str | None:
        """
        Unquotes a symbol if it is quoted, otherwise returns None
        """
        if symbol.startswith("q_"): return symbol[2:]
        return None
    
    def getBaseFunctions(self) -> List[str]:
        return self.baseFunctions.keys()
    
    def getAllFunctions(self) -> List[str]:
        """
        Litteraly returns anything that is a function in the signature, no exceptions

        @return: List of all functions in the signature. Should be equal to all base functions + all quoted functions + all quoted predicates + special functions + quotedVariables
        """
        return list(self.baseFunctions.keys()) + \
            [Signature.quoteSymbol(var) for var in self.baseFunctions] + \
            [Signature.quoteSymbol(var) for var in self.basePredicates] +\
            [Signature.quoteSymbol(var) for var in self._getSpecialFunctions()] +\
            [Signature.quoteSymbol(var) for var in self.quotableVariables]

    def _getSpecialFunctions(self) -> Dict[str,int]:
        # TODO : what else
        return {"qianaQuotingFunc" : 1}
    
    def getTruthPredicate(self) -> str:
        """
        Returns the name of the truth predicate in the signature
        """
        return "qianaTruth"
    
    def getBasePredicates(self) -> List[str]:
        return self.basePredicates.keys()
    
    def getAllPredicates(self) -> List[str]:
        return self.getBasePredicates() + [self.getTruthPredicate()]
    
    def getQuotedVars(self) -> List[str]:
        return [Signature.quoteSymbol(var) for var in self.quotableVariables]