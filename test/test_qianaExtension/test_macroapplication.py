def test_formula_from_struct():
    from qiana.qianaExtension.macroapplication import _formula_from_struct

    def ffs(struct):
        return _formula_from_struct(struct).replace(" ", "")

    # Test leaf case (single element)
    assert ffs(["a"]) == "a"
    assert ffs(["variable"]) == "variable"
    assert ffs(["123"]) == "123"

    # Test function/predicate application
    assert ffs(["f", ["a"], ["b"]]) == "f(a,b)"
    assert ffs(["pred", ["x"]]) == "pred(x)"
    assert ffs(["relation", ["term1"], ["term2"], ["term3"]]) == "relation(term1,term2,term3)"
    
    # Test function with no arguments (should return just the symbol)
    assert ffs(["constant"]) == "constant"

    # Test comma operator (variable lists)
    assert ffs([",", "x", "y"]) == "x,y"
    assert ffs([",", "a", "b", "c"]) == "a,b,c"
    assert ffs([",", "var1"]) == "var1"

    # Test negation
    assert ffs(["~", ["p"]]) == "~p"
    assert ffs(["~", ["pred", ["x"]]]) == "~pred(x)"

    # Test binary operators
    assert ffs(["=>", ["p"], ["q"]]) == "(p=>q)"
    assert ffs(["<=>", ["a"], ["b"]]) == "(a<=>b)"
    assert ffs(["=", ["x"], ["y"]]) == "(x=y)"
    assert ffs(["&", ["p"], ["q"]]) == "(p&q)"
    assert ffs(["|", ["a"], ["b"]]) == "(a|b)"

    # Test quantification
    assert ffs(["!", ["x"], ["p"]]) == "![x]:(p)"
    assert ffs(["?", ["y"], ["q"]]) == "?[y]:(q)"
    assert ffs(["!", [",", "x", "y"], ["pred", ["x"], ["y"]]]) == "![x,y]:(pred(x,y))"

    # Test nested structures
    assert ffs(["&", ["pred", ["x"]], ["~", ["other", ["y"]]]]) == "(pred(x)&~other(y))"
    assert ffs(["=>", ["=", ["x"], ["y"]], ["pred", ["x"]]]) == "((x=y)=>pred(x))"
    
    # Test complex nested quantification
    assert ffs(["!", ["x"], ["=>", ["p", ["x"]], ["q", ["x"]]]]) == "![x]:((p(x)=>q(x)))"

    # Test deeply nested function calls
    assert ffs(["f", ["g", ["a"]], ["h", ["b"], ["c"]]]) == "f(g(a),h(b,c))"

def test_quote_from_struct():
    from qiana.qianaExtension.macroapplication import _quote_from_struct

    def qfs(struct):
        return _quote_from_struct(struct, {}).replace(" ", "")

    # Test leaf case (single element)
    assert qfs(["a"]) == "q_a"
    assert qfs(["constant"]) == "q_constant"

    # Test function/predicate application
    assert qfs(["f", ["a"], ["b"]]) == "q_f(q_a,q_b)"
    assert qfs(["pred", ["x"]]) == "q_pred(q_x)"
    assert qfs(["relation", ["term1"], ["term2"], ["term3"]]) == "q_relation(q_term1,q_term2,q_term3)"

    # Test comma operator (variable lists)
    try : 
        qfs([",", "x", "y"])
        assert False, "Expected ValueError for comma operator without qvars"
    except ValueError as e: pass

    # Test negation
    assert qfs(["~", ["p"]]) == "q_Neg(q_p)"
    assert qfs(["~", ["pred", ["x"]]]) == "q_Neg(q_pred(q_x))"

    # Test binary operators
    assert qfs(["&", ["p"], ["q"]]) == "q_And(q_p,q_q)"
    assert qfs(["|", ["a"], ["b"]]) == "q_Or(q_a,q_b)"

    # Test quantification
    assert qfs(["!", ["X"], ["p", ["X"]]]) == "q_Forall(q_X1,q_p(q_X1))"
    assert qfs(["?", ["X"], ["p", ["X"]]]) == "q_Neg(q_Forall(q_X1,q_Neg(q_p(q_X1))))"

    # Test nested structures
    assert qfs(["!", [",", "X", "Y"], ["pred", ["X"], ["Y"]]]) == "q_Forall(q_X1,q_Forall(q_X2,q_pred(q_X1,q_X2)))"

def test_quote():
    from qiana.qianaExtension.macroapplication import _quote

    def quote(text):
        return _quote(text).replace(" ", "")

    # Test simple formula
    assert quote("p") == "q_p"
    assert quote("f(a,b)") == "q_f(q_a,q_b)"
    
    # Test negation
    assert quote("~p") == "q_Neg(q_p)"
    
    # Test binary operators
    assert quote("p & q") == "q_And(q_p,q_q)"
    assert quote("p | q") == "q_Or(q_p,q_q)"

    # Test quantification
    assert quote("![X]: p(X)") == "q_Forall(q_X1,q_p(q_X1))"
    assert quote("? [X]: p(X)") == "q_Neg(q_Forall(q_X1,q_Neg(q_p(q_X1))))"

    # Test nested quotation
    assert quote("q_Forall(q_X1,q_p(q_X1))") == "q_Quote(q_Forall(q_X1,q_p(q_X1)))"

def test_find_bang_pattern():
    from qiana.qianaExtension.macroapplication import _find_bang_pattern as fbp

    val = fbp("fof(test,axiom, !believes(alice,p(c,d)))")
    assert fbp("!believes(alice,bob_is_nice)") == ("!believes(alice,bob_is_nice)", "believes", "alice,bob_is_nice")

def test_applyMacros():
    from qiana.qianaExtension.macroapplication import applyMacros

    def app_mac(text):
        return applyMacros(text).replace(" ", "")

    # No macros
    assert app_mac("p") == "p"
    assert app_mac("f(a,b)") == "f(a,b)"
    assert app_mac("![X]: p(X)") == "![X]:p(X)"
    assert app_mac("fof(test,axiom,? [X]: p(X))") == "fof(test,axiom,?[X]:p(X))"

    # Simple macro application
    assert app_mac("fof(test,axiom, !believes(alice,p(c)))") == "fof(test,axiom,ist(believes(alice),q_p(q_c)))"
    assert app_mac("fof(test,axiom, !believes(alice,p(c,d)))") == "fof(test,axiom,ist(believes(alice),q_p(q_c,q_d)))"

    # Nested macro application
    assert app_mac("fof(test,axiom, !believes(alice,!believes(bob,flat(earth))))") == "fof(test,axiom,ist(believes(alice),q_ist(q_believes(q_bob),q_Quote(q_flat(q_earth)))))"
    
    # Nester macro application with multiple macros and quantification 
    assert app_mac("fof(test,axiom, (!believes(alice,? [X]: p(X))) & !believes(alice,!believes(bob,p(q))))") == "fof(test,axiom,(ist(believes(alice),q_Neg(q_Forall(q_X1,q_Neg(q_p(q_X1))))))&ist(believes(alice),q_ist(q_believes(q_bob),q_Quote(q_p(q_q)))))"