"""   Qiana Formulas

Internal representation of formulas
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import List, Dict, Iterable, Set

class Formula:
    """Represents a formula of an operator and constituent formulas"""

    ###########################################################################
    #   Convenience functions and objects
    ###########################################################################

    IMPLIES = "=>"
    AND = "&"
    OR = "|"
    NOT = "~"
    EQV = "<=>"
    FORALL = "forall"
    OPERATORS = {
        IMPLIES: "q_Implies",
        AND: "q_And",
        OR: "q_Or",
        NOT: "q_Not",
        FORALL: "q_Forall",
    }

    @staticmethod
    def isQuoted(s: str) -> bool:
        """TRUE if the symbol is quoted"""
        return s.startswith("q_")

    @staticmethod
    def isVariable(s: str) -> bool:
        """Heuristically finds variables"""
        return not Formula.isQuoted(s) and (len(s) < 3 or s.endswith("_AND") or s.endswith("_TERM"))


    @staticmethod
    def isIdentifier(c: str) -> bool:
        """True if this character is a valid identifier character"""
        return c == "_" or c.isalnum()

    @staticmethod
    def checkIdentifier(predicate: str):
        """Passes if all characters are valid identifier characters"""
        if not all(Formula.isIdentifier(p) for p in predicate):
            raise Exception(f"Expected identifier, not {predicate}")

    @staticmethod
    def quoteStr(s: str) -> str:
        """Quotes a logical operator, predicate, or function, unless it is already quoted"""
        if s.startswith("q_"):
            return s
        return Formula.OPERATORS.get(s, "q_" + s)
    
    @staticmethod
    def unquoteStr(s : str) -> str:
        """Unquotes a logical symbol, predicate, or function, if the symbol is not quoted, raise an error"""
        if s.startswith("q_"):
            return s[2:]
        raise Exception(f"Expected quoted string, not {s}")

    @staticmethod
    def isQuotedVariable(s: str) -> bool:
        """TRUE for quoted variables"""
        return s.startswith("q_") and Formula.isVariable(s[2:])

    ###########################################################################
    #   Formula objects
    ###########################################################################

    def __init__(self, operator: str, *args: Formula) -> None:
        self.operator = operator
        for a in args:
            if not isinstance(a, Formula):
                raise Exception(
                    f"Formula arguments must be formulas, not {a} of type {type(a)}"
                )
        self.args = args

    def quote(self) -> Term:
        """Quotes the formula except variables"""
        return Term(Formula.quoteStr(self.operator), *[a.quote() for a in self.args])

    def instantiate(self, instantiation: Mapping[Variable, Term]) -> Formula:
        """Instantiates the formula with variables. Not needed, just for future use."""
        return Formula(
            self.operator, *[a.instantiate(instantiation) for a in self.args]
        )

    def setType(self, type: str):
        """Sets the type of the formula"""
        self.type = type

    def __str__(self) -> str:
        if self.operator == Formula.NOT:
            return "~" + str(self.args[0])
        return "(" + (" " + self.operator + " ").join([str(a) for a in self.args]) + ")"

    def expand(self, n: int) -> Formula:
        """Expands any meta-variables from x_1...x_n"""
        return Formula(self.operator, *[a.expand(n) for a in self.args])

    def getComponents(
        self,
        predicates: Mapping[str, int],
        functions: Mapping[str, int],
    ):
        """Fills up the predicates with their arities, the variables, and the functions with their arities"""
        for a in self.args:
            a.getComponents(predicates, functions)


class Forall(Formula):
    """Represents a quantified formula"""

    def __init__(self, variables: List[str], formula: Formula) -> None:
        self.variables = [Variable(v) for v in variables]
        self.operator = Formula.FORALL
        self.args = [formula]

    def instantiate(self, instantiation: Mapping[Variable, Term]) -> Formula:
        """Instantiates the formula with variables. Not needed, just for future use."""
        newInst = dict(instantiation)
        for variable in self.variables:
            newInst.pop(variable, None)
        return Forall(self.variables, self.args[0].instantiate(newInst))

    def getComponents(self, predicates, functions):
        """Fills up the predicates with their arities, the variables, and the functions with their arities"""
        self.args[0].getComponents(predicates, functions)

    def expand(self, n: int):
        """Expands FORALL x_n    to  FORALL x_1, ..., x_n"""
        newVariables = []
        for v in self.variables:
            newVariables += v.expand(n)
        newForall = Forall([], self.args[0].expand(n))
        newForall.variables = newVariables
        return newForall

    def quote(self) -> Term:
        """Quotes the formula except variables"""
        if len(self.variables) == 0:
            return self.args[0].quote()
        return Term(
            Formula.quoteStr(self.operator),
            self.variables[0].quote(),
            Forall(self.variables[1:], self.args[0]).quote(),
        )

    def __str__(self) -> str:
        return (
            "(! ["
            + ", ".join([str(a) for a in self.variables])
            + "]: "
            + str(self.args[0])
            + ")"
        )


###########################################################################################
#                       Atoms                                                             #
###########################################################################################


class Atom(Formula):
    """Represents an atom of a predicate and arguments"""

    def __init__(self, predicate: str, *args: Term) -> None:
        Formula.checkIdentifier(predicate)
        self.operator = predicate
        for a in args:
            if not isinstance(a, Term):
                raise Exception(
                    f"Atom arguments must be terms, not {a} of type {type(a)}"
                )
        self.args = args

    def quote(self) -> Term:
        """Quotes the formula except variables"""
        if len(self.args) == 0 and Formula.isVariable(self.operator):
            return Variable(self.operator)
        return Term(Formula.quoteStr(self.operator), *[a.quote() for a in self.args])

    def instantiate(self, instantiation: Mapping[Variable, Term]) -> Formula:
        """Instantiates the atom with variables. Not needed, just for future use."""
        return Atom(self.operator, *[a.instantiate(instantiation) for a in self.args])

    def expand(self, n: int):
        """Expands
        - p(x_n)   to   p(x1, x2, ..., x_n)
        - p(x_AND) to   p(x_1) & p(x_2) & ... p(x_n)"""
        if (
            len(self.args) > 0
            and isinstance(self.args[0], Variable)
            and self.args[0].function.endswith("_AND")
        ):
            return And(
                *[
                    Atom(self.operator, *[v.setIndex(i) for v in self.args])
                    for i in range(1, n + 1)
                ]
            )
        return Atom(self.operator, *[k for a in self.args for k in a.expand(n)])

    def getComponents(
        self,
        predicates: Mapping[str, int],
        functions: Mapping[str, int],
    ):
        """Fills up the predicates with their arities, the variables, and the functions with their arities"""
        predicates[self.operator] = len(self.args)
        for a in self.args:
            a.getComponents(predicates, functions)

    def __str__(self) -> str:
        return self.operator + "(" + ", ".join([str(a) for a in self.args]) + ")"
    
    def getArity(self) -> int:
        """Returns the arity of the predicate at the top of this atom"""
        return len(self.args)


def Ist(context: Term, formula: Formula) -> Atom:
    """Convenience function to create the formula "ist(context, formula)" """
    return Atom("ist", context, formula)


def Equals(term1: Term, term2: Term) -> Atom:
    """Convenience function to create the formula "equals(arg1, arg2)" """
    return Atom("equals", term1, term2)


###########################################################################################
#                       Terms                                                             #
###########################################################################################


class Term:
    """Represents a term of a function symbol and arguments"""

    function : str

    def __init__(self, function: str, *args: Term) -> None:
        Formula.checkIdentifier(function)
        self.function = function
        for a in args:
            if not isinstance(a, Term):
                raise Exception(
                    f"Term arguments must be terms, not {a} of type {type(a)}"
                )
        self.args = args

    def __key(self):
        return (self.function, *[a.__key() for a in self.args])

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Term):
            return self.__key() == other.__key()
        return NotImplemented

    def setIndex(self, i: int):
        """If this is a variable x_AND or x_TERM, returns x_i. Otherwise, returns self."""
        return self

    def expand(self, n: int):
        """Expands x_n to x_1...x_n. Expands p(x_TERM) to p(x_1),...p(x_n). Otherwise, returns self"""
        if any(s.function.endswith("_TERM") for s in self.args):
            return [
                Term(self.function, *[s.setIndex(i) for s in self.args])
                for i in range(1, n + 1)
            ]
        return [Term(self.function, *[k for a in self.args for k in a.expand(n)])]

    def instantiate(self, instantiation: Mapping[Variable, Term]) -> Formula:
        """Instantiates the term with variables. Not needed, just for future use."""
        return Term(self.function, *[a.instantiate(instantiation) for a in self.args])

    def getComponents(self, predicates, functions):
        """Fills up the predicates with their arities, the variables, and the functions with their arities"""
        functions[self.function] = len(self.args)
        for a in self.args:
            a.getComponents(predicates, functions)

    def quote(self) -> Term:
        """Quotes the formula except variables"""
        return Term(Formula.quoteStr(self.function), *[a.quote() for a in self.args])
    
    def getArity(self) -> int:
        """Returns the arity of the function at the top of this term"""
        return len(self.args)

    def __str__(self) -> str:
        if len(self.args) == 0:
            return self.function
        return self.function + ("(" + ", ".join([str(a) for a in self.args]) + ")")


class Variable(Term):
    """Represents a variable"""

    def __init__(self, name: str) -> None:
        self.function = name
        self.args = []

    def getComponents(self, predicates, functions):
        """Does nothing"""
        return

    def setIndex(self, i: int):
        """If this is a variable x_AND or x_TERM, returns x_i. Otherwise, returns self."""
        if self.function.endswith("_AND"):
            return Variable(self.function[:-4] + "_" + str(i))
        if self.function.endswith("_TERM"):
            return Variable(self.function[:-5] + "_" + str(i))
        return self

    def expand(self, n: int):
        """Expands x_n to x_1....x_n"""
        if not self.function.endswith("n"):
            return [self]
        return [Variable(self.function[:-1] + "_" + str(i)) for i in range(1, n + 1)]

    def quote(self) -> Term:
        """Does nothing, returns self"""
        return self
    
    def getArity(self):
        """By convention, variables have arity 0"""
        return 0

    def instantiate(self, instantiation: Mapping[Variable, Term]) -> Formula:
        """Instantiates the term with variables. Not needed, just for future use."""
        return instantiation.get(self, self)

    def __str__(self) -> str:
        return self.function.title()


###########################################################################################
#                       Convenience functions                                             #
###########################################################################################


def Implies(arg1: Formula, arg2: Formula) -> Formula:
    """Convenience function to create the formula "arg1 => arg2" """
    return Formula(Formula.IMPLIES, arg1, arg2)


def And(*args: Formula) -> Formula:
    """Convenience function to create the formula "arg1 & arg2" """
    return Formula(Formula.AND, *args)


def Not(arg: Formula) -> Formula:
    """Convenience function to create the formula "~arg1" """
    return Formula(Formula.NOT, arg)


def Eqv(form1: Formula, form2: Formula) -> Formula:
    """Convenience function to create the formula "form1 <-> form2" """
    return Formula(Formula.EQV, form1, form2)


def qAnd(*args: Term) -> Term:
    """Convenience function to create the term qAnd(arg1, arg2)"""
    return Term(Formula.quoteStr(Formula.AND), *args)


def qNot(arg: Term) -> Term:
    """Convenience function to create the term qNot(arg)"""
    return Term(Formula.quoteStr(Formula.NOT), arg)


def V(name: str) -> Variable:
    """Convenience function to create a variable"""
    return Variable(name)
