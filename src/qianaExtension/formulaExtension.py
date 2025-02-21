from typing import List, Tuple, Dict, Set

from itertools import product

from src.qianaExtension.signature import Signature

def getAllSchemesInstances(lines : List[str], signature: Signature = Signature()) -> List[str]:
    """
    Returns all the instances of the formulas defined in the lines parameter, with the patterns defined in the lines parameter applied to them.

    @param lines: List[str] - a list of lines defining the formulas/schemes and the patterns to apply to them
    @param signature: Signature - the signature used with the patterns to obtain the final list of formulas
    @return: List[str] - a list of all the instances of the formulas obtained by applying the patterns in lines, these are complete and valid tptp formulas
    """
    lines = [line.rstrip("\n\r") for line in lines]
    lines = [line for line in lines if line and line[0] != "#"] # We remove empty lines and comments
    
    # We parse the lines that define the signature and extend the signature we received
    def _getSymbolAndArity(line:str) -> Tuple[str, int]:
        _, symbol, arity = line.strip().split(":")
        return symbol, int(arity)
    newLines = []
    for line in lines:
        if line.startswith("FUNCTION "):
            signature.addFunction(_getSymbolAndArity(line))
        elif line.startswith("PREDICATE "):
            signature.addPredicate(_getSymbolAndArity(line))
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
            or line.endswith("FUNCTION") \
            or line.endswith("PREDICATE") \
            or line.startswith("ARITIES ")
        if line.startswith("FORMULA "):
            formulaNames.append(line.removeprefix("FORMULA "))
            patternInfos.append([])
            index += 1
        elif line.startswith("BODY "):
            formulas.append(line.removeprefix("BODY "))
        else:
            patternInfos[index].append(line)
        
    assert len(formulas) == len(formulaNames) == len(patternInfos)
    instances = []
    for i, formula in enumerate(formulas):
        instances.extend(getAllInstancesOfFormula(formulaNames[i], formula, patternInfos[i], signature))
    return instances

def getAllInstancesOfFormula(name: str, formula: str, patternInfo : List[str], signature : Signature) -> List[str]:
    """
    Parse the lines of pattern info to have the necessary information to apply the macro patterns and returns all formula instances this generates.

    @param formula: str - a formula body in tptp format with macro patterns
    @param patternInfo: List[str] - a list of patterns to apply to the formula
    @return: List[str] - a list of all the instances of the formula obtained by applying the patterns in patternInfo, these are complete and valid tptp formulas
    """
    aritySymbols = [] # Default case if the arities are not specified, in the abscence of dot patterns
    swapValues : Dict[str, List[str]]  = dict() # Matches each swap pattern symbol (like "$f") to the list of concrete symbol that can be put in its place
    for line in patternInfo:
        line = line.strip()
        # If the line starts with a # it is a comment
        if line[0] == "#":
            pass
        # If the line is of the form "$f is FUNCTION", it is a swap pattern
        elif line[0] == "$":
            symbol = line.split(" ")[0]
            if line.endswith("FUNCTION"):
                swapValues[symbol] = signature.getAllFunctions()
            elif line.endswith("PREDICATE"):
                swapValues[symbol] = signature.getAllPredicates()
            else:
                raise ValueError("Invalid pattern type in patternInfo")
        # If the line is of the form "ARITIES: $f, $g" it is the list of arities for the dot patterns
        elif line.startswith("ARITIES"):
            line = line.removeprefix("ARITIES").strip().replace(" ", "")
            aritySymbols = line.split(",")

    formulas = []
    valueCombinations = product(*swapValues.values())
    for combi in valueCombinations:
        swapPatterns = dict(zip(swapValues.keys(), combi))
        arities = [int(symbol) if symbol.isdigit() else signature.getArity(swapPatterns[symbol]) for symbol in aritySymbols]
        newFormula = applyAllPatternsOneInstance(formula, arities, swapPatterns)
        newFormula = "fof(" + name + "_".join(combi) + "," + newFormula + ")."
        formulas.append(newFormula)
    
    # If valueCombinations is empty, we still need to apply the patterns with no swap values
    if not valueCombinations:
        for symbol in aritySymbols : assert symbol.isdigit()
        arities = [int(symbol) for symbol in aritySymbols]
        formula = applyAllPatternsOneInstance(formula, arities, dict())
        formula = "fof(" + name + "," + formula + ")."
        formulas = [formula]

    return formulas

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
    Returns the index of the first dots in formula paired with the separation symbol. Only works for 3 dots with the same separation symbol at each end, the symbol is one char.
    
    @param formula: str - a formula body in tptp format with macro patterns
    @return: Tuple[int, str] | None - The index of the first dots in formula paired with the separation symbol they use or None if there is no dot pattern
    """
    for i in range(len(formula) - 2):
        if formula[i] == "." and formula[i + 1] == "." and formula[i + 2] == ".":
            assert formula[i - 1] == formula[i + 3] # check if both ends of the dots have matching separation symbol
            assert formula[i - 1] in [",", "&", "|", "=>", "<=>"] # check if the separation symbol is valid
            return i-1, formula[i - 1]
    return None

def findOperands(formula: str, index: int) -> Tuple[str, str, int, int]:
    """
    Returns the two operands of a series of dots in formula

    @param formula: str - a formula body in tptp format with macro patterns
    @param index: int - the index of the first dot of the symbol to the left of the dots
    @return: Tuple[str, str, int, int] - the two operands of the dot in formula, and the indexes delimiting the range of the operand+3 dots pattern
    """
    
    leftStartingIndex = index-1
    while formula[leftStartingIndex] == " ": leftStartingIndex -= 1
    rightStartingIndex = index+5
    while formula[rightStartingIndex] == " ": rightStartingIndex += 1

    # Yes the code bellow can be rewritten in a handful of lines with a for loop and a break, and yes it would avoid the code reuse. Don't.

    iterIndexLeft = leftStartingIndex
    parenthesisCount = 0
    while formula[iterIndexLeft] not in ["(", ",", " "] or parenthesisCount != 0:
        if formula[iterIndexLeft] == ")":
            parenthesisCount += 1
        elif formula[iterIndexLeft] == "(":
            parenthesisCount -= 1
        iterIndexLeft -= 1
        assert iterIndexLeft >= 0
    leftOperand = formula[iterIndexLeft+1:leftStartingIndex+1]
    
    iterIndexRight = rightStartingIndex
    parenthesisCount = 0
    while formula[iterIndexRight] not in [")", ",", " "] or parenthesisCount != 0:
        if formula[iterIndexRight] == ")":
            parenthesisCount += 1
        elif formula[iterIndexRight] == "(":
            parenthesisCount -= 1
        iterIndexRight += 1
        assert iterIndexRight < len(formula)
    rightOperand = formula[rightStartingIndex:iterIndexRight]

    return leftOperand, rightOperand, iterIndexLeft+1, iterIndexRight-1

def injectInDifference(firstOperand: str, secondOperand: str, symbolToInject: str) -> str:
    """
    Finds the difference between two operands (strings that are almost identical except for a counting symbol, such as "t1" and "tn") and injects a symbol in the difference. For example returning "t2".

    @param firstOperand: str - the first operand
    @param secondOperand: str - the second operand
    @param symbolToInject: str - the symbol to inject in the difference of the operands
    @return: str - the difference between the two operands with the symbol put in the place of the difference
    """
    assert firstOperand != secondOperand
    if len(firstOperand) < len(secondOperand): firstOperand, secondOperand = secondOperand, firstOperand
    for (i, k) in enumerate(firstOperand):
        if k != secondOperand[i]:
            indexLeft = i
            break
    reversedFirstOperad = firstOperand[::-1]
    reversedSecondOperad = secondOperand[::-1]
    for (i, k) in enumerate(reversedFirstOperad):
        if k != reversedSecondOperad[i]:
            indexRight = len(firstOperand) - i - 1
            break
    return firstOperand[:indexLeft] + symbolToInject + firstOperand[indexRight+1:]

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