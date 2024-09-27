from typing import List

class ReasoningStep():
    def __init__(self, id : str, text : str, transformation : str, Parents : List[str]):
        self.id = id
        self.text = text
        self.transformation = transformation
        self.Parents = Parents

    def toJson(self):
        return  "{" + \
        "\"id\":\"" + self.id + "\"," +\
        "\"text\":\"" + self.text + "\"," +\
        "\"parents\":[" + ",".join(["\"" + parentID + "\"" for parentID in self.Parents]) + "]," +\
        "\"deductionMethode\":\"" + self.transformation + "\"" +\
        "}"

    def __str__(self):
        return self.id + ". " + self.text + " [" + self.transformation + " " + ",".join(self.Parents) + "]"
    
    def GetJsonFile(steps : List["ReasoningStep"]):
        if len(steps) == 0: return "{ \"NodeList\":[],\n \"finalNode\":\"\"}"
        return "{ \"NodeList\":[" + ",\n".join([rs.toJson() for rs in steps]) +\
            "],\n" +\
            "\"finalNode\":\"" + steps[-1].id + "\"" +\
            "}"