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
    # FUNCTION and PREDICATE define new base functions and predicate, respectively (elements of $F_b$ and $P_b$)
    FUNCTION f OF ARITY 2
    PREDICATE p OF ARITY 2
    FUNCTION c OF ARITY 0

    FORMULA test
    BODY ![X1,...,Xn] (wft(X1) &...& wft(Xn) => truth($qp(X1,...,Xn)))
    DOT_ARITIES $p $p $p
    RANGE $p IN BASE_PREDICATE
    # Alternatives are BASE_PREDICATE, BASE_FUNCTION, ANY_FUNCTION, ANY_PREDICATE, QUOTED_VARIABLE
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
    # FUNCTION and PREDICATE define new base functions and predicate, respectively (elements of $F_b$ and $P_b$)
    FUNCTION f OF ARITY 2
    FUNCTION ff OF ARITY 3
    PREDICATE p OF ARITY 2
    FUNCTION c OF ARITY 0

    FORMULA test
    BODY ![X1,...,Xn] (wft(X1) &...& wft(Xn) => truth($qp(X1,...,Xn)))
    DOT_ARITIES $p $p $p
    RANGE $p IN BASE_PREDICATE
    # Alternatives are BASE_PREDICATE, BASE_FUNCTION, ANY_FUNCTION, ANY_PREDICATE, QUOTED_VARIABLE
    WITH $qp QUOTING $p
    """
    lines = lines.strip().splitlines()
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
