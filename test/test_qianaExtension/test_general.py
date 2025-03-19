import pytest

def test_import_qianaExtension():
    from qianaExtension.formulaExtension import getAllSchemesInstances

def test_findOperand():
    from qianaExtension.formulaExtension import findOperands
    leftop, rightop, leftIndex, rightIndex = findOperands("t1,...,t2", 2)

def test_schemes_basic():
    from qianaExtension.formulaExtension import getAllSchemesInstances
    from qianaExtension.signature import Signature
    lines = """
    % FUNCTION and PREDICATE define new base functions and predicate, respectively (elements of $F_b$ and $P_b$)
    FUNCTION f OF ARITY 2
    PREDICATE p OF ARITY 2
    FUNCTION c OF ARITY 0

    FORMULA test
    BODY ![X1,...,X#] : ((wft(X1) &...& wft(X#)) => truth($qp(X1,...,X#)))
    DOT_ARITIES $p $p $p
    RANGE $p IN BASE_PREDICATE
    % Alternatives are BASE_PREDICATE, BASE_FUNCTION, ANY_FUNCTION, ANY_PREDICATE, QUOTED_VARIABLE
    WITH $qp QUOTING $p
    """
    lines = lines.strip().splitlines()
    sig = Signature()
    allInstances = getAllSchemesInstances(lines, sig)
    for instance in allInstances: assert "..." not in instance

def test_schemes_harder():
    from qianaExtension.formulaExtension import getAllSchemesInstances
    from qianaExtension.signature import Signature
    lines = """
    % FUNCTION and PREDICATE define new base functions and predicate, respectively (elements of $F_b$ and $P_b$)
    FUNCTION f OF ARITY 2
    FUNCTION ff OF ARITY 3
    PREDICATE p OF ARITY 2
    FUNCTION c OF ARITY 0

    FORMULA test
    BODY ![X1,...,X#] : ((wft(X1) &...& wft(X#)) => truth($qp(X1,...,X#)))
    DOT_ARITIES $p $p $p
    RANGE $p IN BASE_PREDICATE
    % Alternatives are BASE_PREDICATE, BASE_FUNCTION, ANY_FUNCTION, ANY_PREDICATE, QUOTED_VARIABLE
    WITH $qp QUOTING $p
    """
    lines = lines.strip().splitlines()
    sig = Signature()
    allInstances = getAllSchemesInstances(lines, sig)
    for instance in allInstances: assert "..." not in instance

def test_noFunctions():
    """
    By not adding any base function we create a scheme that ranges over 0 functions
    """
    from qianaExtension.formulaExtension import getAllSchemesInstances
    from qianaExtension.signature import Signature
    lines = """
    FORMULA A31
    BODY ![X1,...,X#, Y1, Y2] : ((term(X1)&...&term(X#)) => sub($f(X1,...,X#), Y1, Y2) = $f(sub(X1, Y1, Y2),...,sub(X#, Y1, Y2)))
    RANGE $f IN BASE_FUNCTION
    DOT_ARITIES $f $f $f $f
    """.splitlines()
    sig = Signature()
    allInstances = getAllSchemesInstances(lines, sig)
    for instance in allInstances: assert "..." not in instance

def test_A31():
    """
    Specifically test scheme A31
    """
    from qianaExtension.formulaExtension import getAllSchemesInstances
    from qianaExtension.signature import Signature
    lines = """
    FUNCTION f OF ARITY 2
    FORMULA A31
    BODY ![X1,...,X#, Y1, Y2] : ((term(X1)&...&term(X#)) => sub($f(X1,...,X#), Y1, Y2) = $f(sub(X1, Y1, Y2),...,sub(X#, Y1, Y2)))
    RANGE $f IN BASE_FUNCTION
    DOT_ARITIES $f $f $f $f
    """.splitlines()
    sig = Signature()
    allInstances = getAllSchemesInstances(lines, sig)
    for instance in allInstances: assert "..." not in instance


def test_include_schemes():
    """
    Test the schemes included in the qianaExtension/qianaAxio.schemes file
    """
    from qianaExtension.formulaExtension import getAllSchemesInstances
    from qianaExtension.signature import Signature
    with open("qianaExtension/qianaAxio.schemes") as f:
        lines = f.readlines()
    sig = Signature()
    allInstances = getAllSchemesInstances(lines, sig)
    for instance in allInstances: assert "..." not in instance
