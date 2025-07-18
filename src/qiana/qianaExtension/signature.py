from typing import Dict, List, Set, Tuple

import os

from qiana.qianaExtension.tptpUtils import quoteSymbol, unquoteSymbol, isQuoted, get_special_functions_arities, getTruthPredicate, next_quoted_var
from qiana.qianaExtension.tptpParsing import parseSymbols

class Signature:

    baseFunctions : Dict[str,int] # Dict macthing function names to arity, corresponds to functions from F_b
    basePredicates : Dict[str,int]
    nbrQuotedVars : int
    quotedVars : str

    def __init__(self, functions: Dict[str,int] = None, predicates: Dict[str,int] = None, nbrQuotedVars: int = 5):
        self.baseFunctions = functions if functions else {}
        self.basePredicates = predicates if predicates else {}
        self.nbrQuotedVars = nbrQuotedVars
        
    def extendFromSignature(self, signature: 'Signature') -> 'Signature':
        """
        Extend and return the signature this is applied, which becomes the union of itself and the signature passed as argument
        """
        self.baseFunctions.update(signature.baseFunctions)
        self.basePredicates.update(signature.basePredicates)
        self.nbrQuotedVars = max(self.nbrQuotedVars, signature.nbrQuotedVars)
        return self
    
    def addFunction(self, symbol: str, arity: int) -> None:
        self.baseFunctions[symbol] = arity

    def addPredicate(self, symbol: str, arity: int) -> None:
        self.basePredicates[symbol] = arity

    def getArity(self, symbol: str) -> int:
        symbol = unquoteSymbol(symbol) or symbol
        if symbol in self.baseFunctions: return self.baseFunctions[symbol]
        if symbol in self.basePredicates: return self.basePredicates[symbol]
        if symbol in self.getQuotedVars(): return 0
        if symbol == getTruthPredicate(): return 1
        if symbol in get_special_functions_arities(): return get_special_functions_arities()[symbol]
        raise ValueError("Symbol not found in signature")

    def getBaseFunctions(self) -> List[str]:
        return self.baseFunctions.keys()
    
    def getAllFunctions(self) -> List[str]:
        """
        Litteraly returns anything that is a function in the signature, no exceptions

        @return: List of all functions in the signature. Should be equal to all base functions + all quoted functions + all quoted predicates + special functions + quotedVariables
        """
        return list(self.baseFunctions.keys()) + \
            [quoteSymbol(var) for var in self.baseFunctions] + \
            [quoteSymbol(var) for var in self.basePredicates] +\
            [quoteSymbol(var) for var in get_special_functions_arities()] +\
            [quoteSymbol(var) for var in self.getQuotedVars()]
    
    def getBasePredicates(self) -> List[str]:
        return list(self.basePredicates.keys())
    
    def getAllPredicates(self) -> List[str]:
        return self.getBasePredicates() + [getTruthPredicate()]
    
    def getQuotedVars(self) -> List[str]:
        return next_quoted_var([], self.nbrQuotedVars)
    
    def extendFromTptps(self, tptpFormulas: str) -> None:
        """
        Read text matching a list of TPTP formulas (possibly with linebreaks and formulas split over multiple lines) and extend the signature with the functions and predicates found in the formulas.
        """
        lines = [line for line  in tptpFormulas.splitlines() if not line.startswith("%") and line.strip()]
        formula = ""
        for line in lines:
            formula += " " + line.strip()
            if line.strip().endswith(")."):
                body = formula.split(",", 2)[2].strip().removesuffix(").") # go from fof(name, role, body). to body
                self.extendFromTptp(body)
                formula = ""

    def extendFromTptp(self, tptpFormula: str) -> None:
        """
        Read the body of a TPTP formula and extend the signature with the functions and predicates found in the formula.
        @param tptpFormula: The body of a TPTP formula, example : "![X1] : p(f(X1),X1)"
        """
        for symbol, (arity, isFunction) in parseSymbols(tptpFormula).items():
            if symbol[0].isupper(): continue # We don't want to add variables
            if symbol in get_special_functions_arities() or symbol == getTruthPredicate(): continue
            if isQuoted(symbol): continue # We can't know if it's a quoted function or predicate, so we skip the case. 
            if isFunction: self.addFunction(symbol, arity)
            else: self.addPredicate(symbol, arity)

    def _parseFormula(formula : str, formulasNext : bool = False) -> List[Tuple[str, int, bool]]:
        """
        Take a formula (for example "![X1] p(f(X1))") and returns a list of tuple containing each symbol along with its arity and a isAFunction boolean
        """
      
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
        if "]" in formula: 
            splitformula = formula.split("]", 1)[1].strip()
            assert splitformula.startswith(":"), f"Expected ':' after ']' in {formula}"
            formula = splitformula[1:].strip()
        if not formula : return []
        
        # Remove outermost parenthesis
        while formula[0] == "(":
            parenthesis_level = 0
            for i, char in enumerate(formula):
                if char == "(":
                    parenthesis_level += 1
                elif char == ")":
                    parenthesis_level -= 1
                if parenthesis_level == 0:
                    break
            if i == len(formula) - 1:
                formula = formula[1:-1].strip()
            else:
                break

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
        symbol, arguments = Signature._parseTopLevel(formula)

        # Only variables start with an uppercase char
        if not symbol[0].islower():
            assert not arguments
            return []
        
        return [(symbol, len(arguments), formulasNext)] + [tuple for arg in arguments for tuple in Signature._parseFormula(arg, True)]

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