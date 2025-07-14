from typing import List, Dict, Tuple

import re

def parseSymbols(tptp : str) -> Dict[str,Tuple[int, bool]]:
    """
    Parse a tptp formula into a dictionary of symbols to their arity and whether they are functions (if not, it means they are predicats). Note that variables are included in the output as functions and need to be filtered out if necessary.
    @param tptp: The tptp formula to parse
    """
    return _goThroughStruct(parseStruct(tptp), False)

def _goThroughStruct(struct : List[str | List], isATerm : bool) -> Dict[str,Tuple[int, bool]]:
    """
    Go through the tree structure of a tptp formula and return a dictionary of symbols to their arity and whether they are functions (if not, it means they are predicats).
    """
    assert isinstance(struct[0], str)
    for element in struct[1:]: assert isinstance(element, list)

    if struct[0] in ["=>", "<=>", "&", "|", "~", "!", "?"]:
        symbols = {}
    elif struct[0] in [",", "="]:
        symbols = {}
        isATerm = True 
    else:
        symbols = {struct[0] : (len(struct[1:]), isATerm)}
        isATerm = True
    for element in struct[1:]:
        symbols.update(_goThroughStruct(element, isATerm))
    return symbols

def parseStruct(tptp : str) -> List[str | List]:
    """
    Derive the syntactic tree of a tptp formula. The first element of the list is the top level symbol, the rest are its arguments, which can be either symbols or sub-structures.
    Example : "![X] : (p(X) => q(X,X))" returns ["!", ["X"], ["=>", ["p", ["X"]], ["q", ["X", "X"]]]]
    """
    topLevel : List = _parseTopLevel(tptp)
    symbol, args = topLevel[0], topLevel[1:]
    elements = [symbol]
    for element in args:
        pattern = re.compile(r'\w+')
        match = pattern.fullmatch(element)
        if match:
            elements.append([element])
        else:
            elements.append(parseStruct(element))
    return elements

def _parseTopLevel(tptp : str) -> List[str]:

    """
    Parse a top level tptp formula into a list of strings, for each toplevel symbol or subterm. 

    Example: "p(f(X1), g(X2))" returns ["p", "f(X1)", "g(X2)"] 
             "(p(X1)) => (q(X2))") returns ["=>", "(p(X1))", "(q(X2))"]
    """
    assert tptp.count("(")  == tptp.count(")")
    tptp = re.sub(r'\s+', ' ', tptp)
    tptp = _removeTopLevelParenthesis(tptp)

    pattern = re.compile(r'([!\?]) ?\[(\w+(?:,\w+)*)\] ?: ?\((.*)\)')
    match = pattern.fullmatch(tptp)
    if match:
        return [match.group(1), match.group(2), match.group(3)] 
    
    pattern = re.compile(r'([!\?]) ?\[(\w+(?:,\w+)*)\] ?: ?(.*)')
    match = pattern.fullmatch(tptp)
    if match:
        return [match.group(1), match.group(2), match.group(3)] 
 
    pattern = re.compile(r'(\w+)\(([\w, \(\)]*)\)')
    match = pattern.fullmatch(tptp)
    if match:
        args = _splitOnCommas(match.group(2))
        return [match.group(1)] + args

    # Find binary operators (<=>, =>, &, |, =) at the top level; need a helper function to check for balanced parentheses
    match = _findBalancedBinaryOperator(tptp)
    if match:
        left_part, operator, right_part = match
        return [operator, left_part, right_part]
    # pattern = re.compile(r'(.*) (=>|<=>|=|&|\|) (.*)')
    # match = pattern.fullmatch(tptp)
    # if match:
    #     return [match.group(2), match.group(1), match.group(3)]
    
    pattern = re.compile(r'~(.*)')
    match = pattern.fullmatch(tptp)
    if match:
        return ["~", match.group(1)]
    
    pattern = re.compile(r'\w+')
    match = pattern.fullmatch(tptp)
    if match:
        return [tptp]

    pattern = re.compile(r'[A-Z]\w*(?:,[A-Z]\w*)*')
    match = pattern.fullmatch(tptp)
    if match:
        if "," in tptp:
            return [","] + [var.strip() for var in tptp.split(",")]
        else:
            return [tptp.strip()]

    assert False

def _findBalancedBinaryOperator(tptp: str) -> Tuple[str, str, str] | None:
    """
    Find a binary operator (=>, <=>, =, &, |) that is at the top level (not inside parentheses).
    Returns (left_part, operator, right_part) if found, None otherwise.
    """
    operators = ["<=>", "=>", "=", "&", "|"]  # Order matters: check longer operators first
    
    parenthesis_depth = 0
    for i, char in enumerate(tptp):
        if char == "(":
            parenthesis_depth += 1
        elif char == ")":
            parenthesis_depth -= 1
        elif parenthesis_depth == 0:
            # Check all operators at this position
            for op in operators:
                if (i + len(op) <= len(tptp) and tptp[i:i+len(op)] == op):
                    # Check if it's not part of a larger alphanumeric token
                    left_ok = i == 0 or not tptp[i-1].isalnum()
                    right_ok = i+len(op) == len(tptp) or not tptp[i+len(op)].isalnum()
                    if left_ok and right_ok:
                        left_part = tptp[:i].strip()
                        right_part = tptp[i+len(op):].strip()
                        return (left_part, op, right_part)
    
    return None

def _splitOnCommas(tptp : str) -> List[str]:
    """
    Take the list of arguments of a function or predicate and split it into a list of strings.
    Example: f(a,b),g(c) => ["f(a,b)", "g(c)"]
    """
    splittingIndexes = []
    parenthesisDepth = 0
    for index, c in enumerate(tptp):
        if c == "(":
            parenthesisDepth += 1
        if c == ")":
            parenthesisDepth -= 1
        if c == "," and parenthesisDepth == 0 :
            splittingIndexes.append(index)
    splittingIndexes = [-1] + splittingIndexes + [len(tptp)]
    values = [tptp[splittingIndexes[i]+1:splittingIndexes[i+1]] for i in range(len(splittingIndexes)-1)]
    return [val.strip() for val in values]

def _removeTopLevelParenthesis(tptp : str) -> str:
    """
    If the tptp formula has matching outer parenthesis, remove them. Do so as many times as necessary.
    """
    tptp = tptp.strip()

    hasOuterParenthesis = True
    while tptp[0] == "(" and tptp[-1] == ")" and hasOuterParenthesis:
        parenthesisDepth = 0
        for c in tptp[:-1]:
            if c == "(":
                parenthesisDepth += 1
            if c == ")":
                parenthesisDepth -= 1
            if parenthesisDepth == 0: 
                hasOuterParenthesis = False
                break
        if hasOuterParenthesis:
            tptp = tptp[1:-1].strip()
    return tptp
