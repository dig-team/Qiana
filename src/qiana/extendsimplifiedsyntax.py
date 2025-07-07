import os

def extend_simplified_syntax(formulas : str) -> str:
    """
    Get as input regular formula bodies separated by dots and not using dots for any other purpose. Returns full TPTP formulas with headers.
    If macros are present they are not yet applied.
    """
    formulas = formulas.replace("\n", " ")
    formulas = formulas.replace(os.linesep, " ")
    result_text = ""
    for iter, formula in enumerate(formulas.split(".")):
        formula = formula.strip()
        if not formula: continue
        result_text += f"fof(input_{str(iter)},axiom,{formula}).\n"
    return result_text.strip("\n")