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

def test_arityRanges():
    """
    Test schemes containing the ARITY keyword.
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

def test_arityRanges2():
    """
    Test schemes containing complex ARITY range specifications with multiple functions,
    different arity ranges, and combined patterns.
    """
    from qianaExtension.formulaExtension import getAllSchemesInstances
    from qianaExtension.signature import Signature
    lines = """
    FUNCTION f OF ARITY 2
    FUNCTION g OF ARITY 1
    FUNCTION h OF ARITY 3
    FUNCTION i OF ARITY 0
    PREDICATE p OF ARITY 2
    PREDICATE q OF ARITY 1
    
    FORMULA complex_test
    BODY ![X1,...,X#, Y1,...,Y#] : (((wft(X1) &...& wft(X#)) & (term(Y1) &...& term(Y#))) => $f(X1,...,X#) = $g(Y1,...,Y#) & $p(X1,Y1))
    DOT_ARITIES $f $g $f $g $f $g
    RANGE $f[1;3] IN BASE_FUNCTION
    RANGE $g[0;2] IN BASE_FUNCTION
    RANGE $p IN BASE_PREDICATE
    DISTINCT $f $g
    
    FORMULA additional_test
    BODY ![Z] : ($h(Z) = Z => $p(Z, $g(Z)))
    RANGE $h[1;1] IN BASE_FUNCTION
    RANGE $g[0;1] IN BASE_FUNCTION
    RANGE $p IN BASE_PREDICATE
    """.splitlines()
    
    sig = Signature()
    allInstances = getAllSchemesInstances(lines, sig)
    
    # General validation
    for instance in allInstances: 
        assert "..." not in instance
    
    # Validate formula generation
    names = [instance.split(",")[0] for instance in allInstances]
    assert len(names) == len(set(names)), "All names should be different"
    
    # Validate specific arity constraint cases
    f2_instances = [inst for inst in allInstances if "f(X1,X2)" in inst]
    f1_instances = [inst for inst in allInstances if "g(Y1)" in inst]
    i0_instances = [inst for inst in allInstances if "i(" in inst]
    
    # Function with arity 2 should be included (in range [1;3])
    assert len(f2_instances) > 0, "Function with arity 2 should be included"
    
    # Function with arity 1 should be included (in range [0;2])
    assert len(f1_instances) > 0, "Function with arity 1 should be included"
    
    # Function with arity 0 should be included in instances where range is [0;2]
    assert len(i0_instances) > 0, "Function with arity 0 should be included"
    
    # Check distinct constraint is enforced
    for instance in allInstances:
        if "f(X1,X2) = f(Y1,Y2)" in instance:
            assert False, "Distinct constraint violated"
            
    # Validate complex patterns
    assert any("f(X1,X2) = g(Y1)" in inst for inst in allInstances), "Missing expected pattern combination"
    assert any("g(Z) = Z => p(Z, g(Z))" in inst for inst in allInstances), "Missing expected pattern in second formula"

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
