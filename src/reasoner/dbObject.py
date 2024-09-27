from typing import Dict, List
import reasoner.solverCaller as solver

import reasoner.inputParser
from reasoner.formulas import Atomic, Belief, Believer, Disjunction, Negation
from reasoner.vampireParser import TPTPOutputParser as oparse
from reasoner.vampireParser import prettifyer as pretty

class DbObject:
    def __init__(self) -> None:
        """Creates an empty database. There is no way to create a nonempty database. Instead, the database should be filled through calls to the "update" methode."""
        self.formulaList = list()
        self.inputNameDict = dict() # Links external aliases to full text
        self.nameDict = dict() # Links external aliases to internal aliases
        self.nameCounter = 1  # Created for the lazy implementation of legalizeName

    def update(self, input_json: Dict[str, List]) -> None:
        reasoner.inputParser.update(self,input_json)

    def addFormula(self, formula):
        self.formulaList.append(formula)

    def addFormulas(self, FormuList):
        for formula in FormuList:
            self.addFormula(formula)

    def legalizeName(self, name, type="ap"):
        """Turns a name into a corresponding legal name. This implies both to make sure neither the use of the name nor of its quotation can create a collision and that the name is not a restricted keyword."""
        # The easiest way to implement this function is to create pure new names. It is important to do this via a function to allow for better names if we wish.
        # The suggested types are "ap" for "atomic proposition" and "bo" for "believer object"
        if name in self.nameDict.keys():
            return self.nameDict.get(name)
        self.nameCounter += 1
        newName = type + str(self.nameCounter) + "EOT" # EOT stands for End Of Token. It ensures that no token is a prefix of another, assuming all types are two characters long.
        self.nameDict.update({name: newName})
        return newName

    def testCoherence(self):
        """A first solver call function to test whether the list of formulas at hand is coherent."""
        return solver.testCoherence(self.formulaList)

    def fullCallVampire(self):
        return pretty(oparse(solver.fullCallVampire(self.formulaList)),self.nameDict,self.inputNameDict)
