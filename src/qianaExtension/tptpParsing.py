from typing import List, Dict, Tuple

import re

def parseSymbols(tptp : str) -> Dict[str,Tuple[int, bool]]:
    """
    Parse a tptp formula into a dictionary of symbols to their arity and whether they are functions (if not, it means they are predicats).
    @param tptp: The tptp formula to parse
    #  TODO : exaplain about vars
    """
    return _goThroughStruct(_parseStruct(tptp), False)

def _goThroughStruct(struct : List[str | List], isATerm : bool) -> Dict[str,Tuple[int, bool]]:
    """
    Go through the tree structure of a tptp formula and return a dictionary of symbols to their arity and whether they are functions (if not, it means they are predicats).
    """
    assert isinstance(struct[0], str)
    for element in struct[1:]: assert isinstance(element, list)

    if struct[0] in ["=>", "<=>", "&", "|", "~", "!", "?"]:
        symbols = {}
    else:
        symbols = {struct[0] : (len(struct[1:]), isATerm)}
        isATerm = True
    for element in struct[1:]:
        symbols.update(_goThroughStruct(element, isATerm))
    return symbols

def _parseStruct(tptp : str) -> List[str | List]:
    """
    Parse a tptp formula body into a tree structure on the sole basis of the parentheses and commas
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
            elements.append(_parseStruct(element))
    return elements

def _parseTopLevel(tptp : str) -> List[str]:
    """
    Parse a top level tptp formula into a list of strings, for each toplevel symbol or subterm. 

    Example: "p(f(X1), g(X2))" returns ["p", "f(X1)", "g(X2)"] \n
             "(p(X1)) => (q(X2))") returns ["=>", "(p(X1))", "(q(X2))"]
    """
    assert tptp.count("(")  == tptp.count(")")
    tptp = re.sub(r'\s+', ' ', tptp)
    tptp = _removeTopLevelParenthesis(tptp)

    pattern = re.compile(r'[!\?] ?\[(\w+(?:,\w+)*)\] ?: ?\((.*)\)')
    match = pattern.fullmatch(tptp)
    if match:
        return ["!", match.group(2)] # Remark that we don't bother including the variables in the structure
    
    pattern = re.compile(r'[!\?] ?\[(\w+(?:,\w+)*)\] ?: ?(.*)')
    match = pattern.fullmatch(tptp)
    if match:
        return ["!", match.group(2)]
 
    pattern = re.compile(r'(\w+)\(([\w, \(\)]*)\)')
    match = pattern.fullmatch(tptp)
    if match:
        args = _splitOnCommas(match.group(2))
        return [match.group(1)] + args

    pattern = re.compile(r'(.*) (=>|<=>|&|\|) (.*)')
    match = pattern.fullmatch(tptp)
    if match:
        return [match.group(2), match.group(1), match.group(3)]
    
    pattern = re.compile(r'~(.*)')
    match = pattern.fullmatch(tptp)
    if match:
        return ["~", match.group(1)]
    
    pattern = re.compile(r'\w+')
    match = pattern.fullmatch(tptp)
    if match:
        return [tptp]

    assert False

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
