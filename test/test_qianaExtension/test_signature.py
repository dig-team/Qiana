def test_extend_from_tptp_simple():
    # Test with a simple predicate
    from qiana.qianaExtension.signature import Signature
    signature = Signature()
    signature.extendFromTptp("p(X1, X2)")
    assert "p" in signature.basePredicates
    assert signature.basePredicates["p"] == 2
    assert not signature.baseFunctions  # Should be empty

def test_extend_from_tptp_with_function():
    # Test with a predicate containing a function
    from qiana.qianaExtension.signature import Signature
    signature = Signature()
    signature.extendFromTptp("p(f(X1), X2)")
    assert "p" in signature.basePredicates
    assert signature.basePredicates["p"] == 2
    assert "f" in signature.baseFunctions
    assert signature.baseFunctions["f"] == 1

def test_extend_from_tptp_nested_functions():
    # Test with nested functions
    from qiana.qianaExtension.signature import Signature
    signature = Signature()
    signature.extendFromTptp("q(f(g(X1)), h(X2, X3))")
    assert "q" in signature.basePredicates
    assert signature.basePredicates["q"] == 2
    assert "f" in signature.baseFunctions
    assert signature.baseFunctions["f"] == 1
    assert "g" in signature.baseFunctions
    assert signature.baseFunctions["g"] == 1
    assert "h" in signature.baseFunctions
    assert signature.baseFunctions["h"] == 2

def test_extend_from_tptp_with_quantifier():
    # Test with quantifiers
    from qiana.qianaExtension.signature import Signature
    signature = Signature()
    signature.extendFromTptp("![X1] : p(X1, f(X2))")
    assert "p" in signature.basePredicates
    assert signature.basePredicates["p"] == 2
    assert "f" in signature.baseFunctions
    assert signature.baseFunctions["f"] == 1

def test_extend_from_tptp_complex():
    # Test with a complex formula
    from qiana.qianaExtension.signature import Signature
    signature = Signature()
    signature.extendFromTptp("r(a, f(b, g(c, d)), h(i(e)))")
    assert "r" in signature.basePredicates
    assert signature.basePredicates["r"] == 3
    assert "f" in signature.baseFunctions
    assert signature.baseFunctions["f"] == 2
    assert "g" in signature.baseFunctions
    assert signature.baseFunctions["g"] == 2
    assert "h" in signature.baseFunctions
    assert signature.baseFunctions["h"] == 1
    assert "i" in signature.baseFunctions
    assert signature.baseFunctions["i"] == 1
    # Constants are 0-arity functions
    assert "a" in signature.baseFunctions
    assert signature.baseFunctions["a"] == 0
    assert "b" in signature.baseFunctions
    assert signature.baseFunctions["b"] == 0
    assert "c" in signature.baseFunctions
    assert signature.baseFunctions["c"] == 0
    assert "d" in signature.baseFunctions
    assert signature.baseFunctions["d"] == 0
    assert "e" in signature.baseFunctions
    assert signature.baseFunctions["e"] == 0

def test_extend_from_tptp_multiple_calls():
    # Test extending with multiple calls
    from qiana.qianaExtension.signature import Signature
    signature = Signature()
    signature.extendFromTptp("p(X1)")
    signature.extendFromTptp("q(f(X1))")
    signature.extendFromTptp("r(g(X1, X2))")
    
    assert "p" in signature.basePredicates
    assert signature.basePredicates["p"] == 1
    assert "q" in signature.basePredicates
    assert signature.basePredicates["q"] == 1
    assert "r" in signature.basePredicates
    assert signature.basePredicates["r"] == 1
    assert "f" in signature.baseFunctions
    assert signature.baseFunctions["f"] == 1
    assert "g" in signature.baseFunctions
    assert signature.baseFunctions["g"] == 2

def test_extend_from_tptp_only_variable():
    # Test with just a variable
    from qiana.qianaExtension.signature import Signature
    signature = Signature()
    signature.extendFromTptp("X1")
    assert not signature.basePredicates  # Should be empty
    assert not signature.baseFunctions  # Should be empty

def test_extend_from_tptp_constants():
    # Test with constants (0-arity functions)
    from qiana.qianaExtension.signature import Signature
    signature = Signature()
    signature.extendFromTptp("p(a, b, c)")
    assert "p" in signature.basePredicates
    assert signature.basePredicates["p"] == 3
    assert "a" in signature.baseFunctions
    assert signature.baseFunctions["a"] == 0
    assert "b" in signature.baseFunctions
    assert signature.baseFunctions["b"] == 0
    assert "c" in signature.baseFunctions
    assert signature.baseFunctions["c"] == 0

def test_extend_from_tptp_logical_connectives():
    # Test with logical connectives
    from qiana.qianaExtension.signature import Signature
    signature = Signature()
    signature.extendFromTptp("p(X1) & q(X2) => r(f(X1), g(X2))")
    assert "p" in signature.basePredicates
    assert signature.basePredicates["p"] == 1
    assert "q" in signature.basePredicates
    assert signature.basePredicates["q"] == 1
    assert "r" in signature.basePredicates
    assert signature.basePredicates["r"] == 2
    assert "f" in signature.baseFunctions
    assert signature.baseFunctions["f"] == 1
    assert "g" in signature.baseFunctions
    assert signature.baseFunctions["g"] == 1

def test_extend_from_tptp_quoted_symbols():
    # Test with quoted symbols
    from qiana.qianaExtension.signature import Signature
    signature = Signature()
    signature.extendFromTptp("q(q_p(X1))")
    assert "q" in signature.basePredicates
    assert signature.basePredicates["q"] == 1
    assert "q_p" not in signature.baseFunctions
    assert "p" not in signature.basePredicates

def test_extend_from_full_tptpts():
    from os.path import join, dirname
    from qiana.qianaExtension.signature import Signature

    signature = Signature()
    with open(join("..","test","testInputs","RJbasic.p")) as file:
        signature.extendFromTptps(file.read())
    pass
    