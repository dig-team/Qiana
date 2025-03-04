from typing import List, Dict, Tuple

import re

from src.qianaExtension.signature import Signature

class SchemeInfo():
    name :str
    body : str
    aritySymbols : List[str]
    symbolTargets : Dict[str,str]
    symbolQuotationMatchings : Dict[str,str]

    def __init__(self, name: str, body: str, aritySymbols: List[str], symbolTargets: Dict[str, str], symbolQuotationMatchings: Dict[str, str]):
        self.name = name
        self.body = body
        self.aritySymbols = aritySymbols
        self.symbolTargets = symbolTargets
        self.symbolQuotationMatchings = symbolQuotationMatchings

    def getBody(self) -> str:
        return self.body

    def getName(self) -> str:
        return self.name

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
           symbolDict[quoting] = Signature.quoteSymbol(symbolDict[quoted]) 
           # symbolDict matches a swap pattern symbol like $f to an actual function symbol like "multiply", symbolQuotationMatchings matches a swap pattern symbol that is a quotation to the swap pattern symbol it needs to be a quotation of (for example matching $qf to $f). So we need to find what the actual symbol associated to $f is, quote it, and then associate that quotation to $qf in symbolDict
        return symbolDict

def getAllSchemeInfos(lines: list[str]) -> Tuple[List[SchemeInfo],Signature]:
    """
    Read all the scheme infos from a list of lines. This returns a list of SchemeInfo objects and a Signature object.
    """
    lines = [line.strip().rstrip("\n\r") for line in lines]
    lines = [line for line in lines if line and line[0] != "#"] # We remove empty lines and comments
    
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
            or line.startswith("WITH ")
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
    nameLine = lines[0]
    bodyLine = lines[1]
    patternInfoLines = lines[2:]

    name = nameLine.removeprefix("FORMULA ").replace(" ", "_")
    body = bodyLine.removeprefix("BODY ")

    aritySymbols = [] # Default case if the arities are not specified, in the abscence of dot patterns
    swapValues : Dict[str, str]  = dict() # Matches each swap pattern symbol (like "$f") to the list of concrete symbol that can be put in its place
    swapQuotations : Dict[str, str] = dict() # Matches each swap pattern symbol that is a quotation to the swap pattern symbol it needs to be a quotation of
    for line in patternInfoLines:
        # If the line is of the form "$f is FUNCTION", it is a swap pattern
        if bool(re.match(r"^DOT_ARITIES(?:\s\$\S+)+$", line)):
            aritySymbols = line.removeprefix("DOT_ARITIES").strip().split(" ")
        elif bool(re.match(r"^RANGE \S+ IN \S+$", line)):
            _, symbol, _, target = line.split(" ")
            assert target in {"BASE_PREDICATE", "BASE_FUNCTION", "ANY_PREDICATE", "ANY_FUNCTION", "QUOTED_VARIABLE"}
            swapValues[symbol] = target
        elif bool(re.match(r"^WITH \S+ QUOTING \S+$", line)):
            _, symbol, _, quotedSymbol = line.split(" ")
            swapQuotations[symbol] = quotedSymbol
    return SchemeInfo(name, body, aritySymbols, swapValues, swapQuotations)
    
