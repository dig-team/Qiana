from typing import List, Dict, Tuple

import re

from qiana.qianaExtension.tptpUtils import quoteSymbol
from qiana.qianaExtension.signature import Signature

class SchemeInfo():
    name :str
    body : str
    aritySymbols : List[str]
    symbolTargets : Dict[str,str]
    symbolQuotationMatchings : Dict[str,str]
    _containsSwapPatterns : bool
    distinctPairs : List[Tuple[str,str]]
    artityRanges : Dict[str, Tuple[float, float]]

    def __init__(self, name: str, body: str, aritySymbols: List[str], symbolTargets: Dict[str, str], symbolQuotationMatchings: Dict[str, str], containsSwapPatterns: bool, distinctPairs: List[Tuple[str,str]]):
        """
        Initialize a SchemeInfo object and stores the attributes. It should be noted the the symbolTargets attribute can contain matching of symbols of the form $f[x;y] where x and y give a limit to the range of the arity of $f. This information will be extracted during initialization and is not present in the symbols returned by getSymbolTargets
        """
        self.name = name
        self.body = body
        self.aritySymbols = aritySymbols
        self.symbolTargets = symbolTargets
        self.symbolQuotationMatchings = symbolQuotationMatchings
        self._containsSwapPatterns = containsSwapPatterns
        self.distinctPairs = distinctPairs
        self._extractRangeInfo()

    def testValidCase(self, case : Dict[str,str], sig : Signature) -> bool:
        """
        Test an association of values to symbol and check its validity according to the following constraints given by the scheme
        1. No two symbols that are supposed to be distinct are equal
        2. The arity of each dot pattern is in the range given by the scheme
        3. The symbols used in the scheme are in the signature
        """
        # Check the symbols are in the signature
        if not all([symbol in sig.getAllFunctions() or symbol in sig.getAllPredicates() for symbol in case.values()]): return False
        if not self._respectDistinctPairs(case): return False
        for symbol, target in case.items():
            if symbol not in self.artityRanges: 
                assert symbol in self.symbolQuotationMatchings
                continue # Symbols that quote another symbols are not in the arity ranges
            lower, upper = self.artityRanges[symbol]
            if not (lower <= sig.getArity(target) <= upper): return False
        return True

    def _respectDistinctPairs(self, case: Dict[str, str]) -> bool:
        """
        Returns True if the case respects all the distinct pairs, False otherwise

        @param case: Dict[str, str] - a mapping of swap pattern symbols to the concrete symbols they are replaced by
        @return: bool - True if the case respects all the distinct pairs, False otherwise
        """
        for (symbol1, symbol2) in self.distinctPairs:
            assert symbol1.startswith("$")
            if symbol2.startswith("$") : target = case[symbol2]
            else: target = symbol2
            if case[symbol1] == target:
                return False
        return True

    def getBody(self) -> str:
        return self.body

    def getName(self) -> str:
        return self.name
    
    def containsSwapPatterns(self) -> bool:
        """
        True if there is at list a swap pattern in the scheme
        """
        return self._containsSwapPatterns
    
    def _extractRangeInfo(self) -> None:
        """
        Called at the end of the initialization to extract the range information from the symbolTargets attribute. Reads all symbol used in the symbolTargets dict and extracts the range information from them, which is stored in the SchemeInfo object. 
        For example if {"$f[1;3]": "BASE_FUNCTION"} is in symbolTargets, this will extract the information that $f has arity between 1 and 3 and update symbolTargets to contain {"$f" : "BASE_FUNCTION"} instead. Remark that a value of -1 is considered as infinity for the upper bound.
        """
        newSymbolTargets = dict()
        arityRanges : Dict[str, Tuple[float, float]] = dict()
        
        for symbol, target in self.symbolTargets.items():
            range_pattern = re.compile(r'^(.*?)\[(\d+);(-?\d+)\]$')
            match = range_pattern.match(symbol)
            if match:
                base_symbol = match.group(1)
                lower = float(match.group(2))
                upper = float(match.group(3))
                if upper == -1: 
                    upper = float("inf")
                newSymbolTargets[base_symbol] = target
                arityRanges[base_symbol] = (lower, upper)
            else:
                range_pattern = re.compile(r'^\$[a-zA-Z0-9_]+')
                assert range_pattern.match(symbol)
                newSymbolTargets[symbol] = target
                arityRanges[symbol] = (0, float("inf"))
        self.symbolTargets = newSymbolTargets
        self.artityRanges = arityRanges


    def getAritySymbols(self) -> List[str]:
        """
        Returns the list of swap pattern symbols that are used to indicate the arities of the dot patterns in the body of the scheme
        """
        return self.aritySymbols

    def getSymbolTargets(self) -> Dict[str,str]:
        """
        @return a dictionary matching swap pattern symbols to a word indicating what to swap it with (for example "FUNCTION" or "PREDICATE")
        """
        return self.symbolTargets
    
    def enrichSymbolDict(self, symbolDict: Dict[str,str]) -> Dict[str,str]:
        """
        Enrich a dict matching pattern symbols (like $f) to their actual symbol (like "multiply") with more such matchings to account for symbols that represent the quotation of another symbol

        @param symbolDict: a dictionary matching symbols to their actual meaning
        @return: The same dictionary, but (possibly) with more matchings
        """
        for quoting, quoted in self.symbolQuotationMatchings.items():
           symbolDict[quoting] = quoteSymbol(symbolDict[quoted]) 
           # symbolDict matches a swap pattern symbol like $f to an actual function symbol like "multiply", symbolQuotationMatchings matches a swap pattern symbol that is a quotation to the swap pattern symbol it needs to be a quotation of (for example matching $qf to $f). So we need to find what the actual symbol associated to $f is, quote it, and then associate that quotation to $qf in symbolDict
        return symbolDict

def getAllSchemeInfos(lines: list[str]) -> Tuple[List[SchemeInfo],Signature]:
    """
    Read all the scheme infos from a list of lines. This returns a list of SchemeInfo objects and a Signature object.
    """
    lines = [line.strip().rstrip("\n\r") for line in lines]
    lines = [line for line in lines if line and line[0] != "%"] # We remove empty lines and comments
    
    signature = Signature()

    # We parse the lines that define the signature and extend the signature we received
    newLines = []
    for line in lines:
        if line.startswith("FUNCTION "):
            signature.addFunction(*_getSymbolAndArity(line))
        elif line.startswith("PREDICATE "):
            signature.addPredicate(*_getSymbolAndArity(line))
        else:
            newLines.append(line)
    lines = newLines
    
    # We parse the lines that define formula schemes
    formulaNames = []
    formulas = []
    patternInfos : List[List[str]] = []
    index = -1
    for line in lines:
        assert line.startswith("FORMULA ") \
            or line.startswith("BODY ") \
            or line.startswith("DOT_ARITIES ") \
            or line.startswith("RANGE ") \
            or line.startswith("WITH ") \
            or line.startswith("DISTINCT ")
        if line.startswith("FORMULA "):
            formulaNames.append(line.removeprefix("FORMULA "))
            patternInfos.append([])
            index += 1
        elif line.startswith("BODY "):
            formulas.append(line.removeprefix("BODY "))
        else:
            patternInfos[index].append(line)
        
    assert len(formulas) == len(formulaNames) == len(patternInfos)
    schemeInfos =  [_readSchemeInfo([formulaNames[i], formulas[i]] + patternInfo) for i, patternInfo in enumerate(patternInfos)]
    return schemeInfos, signature

def _getSymbolAndArity(line:str) -> Tuple[str, int]:
    """
    Parses a line indicating a symbol's arity.

    @return: Tuple[str, int] - the symbol and its arity
    """
    # line should be of the form "FUNCTION f OF ARITY 2" or "PREDICATE p OF ARITY 1"
    assert line.startswith("FUNCTION ") or line.startswith("PREDICATE ")
    assert "OF ARITY" in line

    parts = line.strip().split()
    symbol = parts[1]
    arity = parts[-1]
    return (symbol, int(arity))

def _readSchemeInfo(lines: list[str]) -> SchemeInfo:
    """
    Read the lines corresponding to a scheme and return the associated SchemeInfo object.
    """
    nameLine = lines[0]
    bodyLine = lines[1]
    patternInfoLines = lines[2:]

    name = nameLine.removeprefix("FORMULA ").replace(" ", "_")
    body = bodyLine.removeprefix("BODY ")

    aritySymbols = [] # Default case if the arities are not specified, in the abscence of dot patterns
    swapValues : Dict[str, str]  = dict() # Matches each swap pattern symbol (like "$f") to the list of concrete symbol that can be put in its place
    swapQuotations : Dict[str, str] = dict() # Matches each swap pattern symbol that is a quotation to the swap pattern symbol it needs to be a quotation of
    distinctPairs : List[Tuple[str,str]] = [] # List of pairs of symbols that should be distinct in every instance of the scheme
    foundASwapPattern = False
    for line in patternInfoLines:
        line = line.strip()
        # If the line is of the form "$f is FUNCTION", it is a swap pattern
        if bool(re.match(r"^DOT_ARITIES(?:\s\$\S+)+$", line)):
            aritySymbols = line.removeprefix("DOT_ARITIES").strip().split(" ")
        elif bool(re.match(r"^RANGE \S+ IN \S+$", line)):
            _, symbol, _, target = line.split(" ")
            foundASwapPattern = True
            assert target in {"BASE_PREDICATE", "BASE_FUNCTION", "ANY_PREDICATE", "ANY_FUNCTION", "QUOTED_VARIABLE"}
            swapValues[symbol] = target
        elif bool(re.match(r"^WITH \S+ QUOTING \S+$", line)):
            _, symbol, _, quotedSymbol = line.split(" ")
            swapQuotations[symbol] = quotedSymbol
        elif bool(re.match(r"^DISTINCT \S+ \S+$", line)):
            _, symbol1, symbol2 = line.split(" ")
            distinctPairs.append((symbol1, symbol2))
        else:
            raise ValueError(f"Invalid line in pattern info: {line}")
    return SchemeInfo(name, body, aritySymbols, swapValues, swapQuotations, foundASwapPattern, distinctPairs)

