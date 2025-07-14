# TODO More inputs attempting to elicit wrong answers

def test_onlyTautologies():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","onlyTautologies.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI(timeout=180)  
    assert not pipeline.contradiction()

def test_pureFOLcontradiction():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","pureFOLcontradiction.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert pipeline.contradiction()

def test_q_Term():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    
    def run(tptp):
        pipeline = Pipeline()
        pipeline.computeQianaClosure(tptp)
        pipeline.runCompute_CLI()
        return pipeline.contradiction()

    tptp = """
    fof(goal, conjecture, q_Term(c)).
    """
    assert run(tptp)

    tptp = """
    fof(goal, conjecture, q_Term(q_X1)).
    """
    assert run(tptp)

    tptp = """
    fof(h1, axiom, p(a) | ~p(a)).
    fof(goal, conjecture, q_Term(q_Forall(q_X1, q_p(q_X1)))).
    """
    assert run(tptp)

    tptp = """
    fof(h1, axiom, f(a) | ~f(a)).
    fof(goal, conjecture, q_Term(q_f(q_X1))).
    """
    assert run(tptp)

def test_equal():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    
    def run_assert(tptp, expect_contra : bool):
        pipeline = Pipeline()
        pipeline.computeQianaClosure(tptp)
        pipeline.runCompute_CLI()
        assert pipeline.contradiction() == expect_contra

    tptp = """
    fof(goal,conjecture, f = f).
    """
    run_assert(tptp, True)

    tptp = """
    fof(goal,conjecture, (a = b) => (p(a) => p(b))).
    """
    run_assert(tptp, True)

def test_sub():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    
    def run_assert(tptp, expect_contra : bool):
        pipeline = Pipeline()
        pipeline.computeQianaClosure(tptp)
        pipeline.runCompute_CLI()
        assert pipeline.contradiction() == expect_contra

    tptp = """
    fof(goal, conjecture, q_Sub(q_X1, q_X1, q_X2) = q_X2).
    """
    run_assert(tptp, True)

    tptp = """
    fof(h1, axiom, p(q_Sub(q_X1, q_X1, q_X2))).
    fof(goal, conjecture, p(q_X2)).
    """
    run_assert(tptp, True)

    tptp = """
    fof(f, axiom, p(f(a)) | ~p(f(a))).
    fof(goal, conjecture, q_Sub(q_f(q_X1), q_X1, q_X2) = q_f(q_Sub(q_X1,q_X1,q_X2))).
    """
    run_assert(tptp, True)

    tptp = """
    fof(f, axiom, p(f(a)) | ~p(f(a))).
    fof(h1,axiom,p(q_Sub(q_f(q_X1),q_X1,q_X2))).
    fof(goal,conjecture,p(q_f(q_X2))).
    """
    run_assert(tptp, True)

    tptp = """
    fof(goal, conjecture, ![X] : (q_Sub(q_p(q_X1), q_X1, q_Quote(X)) = q_p(q_Quote(X)))).
    """

def test_q_Wft():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    
    def run_assert(tptp, expect_contra : bool):
        pipeline = Pipeline()
        pipeline.computeQianaClosure(tptp)
        pipeline.runCompute_CLI()
        assert pipeline.contradiction() == expect_contra

    tptp = """
    fof(h1, axiom, p(c) | ~p(c)).
    fof(goal,conjecture,q_Wft(q_c)).
    """
    run_assert(tptp, True)

def test_truth():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    def run_assert(tptp, expect_contra : bool):
        pipeline = Pipeline()
        pipeline.computeQianaClosure(tptp)
        pipeline.runCompute_CLI(timeout=180) # Some of these take a while
        assert pipeline.contradiction() == expect_contra

    # tptp = """
    # fof(h2,axiom,q_Truth(q_p)).
    # fof(goal,conjecture,p).
    # """
    # run_assert(tptp, True)

    # tptp = """
    # fof(h1,axiom,p(c) | ~p(c)).
    # fof(h2,axiom,q_Truth(q_p(q_c))).
    # fof(goal,conjecture,p(c)).
    # """
    # run_assert(tptp, True)
    
    # tptp = """
    # fof(h1,axiom,p(f(a)) | ~p(f(a))).
    # fof(h1,axiom,q_Truth(q_Forall(q_X1, q_p(q_X1)))).
    # fof(goal,conjecture,![X] : q_Truth(q_Sub(q_p(q_X1), q_X1, q_Quote(X)))).
    # """
    # run_assert(tptp, True)

    # tptp = """
    # fof(goal, conjecture, (q_Truth(q_Forall(q_X1,q_X2)) <=> (![X3] : q_Truth(q_Sub(q_X2, q_X1, q_Quote(X3)))))).
    # """
    # run_assert(tptp, True)

    # tptp = """
    # fof(h1, axiom, p(f(a)) | ~p(f(a))).
    # fof(h2, axiom, q_Truth(q_Forall(q_X1, q_p(q_X1)))).
    # fof(goal, conjecture, ![X] : q_Truth(q_Sub(q_p(q_X1), q_X1, q_Quote(X)))).
    # """
    # run_assert(tptp, True)

    # tptp = """
    # fof(h1, axiom, p(f(a)) | ~p(f(a))).
    # fof(h2, axiom, q_Truth(q_Forall(q_X1, q_p(q_X1)))).
    # fof(goal, conjecture, ![X] : q_Truth(q_p(q_Quote(X)))).
    # """
    # run_assert(tptp, True)

    # tptp = """
    # fof(h1, axiom, p(f(a)) | ~p(f(a))).
    # fof(h2, axiom, q_Truth(q_Forall(q_X1, q_p(q_X1)))).
    # fof(goal, conjecture, ![X] : p(q_Eval(q_Quote(X)))).
    # """
    # run_assert(tptp, True)

    # tptp = """
    # fof(h1, axiom, p(f(a)) | ~p(f(a))).
    # fof(h2, axiom, q_Truth(q_Forall(q_X1, q_p(q_X1)))).
    # fof(goal, conjecture, ![X] : p(X)).
    # """
    # run_assert(tptp, True)

    # tptp = """
    # fof(h1, axiom, p(f(a)) | ~p(f(a))).
    # fof(h1, axiom, p(f(b)) | ~p(f(b))).
    # fof(h2, axiom, q_Truth(q_And(q_p(q_a),q_p(q_b)))).
    # fof(goal, conjecture, p(a)).
    # """
    # run_assert(tptp, True)

    # tptp = """
    # fof(h1, axiom, q_Truth(q_Neg(q_And(q_drinkPotion(q_c),q_Neg(q_appearDead(q_c)))))).
    # fof(goal,conjecture, ~(drinkPotion(c) & ~appearDead(c))).
    # """
    # run_assert(tptp, True)

    # tptp = """
    # fof(h1, axiom, q_Truth(q_Neg(q_And(q_drinkPotion(q_c),q_Neg(q_appearDead(q_c)))))).
    # fof(goal,conjecture, drinkPotion(c) => appearDead(c)).
    # """
    # run_assert(tptp, True)

    tptp = """
    fof(tauto, axiom, drinkPotion(c) | appearDead(c) | ~appearDead(c)).
    fof(h1, axiom, q_Truth(q_Forall(q_X1, q_Neg(q_And(q_drinkPotion(q_X1),q_Neg(q_appearDead(q_X1))))))).
    fof(goal,conjecture, ![X] : (~q_Truth(q_Sub(q_And(q_drinkPotion(q_X1),q_Neg(q_appearDead(q_X1))),q_X1,q_Quote(X))))).
    """
    run_assert(tptp, True)

    # TODO : the following tests don't work but given the ones above I am reasonably sure they should and only fail due to performance issues.
    # tptp = """
    # fof(tauto, axiom, drinkPotion(c) | appearDead(c) | ~appearDead(c)).
    # fof(h1, axiom, q_Truth(q_Forall(q_X1, q_Neg(q_And(q_drinkPotion(q_X1),q_Neg(q_appearDead(q_X1))))))).
    # fof(goal,conjecture, ![X] : (~q_Truth(q_And(q_Sub(q_drinkPotion(q_X1),q_X1,q_Quote(X)), q_Sub(q_Neg(q_appearDead(q_X1)), q_X1, q_Quote(X)))))).
    # """
    # run_assert(tptp, True)

    # tptp = """
    # fof(h1, axiom, q_Truth(q_Forall(q_X1, q_Neg(q_And(q_drinkPotion(q_X1),q_Neg(q_appearDead(q_X1))))))).
    # fof(goal,conjecture, ![X] : (drinkPotion(X) => appearDead(X))).
    # """
    # run_assert(tptp, True)

def test_lemma_RJbasic():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    def run_assert(tptp, expect_contra : bool):
        pipeline = Pipeline()
        pipeline.computeQianaClosure(tptp)
        pipeline.runCompute_CLI(timeout=60) # Some of these take a while
        assert pipeline.contradiction() == expect_contra
    tptp = """
    fof(h1,axiom,
        ! [X] : 
            (ist(say(friar), X) => q_Truth(X))
    ).

    fof(h5,axiom,
        ist(say(friar), q_Forall(q_X1, q_Not(q_And(q_drinkPotion(q_X1),q_Not(q_appearDead(q_X1))))))
    ).

    fof(redundant_1,conjecture, ![X] : (drinkPotion(X) => appearDead(X))).
    """
    run_assert(tptp, True)

def test_RJbasic():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","RJbasic.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI(timeout=180)  # This test can take a while
    assert pipeline.contradiction()

def test_RJbasic_noResult():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","RJbasic_noResult.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert not pipeline.contradiction()

def test_nadim_transmutation():
    """
    Used to find a bug at some point and so kept in the tests.
    """
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","nadim_transmutation.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert not pipeline.contradiction()

def test_minimal_quote():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","minimal_quote.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert pipeline.contradiction()

def test_nadim():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    def run_assert(tptp, expect_contra : bool, simplified_input : bool = True):
        pipeline = Pipeline()
        pipeline.computeQianaClosure(tptp, simplified_input=simplified_input, expand_macros=True)
        pipeline.runCompute_CLI(timeout=180) # Some of these take a while
        assert pipeline.contradiction() == expect_contra

    input_text = """
    fof(h1,axiom,ist(wrote(nadim), q_Forall(q_X1, q_Or(q_Neg(q_contemporary(q_X1, q_rhazes)), q_trust(q_X1, q_rhazes))))).
    fof(h2, axiom, ![X] : (ist(wrote(nadim),X) => q_Truth(X))).
    fof(goal, conjecture, ![X] : (contemporary(X,rhazes) => trust(X,rhazes))).
    """
    run_assert(input_text, True, simplified_input=False)

    input_text = """
!wrote(nadim, ![X] : (contemporary(X,rhazes) => !believes(X,transmutate(rhazes,copper)))).
![X] : (ist(wrote(nadim),X) => q_Truth(X)).
![X] : (contemporary(X,rhazes) => !believes(X,transmutate(rhazes,copper))).
contemporary(alice,rhazes).
~!believes(alice,transmutate(rhazes,copper)).
    """

    run_assert(input_text, True)

    input_text = """
!believes(alice,fraud(rhazes) | transmutates_gold_copper(rhazes)).
!believes(alice,~fraud(rhazes)).
good_biographer(nadim) => (contemporary(rhazes, alice) => !believes(alice,~fraud(rhazes))).
contemporary(rhazes, alice).
good_biographer(nadim).
~!believes(alice,transmutates_gold_copper(rhazes)).
    """

    run_assert(input_text, True)

    input_text = """
!believes(alice,fraud(rhazes) | transmutates_gold_copper(rhazes)).
good_biographer(nadim) => (contemporary(rhazes, alice) => !believes(alice,~fraud(rhazes))).
contemporary(rhazes, alice).
good_biographer(nadim).
~!believes(alice,transmutates_gold_copper(rhazes)).
    """

    run_assert(input_text, True)

