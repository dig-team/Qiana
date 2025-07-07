# TODO More inputs attempting to elicit wrong answers

def test_onlyTautologies():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","onlyTautologies.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
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

def test_sub1():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","sub1.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert pipeline.contradiction()

def test_truth1():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","truth1.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert pipeline.contradiction()

def test_truth2():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","truth2.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert pipeline.contradiction()

def test_truth3():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","truth3.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert pipeline.contradiction()

def test_RJbasic():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","RJbasic.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
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

def test_nadim_1():
    input_text = """
!wrote(nadim, ![X] : (contemporary(X,rhazes) => !believes(X,transmutate(rhazes,copper)))).
![X] : (ist(wrote(nadim),X) => q_Truth(X)).
![X] : (contemporary(X,rhazes) => !believes(X,transmutate(rhazes,copper))).
contemporary(alice,rhazes).
~!believes(alice,transmutate(rhazes,copper)).
    """
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    pipeline.computeQianaClosure(input_text, quotedVariableNumber=5, simplified_input=True, expand_macros=True)
    text = pipeline.getQianaClosure()
    pipeline.runCompute_CLI()
    assert pipeline.foundContradiction