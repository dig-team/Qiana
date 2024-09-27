import sys

class _ParsedLine():
    def __init__(self, id, text, transformation, Parents):
        self.id = id
        self.text = text
        self.transformation = transformation
        self.Parents = Parents

    def toJson(self):
        a =  "{" + \
        "\"id\":\"" + self.id + "\"," +\
        "\"text\":\"" + self.text + "\"," +\
        "\"parents\":[" + ",".join(["\"" + parentID + "\"" for parentID in self.Parents]) + "]," +\
        "\"deductionMethode\":\"" + self.transformation + "\"" +\
        "}"
        return a

def _lineTest(line):
    """If it receives a good line output True,parsedLine. Otherwise False,None"""
    if line == "": return False,None
    if line[0] == "%": return False,None
    split1 = line.split(".",1) # Contains the id and the rest of the line
    id = split1[0]
    split2 = split1[1].split("[",1) # Splits at the left brace that starts the rule application
    text = split2[0][1:-1] # Remove spaces at the begining and end of text
    split3 = split2[1].split(" ") # Contains every word in the rule name and then the parents
    if not any(char.isdigit() for char in split3[-1]): # The case in which there are no parents, detected by the fact rule names do not contain numbers, contrary to line ids
        parentIds = []
        transformation = split3[0][:-1]
    else:
        parentIds = split3[-1][:-1].split(",")
        transformation = " ".join(split3[:-1])
    return True, _ParsedLine(id,text,transformation,parentIds)

def TPTPOutputParser(text):
    lines = text.split("\n")
    parsedLines = []
    for line in lines:
        goodLine, parsedLine = _lineTest(line)
        if goodLine: parsedLines.append(parsedLine)
    if len(parsedLines) == 0: return "{ \"NodeList\":[],\n \"finalNode\":\"\"}" #Handles the case in which there is no useful output. This implies no contradiction was detected.
    return "{ \"NodeList\":[" + ",\n".join([pl.toJson() for pl in parsedLines]) +\
    "],\n" +\
    "\"finalNode\":\"" + parsedLines[-1].id + "\"" +\
    "}"

def prettifyer(text, nameDict, inputNameDict):
    """replaces all instances of an interna alias in the output JSON with the stored corresponding full text."""
    text = text.replace("quote","")
    # for extAlias in nameDict.keys(): text = text.replace(nameDict.get(extAlias),inputNameDict.get(extAlias))
    for extAlias in nameDict.keys(): text = text.replace(nameDict.get(extAlias),extAlias)
    return text

# f = open("../../Vampire/testOutput.txt","r")
# print(TPTPOutputParser(f.read()))

