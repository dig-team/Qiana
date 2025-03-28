from typing import List, Tuple, Dict, Set

from itertools import product

from qianaExtension.signature import Signature
from qianaExtension.patternParsing import SchemeInfo, getAllSchemeInfos

def getAllSchemesInstances(lines : List[str], signature: Signature = None) -> List[str]:
    """
    Returns all the instances of the formulas defined in the lines parameter, with the patterns defined in the lines parameter applied to them.

    @param lines: List[str] - a list of lines defining the formulas/schemes and the patterns to apply to them
    @param signature: Signature - the signature used with the patterns to obtain the final list of formulas
    @return: List[str] - a list of all the instances of the formulas obtained by applying the patterns in lines, these are complete and valid tptp formulas
    """
    signature = signature if signature else Signature()
    schemeInfos, signature = getAllSchemeInfos(lines)
    instances = []
    for schemeInfo in schemeInfos:
        instances.extend(getAllInstancesOfFormula(schemeInfo, signature))
    return instances

def getAllInstancesOfFormula(schemeInfo : SchemeInfo, signature : Signature) -> List[str]:
    """
    Parse the lines of pattern info to have the necessary information to apply the macro patterns and returns all formula instances this generates.

    @param formula: str - a formula body in tptp format with macro patterns
    @param patternInfo: List[str] - a list of patterns to apply to the formula
    @return: List[str] - a list of all the instances of the formula obtained by applying the patterns in patternInfo, these are complete and valid tptp formulas
    """

    swapValues : Dict[str, List[str]] = dict()  # Matches each swap pattern symbol to the list of concrete symbols
    
    # Process symbol targets from SchemeInfo
    for symbol, target in schemeInfo.getSymbolTargets().items():
        if target == "BASE_PREDICATE":
            swapValues[symbol] = signature.getBasePredicates()
        elif target == "BASE_FUNCTION":
            swapValues[symbol] = signature.getBaseFunctions()
        elif target == "ANY_PREDICATE":
            swapValues[symbol] = signature.getAllPredicates()
        elif target == "ANY_FUNCTION":
            swapValues[symbol] = signature.getAllFunctions()
        elif target == "QUOTED_VARIABLE":
            swapValues[symbol] = signature.getQuotedVars()
        else:
            raise ValueError(f"Unknown target type: {target}")
        
    # Obtain a list of dicts, each corresponding to one possible mapping of swap pattern symbols to the appropriate concrete symbols
    allCombinations : List[Dict[str,str]] = [dict(zip(swapValues.keys(), combi)) for combi in product(*swapValues.values())]
    allCombinations = [schemeInfo.enrichSymbolDict(case) for case in allCombinations]
    allCombinations = [case for case in allCombinations if _respectDistinctPairs(case, schemeInfo.getDistinctPairs())] 

    formulas = []
    if not allCombinations and not schemeInfo.containsSwapPatterns(): allCombinations = [dict()] # If there is no swap pattern we still need to generate a formula. However if there is no valid combaination but there is a swap pattern, we generate nothing at all
    for case in allCombinations:
        arities = [signature.getArity(case[symbol]) for symbol in schemeInfo.getAritySymbols()]
        schemeBody = schemeInfo.getBody()
        schemeBody = applyAllPatternsOneInstance(schemeBody, arities, case)
        schemeBody = "fof(" + schemeInfo.getName() + "_" + "_".join(case.values()) + "axiom,axiom," + schemeBody + ")."
        formulas.append(schemeBody)
    return formulas

def _respectDistinctPairs(case: Dict[str, str], distinctPairs: List[Tuple[str, str]]) -> bool:
    """
    Returns True if the case respects all the distinct pairs, False otherwise

    @param case: Dict[str, str] - a mapping of swap pattern symbols to the concrete symbols they are replaced by
    @param distinctPairs: List[Tuple[str, str]] - a list of pairs of symbols that should be distinct in every instance of the scheme
    @return: bool - True if the case respects all the distinct pairs, False otherwise
    """
    for (symbol1, symbol2) in distinctPairs:
        assert symbol1.startswith("$")
        if symbol2.startswith("$") : target = case[symbol2]
        else: target = symbol2
        if case[symbol1] == target:
            return False
    return True

def applyAllPatternsOneInstance(formula: str, arities: List[int], swapPatterns: Dict[str, str]) -> str:
    """
    Applies all the patterns to obtain one instance of the formula with all macro-patterns expanded
    """
    formula = replaceAllDotPatterns(formula, arities) #We do the dot patterns first to put swappable symbols in dot patterns. The converse would make no sense, so we lose nothing with this ordering.
    formula = replaceAllSwapPatterns(formula, swapPatterns)
    return formula

def replaceAllSwapPatterns(formula: str, swapPatterns: Dict[str, str]) -> str:
    """
    @param formula: str - a formula body in tptp format with macro patterns
    @param swapPatterns: List[Tuple[str, str]] - a list of pairs of symbols to replace, the first element of the pair is the symbol to replace, the second is the symbol to replace it with
    @return: str - the formula with all instances of the first element of each pair replaced by the second element
    """
    for (targetSymbol, newSymbol) in swapPatterns.items():
        assert targetSymbol[0] == "$"
        formula = formula.replace(targetSymbol, newSymbol)
    return formula


def findDots(formula: str) -> Tuple[int, str] | None:
    """
    Find the leftmost pattern of three dots surrounded by the same symbol on each side.
    Returns the index of the symbol to the left of these dots paired with the separation symbol. Only works for 3 dots with the same separation symbol at each end, the symbol is one char.
    
    @param formula: str - a formula body in tptp format with macro patterns
    @return: Tuple[int, str] | None - The index of the symbol to the left of the leftmost 3 dots in formula paired with the separation symbol they use or None if there is no dot pattern
    """
    for i in range(len(formula) - 2):
        if formula[i] == "." and formula[i + 1] == "." and formula[i + 2] == ".":
            assert formula[i - 1] == formula[i + 3] # check if both ends of the dots have matching separation symbol
            assert formula[i - 1] in [",", "&", "|"] # check if the separation symbol is valid
            return i-1, formula[i - 1]
    return None

def findOperands(formula: str, index: int) -> Tuple[str, str, int, int]:
    """
    Returns the two operands of a series of dots in formula

    @param formula: str - a formula body in tptp format with macro patterns
    @param index: int - the index of the symbol to the left of the dot pattern
    @return: Tuple[str, str, int, int] - the two operands of the dot in formula, and the indexes delimiting the range of the operand+3 dots pattern
    """
    leftStartingIndex = index-1
    while formula[leftStartingIndex] == " ": leftStartingIndex -= 1
    rightStartingIndex = index+5
    while formula[rightStartingIndex] == " ": rightStartingIndex += 1

    # Yes the code bellow can be rewritten in a handful of lines with a for loop and a break, and yes it would avoid the code reuse. Don't.

    iterIndexLeft = leftStartingIndex
    parenthesisCount = 0
    while formula[iterIndexLeft] not in ["(", "[", ",",":"] or parenthesisCount != 0:
        if formula[iterIndexLeft] == ")":
            parenthesisCount += 1
        elif formula[iterIndexLeft] == "(":
            parenthesisCount -= 1
        iterIndexLeft -= 1
        if iterIndexLeft < 0: 
            assert(iterIndexLeft == -1)
            break
    leftOperand = formula[iterIndexLeft+1:leftStartingIndex+1]
    
    iterIndexRight = rightStartingIndex
    parenthesisCount = 0
    while formula[iterIndexRight] not in [")", "]", ",", ":"] or parenthesisCount != 0:
        if formula[iterIndexRight] == ")":
            parenthesisCount += 1
        elif formula[iterIndexRight] == "(":
            parenthesisCount -= 1
        iterIndexRight += 1
        if iterIndexRight >= len(formula):
            assert(iterIndexRight == len(formula))
            break
    rightOperand = formula[rightStartingIndex:iterIndexRight]

    return leftOperand.strip(), rightOperand.strip(), iterIndexLeft+1, iterIndexRight-1

def injectInDifference(firstOperand: str, secondOperand: str, symbolToInject: str) -> str:
    """
    Receive two operands that are almost identical except for a counting symbol that is "1" in the first operand and "#" in the second operand.
    Injects a sumbol in the difference between the two operands.

    @param firstOperand: str - the first operand
    @param secondOperand: str - the second operand
    @param symbolToInject: str - the symbol to inject in the difference of the operands
    @return: str - the difference between the two operands with the symbol put in the place of the difference
    """
    assert secondOperand.replace("#","1") == firstOperand
    return secondOperand.replace("#", symbolToInject)

def replaceDotPattern(formula: str, leftOfPattern: int, rightOfPattern: int, separationSymbol: str, leftOperand:str, rightOperand: str, arity: int):
    """
    Replaces a series of dots in formula with the appropriate number of separation symbols

    @param formula: str - a formula body in tptp format with macro patterns
    @param leftOfPattern: int - the index of the symbol to the left of the operand to the left of the dots
    @param rightOfPattern: int - the index of the symbol to the right of the operand to the right of the dots
    @param separationSymbol: str - the symbol used to separate the operands
    @param leftOperand: str - the left operand of the dots
    @param rightOperand: str - the right operand of the dots
    @param arity: int - the number of operands to insert in the series
    @return: str - the formula with the dot pattern replaced by the separation symbol and repeated operands
    """
    replaced = separationSymbol.join([injectInDifference(leftOperand, rightOperand, str(i)) for i in range(1, arity+1)])
    return formula[:leftOfPattern] + replaced + formula[rightOfPattern+1:]

def replaceAllDotPatterns(formula: str, arities: List[int]) -> str:
    """
    Replaces all dot patterns in formula with the appropriate number of separation symbols

    @param formula: str - a formula body in tptp format with macro patterns
    @param arities: List[int] - the arities of the functions in the formula
    @return: str - the formula with all dot patterns replaced by the separation symbol and repeated operands
    Example: replaceAllDotPatterns("(wff(t1) &...& wff(tn) => wff(f(t1,...,tn)))", [2, 2]) -> "(wff(t1) & wff(t2) => wff(f(t1,t2))"
    """
    for arity in arities:
        assert findDots(formula) is not None
        dotIndex, seprationSymbol = findDots(formula)
        leftOperand, rightOperand, leftIndex, rightIndex = findOperands(formula, dotIndex)
        formula = replaceDotPattern(formula, leftIndex, rightIndex, seprationSymbol, leftOperand, rightOperand, arity)
    return formula

if __name__ == "__main__":
    formula = "(wff(t1) &...& wff(tn) => wff(f(t1,...,tn)))"
    # n =arity of f
    print(replaceAllDotPatterns(formula, [2, 2])) # "(wff(t1) & wff(t2) => wff(f(t1,t2))"

    print(injectInDifference("t1", "t2", "n")) # "tn"

    with open("examples/exampleSchemes.schemes", "r") as f:
        schemes = f.readlines()
    print(getAllSchemesInstances(schemes, Signature(functions={"f": 2, "g": 1}, predicates={"wff": 1}, constants={"c"})))