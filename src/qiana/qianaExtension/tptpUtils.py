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

def get_special_functions_arities() -> Dict[str,int]:
    return {"q_Quote" : 1, "q_Neg" : 1, "q_And" : 2, "q_Or" : 2, "q_Forall" : 2}

def get_special_function(symbol_name) -> Dict[str,str]:
    return {
        "q_Quote" : "q_Quote",
        "q_Neg" : "q_Neg",
        "q_And" : "q_And",
        "q_Or" : "q_Or",
        "q_Forall" : "q_Forall"
    }[symbol_name]

def getTruthPredicate() -> str:
    """
    Returns the name of the truth predicate in the signature
    """
    return "q_Truth"


