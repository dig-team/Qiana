from typing import List, Callable, Tuple
from enum import Enum, auto
import re

class SchemeFactory():
    """
    A purely static utility class providing utility functions to generate schemes.
    For use in schemes generation, this serves the same function as the "extand" method of the Formula type but is more general.
    However the schemes it creates are more complex and less readable than those created by the "extand" method, so it is not recommended to use this class for schemes that can be created with "extand".
    """

    @staticmethod
    def generateInstance(schemeText : str, maxIndices : List[int]):
        """
        @param schemeText: the text of the scheme. This is a formula using macros following the "\!" escape character. 
        a \!^ b is a macro for qAnd(a,b) and \![f(t_$);,] stands for f(t_1), ..., f(t_n); where n is given by the second argument of this function.
        @param maxIndices: a list of integers, the i-th integer is the maximum value of indices for the i-th use of the \![prefix;sep] macro
        """
        pass

    @staticmethod
    def _expandSimpleMacros(schemeText : str) -> str:
        """
        A simple utility function to expand macros of the form a \!^ b 
        """
        patternqAnd = re.compile(r"([[^(), ]+|\(.*\)]) *\\!\^ *([[^(), ]+|\(.*\)])")
        m = patternqAnd.search(schemeText)
        while m:
            schemeText = patternqAnd.sub(r"qAnd(\1,\2)", schemeText)
            m = patternqAnd.search(schemeText)
        return schemeText

    class ExtensionModes(Enum):
        predicateAND = auto()
        argumentList = auto()

    @staticmethod
    def generateSchemeInstance(schemeInstanceFromTexts : Callable[[Tuple[str, ...]],str], indicesToStrings : List[Callable[[int],str]], maxIndices : List[int], modes : List[ExtensionModes]) -> str:
        """
        @param schemeInstanceFromText: a function that takes a number l of string arguments and return the text of an instance of a scheme, ready to be parsed
        @param indicesToStrings: a list of l functions that take an index and return a string; each either a function argument or a predicate application (l is the same as in scheemInstanceFromText)
        @param maxIndices: a list of l integers, the i-th integer is the maximum value of indices in the text for the i-th argument of schemeInstanceFromText
        @param modes: a list of l ExtensionModes, indicating for every element of indicesToStrings whether to extend it as a conjuntion or as a list of arguments
        @return: the text of the scheme instance
        """
        assert len(indicesToStrings) == len(maxIndices) == len(modes)
        return schemeInstanceFromTexts(*[SchemeFactory._argumentRepetition(indicesToStrings[i], maxIndices[i], modes[i]) for i,_ in enumerate(indicesToStrings)])

    @staticmethod
    def _argumentRepetition(indiceToArgument: Callable[[int],str], maxIndice: int, mode : ExtensionModes) -> str:
        if mode == SchemeFactory.ExtensionModes.predicateAND:
            return " & ".join([indiceToArgument(i) for i in range(maxIndice)])
        if mode == SchemeFactory.ExtensionModes.argumentList:
            return ", ".join([indiceToArgument(i) for i in range(maxIndice)])
        raise ValueError("Unknown mode")

