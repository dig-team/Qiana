from typing import Dict, List, Set, Tuple

class Signature:

    baseFunctions : Dict[str,int] # Dict macthing function names to arity, corresponds to functions from F_b
    basePredicates : Dict[str,int]
    quotableVariables : Set[str]

    def __init__(self, functions: Dict[str,int] = None, predicates: Dict[str,int] = None, quotableVariables: Set[str] = None):
        self.baseFunctions = functions if functions else {}
        self.basePredicates = predicates if predicates else {}
        self.quotableVariables = quotableVariables if quotableVariables else set()
        
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
    
    @classmethod
    def isQuoted(cls, symbol: str) -> bool:
        return symbol.startswith("q_")
    
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

    def extendFromTptp(self, tptpFormula: str) -> None:
        """
        Read the body of a TPTP formula and extend the signature with the functions and predicates found in the formula.
        @param tptpFormula: The body of a TPTP formula, example : "![X1] p(f(X1),X1)"
        """
        for symbol, arity, isFunction in Signature._parseFormula(tptpFormula):
            if symbol in self._getSpecialFunctions() or symbol == self.getTruthPredicate():
                continue
            if Signature.isQuoted(symbol):
                # We can't know if it's a quoted function or predicate, so we skip the case. # TODO : add to both instead? It would create additional schemes but maybe that would be fine?
                continue
            if isFunction:
                self.addFunction(symbol, arity)
            else:
                self.addPredicate(symbol, arity)

    def _parseFormula(formula : str, formulasNext : bool = False) -> List[Tuple[str, int, bool]]:
        """
        Take a formula (for example "![X1] p(f(X1))") and returns a list of tuple containing each symbol along with its arity and a isAFunction boolean
        """
        def _parseTopLevel(formula : str) -> Tuple[str, List[str]]:
            """
            Read a formula of the form $f(a1, a2, ..., an)$ and return the function name and the arguments
            """
            formula = formula.strip()
            name_end = formula.find('(')
            if name_end == -1:
                return formula.strip(), []
            
            name = formula[:name_end].strip()
            
            if not formula.endswith(')'):
                raise ValueError(f"Formula missing closing parenthesis: {formula}")
            
            arg_string = formula[name_end + 1:-1]
            
            args = []
            if arg_string.strip():
                current_arg = ""
                paren_level = 0
                for char in arg_string:
                    if char == '(' and paren_level == 0:
                        current_arg += char
                        paren_level += 1
                    elif char == '(' and paren_level > 0:
                        current_arg += char
                        paren_level += 1
                    elif char == ')' and paren_level > 1:
                        current_arg += char
                        paren_level -= 1
                    elif char == ')' and paren_level == 1:
                        current_arg += char
                        paren_level -= 1
                    elif char == ',' and paren_level == 0:
                        args.append(current_arg.strip())
                        current_arg = ""
                    else:
                        current_arg += char
                
                if current_arg:
                    args.append(current_arg.strip())
            
            return name, args

        if "]" in formula: formula = formula.split("]", 1)[1] 
        if not formula : return []
        if formula[0] == "(" and formula[-1] == ")": formula = formula[1:-1].strip()

        # Handle the only unary logical connectives 
        if formula.startswith("~"):
            return Signature._parseFormula(formula[1:], True)

        binary_connectives = ["&", "=>", "<=>", "|"]
        parenthesis_level = 0
        for i, char in enumerate(formula):
            if char == "(":
                parenthesis_level += 1
            elif char == ")":
                parenthesis_level -= 1
            elif parenthesis_level == 0 :
                for connective in binary_connectives:
                    if formula[i:].startswith(connective):
                        assert not formulasNext 
                        return Signature._parseFormula(formula[:i], formulasNext) + Signature._parseFormula(formula[i+len(connective):], formulasNext)

        # Reach this only if there were no toplevel connectives
        symbol, arguments = _parseTopLevel(formula)

        # Only variables start with an uppercase char
        if not symbol[0].islower():
            assert not arguments
            return []
        
        return [(symbol, len(arguments), formulasNext)] + [tuple for arg in arguments for tuple in Signature._parseFormula(arg, True)]
