from typing import Dict, List

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

def next_quoted_var(qvars: List[str], nbr_vars : int = 1) -> List[str] | str:
    """
    Receives a list of quoted variables and generates a new one that does not exist in the list.
    If nbr_vars is specified and different from 1, it will return nbr_vars new variables instead (and therefore the output will be a list).
    This functions has determinist output and behaves as though there was a fixed infinite list of quoted vars.
    """
    if nbr_vars < 0: raise ValueError("nbr_vars must be non-negative")
    if nbr_vars == 0 : return []
    if nbr_vars == 1: return "q_X" + str(len(qvars) + 1)
    return ["q_X" + str(i) for i in range(len(qvars) + 1, len(qvars) + nbr_vars + 1)]
