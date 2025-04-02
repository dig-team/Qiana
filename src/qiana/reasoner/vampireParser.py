from typing import Tuple, Union, List
import sys

from qiana.interfaceTypes import ReasoningStep

def _parseParentBlock(parentBlock : str) -> Tuple[str,List[str]]:
    """Parses the parent block of a line and returns the name of the transformation and the list of parent ids"""
    if not any(char.isdigit() for char in parentBlock): return parentBlock, []
    if not 1 + parentBlock.find("rectify"): parentBlock, [] # If we find the word rectify in the parent block, the rule is a numbered instance of rectify
    indexLastSpace = parentBlock.rfind(" ")
    transformation, parents = parentBlock[:indexLastSpace], parentBlock[indexLastSpace+1:].split(",")
    return transformation, parents

def _lineTest(line : str) -> Tuple[bool,Union[None,ReasoningStep]]:
    """
    If the text received corresponds to a valid inference line then output
    """
    if line.strip() == "": return False,None
    if line[0] == "%": return False,None
    indexEndOfId = line.find(".")
    indexEndOfText = line.rfind("[")
    id, text, parentBlock = line[:indexEndOfId], line[indexEndOfId+2:indexEndOfText-1], line[indexEndOfText+1:-1]
    transformation, parents = _parseParentBlock(parentBlock)
    if text == "!":
        pass
    return True, ReasoningStep(id,text,transformation, parents)

# OLD LINETEST
# def _lineTest(line):
#     """If it receives a good line output True,parsedLine. Otherwise False,None"""
#     if line == "": return False,None
#     if line[0] == "%": return False,None
#     split1 = line.split(".",1) # Contains the id and the rest of the line
#     id = split1[0]
#     split2 = split1[1].split("[",1) # Splits at the left brace that starts the rule application
#     text = split2[0][1:-1] # Remove spaces at the begining and end of text
#     split3 = split2[1].split(" ") # Contains every word in the rule name and then the parents
#     if not any(char.isdigit() for char in split3[-1]): # The case in which there are no parents, detected by the fact rule names do not contain numbers, contrary to line ids
#         parentIds = []
#         transformation = split3[0][:-1]
#     else:
#         parentIds = split3[-1][:-1].split(",")
#         transformation = " ".join(split3[:-1])
#     return True, _ParsedLine(id,text,transformation,parentIds)

def TPTPOutputParser(text : str) -> List[ReasoningStep]:
    lines = text.split("\n")
    parsedLines = []
    for line in lines:
        goodLine, parsedLine = _lineTest(line)
        if goodLine: parsedLines.append(parsedLine)
    return parsedLines
    
def prettifyer(text, nameDict, inputNameDict):
    """replaces all instances of an interna alias in the output JSON with the stored corresponding full text."""
    text = text.replace("quote","")
    # for extAlias in nameDict.keys(): text = text.replace(nameDict.get(extAlias),inputNameDict.get(extAlias))
    for extAlias in nameDict.keys(): text = text.replace(nameDict.get(extAlias),extAlias)
    return text

# f = open("../../Vampire/testOutput.txt","r")
# print(TPTPOutputParser(f.read()))

