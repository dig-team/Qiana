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
    names = [instance.split(",")[0] for instance in allInstances]
    assert len(names) == len(set(names)), "All names should be different"

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


def test_distincPairs():
    """
    Test schemes containing the DISTINCT keyword.
    """
    from qianaExtension.formulaExtension import getAllSchemesInstances
    from qianaExtension.signature import Signature
    lines = """
    FUNCTION f OF ARITY 2
    FUNCTION ff OF ARITY 2
    PREDICATE p OF ARITY 2
    FUNCTION c OF ARITY 0

    FORMULA test
    BODY ![X1,...,X#, Y1, Y2] : ((term(X1)&...&term(X#)) => sub($f(X1,...,X#), Y1, Y2) = $g(sub(X1, Y1, Y2),...,sub(X#, Y1, Y2)))
    RANGE $f IN BASE_FUNCTION
    RANGE $g IN BASE_FUNCTION
    DOT_ARITIES $f $f $f $f
    DISTINCT $f $g
    """.splitlines()
    sig = Signature()
    allInstances = getAllSchemesInstances(lines, sig)
    for instance in allInstances: assert "..." not in instance
    names = [instance.split(",")[0] for instance in allInstances]
    assert len(names) == len(set(names)), "All names should be different"

def test_distincPairs2():
    """
    Test schemes containing the DISTINCT keyword.
    """
    from qianaExtension.formulaExtension import getAllSchemesInstances
    from qianaExtension.signature import Signature
   
    lines = """
    FUNCTION f OF ARITY 2
    FUNCTION g OF ARITY 2

    FORMULA test
    BODY $f(x1,...,x#) = $g(x1,...,x#)
    RANGE $f IN BASE_FUNCTION
    RANGE $g IN BASE_FUNCTION
    DOT_ARITIES $f $g
    DISTINCT $f $g
    """.splitlines()
    sig = Signature()
    allInstances = getAllSchemesInstances(lines, sig)
    for instance in allInstances: assert "..." not in instance
    names = [instance.split(",")[0] for instance in allInstances]
    assert len(names) == len(set(names)), "All names should be different"
    for instance in allInstances: assert not "f(x1,x2) = f(x1,x2)" in instance
    assert any("f(x1,x2) = g(x1,x2)" in instance for instance in allInstances)

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

def test_arityRanges1():
    """
    Test the qiana extension with arity ranges.
    """
    from src.qianaExtension.formulaExtension import getAllSchemesInstances
    lines = [
        "FUNCTION f0 OF ARITY 0",
        "FUNCTION f1 OF ARITY 1",
        "FUNCTION f2 OF ARITY 2",
        "FUNCTION f3 OF ARITY 3",
        "FORMULA testFormula",
        "BODY ![X1,...,X#] : p($f(X1,...,X#))",
        "DOT_ARITIES $f $f",
        "RANGE $f[1;2] IN BASE_FUNCTION",
    ]
    instances = getAllSchemesInstances(lines)
    assert not any("f0" in instance for instance in instances)
    assert any("f2" in instance for instance in instances)
    assert not any("f3" in instance for instance in instances)

def test_arityRanges2():
    """
    Test the qiana extension with arity ranges.
    """
    from qianaExtension.formulaExtension import getAllSchemesInstances
    from qianaExtension.signature import Signature
    lines = """
    FUNCTION f OF ARITY 2
    FUNCTION ff OF ARITY 3

    FORMULA test
    BODY ![X1,...,X#] : ((wft(X1) &...& wft(X#)) => truth($f(X1,...,X#)))
    DOT_ARITIES $f $f $f
    RANGE $f[0;2] IN BASE_FUNCTION
    """.splitlines()
    sig = Signature()
    allInstances = getAllSchemesInstances(lines, sig)
    for instance in allInstances: assert "..." not in instance

def test_arityRanges3():
    """
    Test schemes containing complex ARITY range specifications with multiple functions,
    different arity ranges, and combined patterns.
    """
    from qianaExtension.formulaExtension import getAllSchemesInstances
    from qianaExtension.signature import Signature
    lines = """
    FUNCTION ff OF ARITY 2
    FUNCTION g OF ARITY 1
    FUNCTION h OF ARITY 3
    FUNCTION i OF ARITY 0
    PREDICATE p OF ARITY 2
    PREDICATE q OF ARITY 1
    
    FORMULA complex_test
    BODY ![X1,...,X#, Y1,...,Y#] : (((wft(X1) &...& wft(X#)) & (term(Y1) &...& term(Y#))) => $f(X1,...,X#) = $g(Y1,...,Y#) & $p(X1,Y1))
    DOT_ARITIES $f $g $f $g $f $g
    RANGE $f[1;2] IN BASE_FUNCTION
    RANGE $g[0;2] IN BASE_FUNCTION
    RANGE $p IN BASE_PREDICATE
    DISTINCT $f $g
    
    FORMULA additional_test
    BODY ![Z] : ($h(Z) = Z => $p(Z, $g(Z)))
    RANGE $h[1;1] IN BASE_FUNCTION
    RANGE $g[0;1] IN BASE_FUNCTION
    RANGE $p IN BASE_PREDICATE
    
    FORMULA edge_case_test
    BODY $f(X) = $g(Y)
    RANGE $f[0;0] IN BASE_FUNCTION
    RANGE $g[2;-1] IN BASE_FUNCTION
    
    FORMULA boundary_test
    BODY $f(X1,...,X#) = $f(Y1,...,Y#)
    DOT_ARITIES $f $f
    RANGE $f[2;2] IN BASE_FUNCTION
    """.splitlines()
    
    sig = Signature()
    allInstances = getAllSchemesInstances(lines, sig)
    
    # Organize instances by formula scheme
    complex_test_instances = [inst for inst in allInstances if "complex_test" in inst]
    additional_test_instances = [inst for inst in allInstances if "additional_test" in inst]
    edge_case_instances = [inst for inst in allInstances if "edge_case_test" in inst]
    boundary_test_instances = [inst for inst in allInstances if "boundary_test" in inst]
    
    # Verify we have instances for each formula type
    assert len(complex_test_instances) > 0, "Should have complex_test instances"
    assert len(additional_test_instances) > 0, "Should have additional_test instances"
    assert len(edge_case_instances) > 0, "Should have edge_case_test instances"
    assert len(boundary_test_instances) > 0, "Should have boundary_test instances"
    
    # Verify all instances are accounted for
    assert set(complex_test_instances + additional_test_instances + edge_case_instances + boundary_test_instances) == set(allInstances)

    assert all("..." not in instance for instance in allInstances)
    assert not any("h(" in instance for instance in complex_test_instances)
    assert not any("i(X" in instance for instance in complex_test_instances)
    assert not any("ff(" in instance for instance in additional_test_instances)
