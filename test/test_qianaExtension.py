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

def test_extend_from_tptp():
    from src.qianaExtension.signature import Signature
    
    # Test case 1: Simple function and predicate
    sig1 = Signature()
    symbols1 = sig1.extendFromTptp("p(f(X1),X1)")
    assert len(symbols1) == 2
    assert ('p', 2, True) in symbols1
    assert ('f', 1, False) in symbols1
    
    # Test case 2: Nested functions
    sig2 = Signature()
    symbols2 = sig2.extendFromTptp("p(f(g(X1)),h(X2))")
    assert len(symbols2) == 4
    assert ('p', 2, True) in symbols2
    assert ('f', 1, False) in symbols2
    assert ('g', 1, False) in symbols2
    assert ('h', 1, False) in symbols2
    
    # Test case 3: Multiple arguments
    sig3 = Signature()
    symbols3 = sig3.extendFromTptp("p(X1,X2,X3) => q(f(X1,X2),g(X3))")
    assert len(symbols3) >= 4
    assert ('p', 3, True) in symbols3
    assert ('q', 2, True) in symbols3
    assert ('f', 2, False) in symbols3
    assert ('g', 1, False) in symbols3
    
    # Test case 4: Quantifiers and complex formula
    sig4 = Signature()
    symbols4 = sig4.extendFromTptp("![X1,X2]: (p(X1) & q(X2) => r(f(X1),g(X2)))")
    assert len(symbols4) >= 5
    assert ('p', 1, True) in symbols4
    assert ('q', 1, True) in symbols4
    assert ('r', 2, True) in symbols4
    assert ('f', 1, False) in symbols4
    assert ('g', 1, False) in symbols4
    
    # Test case 5: Empty arguments
    sig5 = Signature()
    symbols5 = sig5.extendFromTptp("p() & q(c())")
    assert len(symbols5) >= 2
    assert ('p', 0, True) in symbols5
    assert ('c', 0, False) in symbols5
    
    # Test case 6: Quoted symbols
    sig6 = Signature()
    symbols6 = sig6.extendFromTptp("truth(q_p(X1))")
    assert len(symbols6) >= 2
    assert ('truth', 1, True) in symbols6
    assert ('q_p', 1, False) in symbols6
