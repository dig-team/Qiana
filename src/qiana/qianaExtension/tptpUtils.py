from typing import Dict

def quoteSymbol(symbol: str) -> str:
    return f"q_{symbol}"

def unquoteSymbol(symbol: str) -> str | None:
    """
    Unquotes a symbol if it is quoted, otherwise returns None
    """
    if symbol.startswith("q_"): return symbol[2:]
    return None

def isQuoted(symbol: str) -> bool:
    return symbol.startswith("q_")

def getSpecialFunctions() -> Dict[str,int]:
    return {"q_Quote" : 1, "q_Neg" : 1, "q_And" : 2, "q_Or" : 2, "q_Forall" : 2}

def getTruthPredicate() -> str:
    """
    Returns the name of the truth predicate in the signature
    """
    return "q_Truth"