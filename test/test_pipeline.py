import pytest

def test_onEmptyClosure():
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    pipeline.computeQianaClosure("")

def test_nonEmptyClosure():
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    tptp = """
    fof(p, axiom, p(X1)).
    fof(q, axiom, q(X2)).
    fof(r, axiom, r(f(X1), 
        g(X2))).
    """
    pipeline.computeQianaClosure("p(X1) & q(X2) => r(f(X1), g(X2))")

def test_runComputeForCLI():
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    tptp = """
    fof(p, axiom, p(X1)).
    fof(q, axiom, q(X2)).
    fof(r, axiom, r(f(X1), 
        g(X2))).
    """
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()

def test_input_example_noindent():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","inputBasicNoIndent.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()

def test_input_example1():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","inputBasic.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()

def test_input_example2():
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","RJbasic.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()

def test_A30():
    """
    Scheme A30 handles distinct quoted variables for sub. Here we ensure they are properly distinct.
    """
    from os.path import join, dirname
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    tptp = ""
    pipeline.computeQianaClosure(tptp)
    closure = pipeline.qianaClosure
    assert any(line for line in closure.splitlines())
    assert all(not "axiom30" in line or not "q_Sub(q_X1, q_X1" in line for line in closure.splitlines())

def test_nadim():
    input_text = """
!wrote(nadim, (![X] : contemporary(X,rhaze) => transmutates(X))).
![X] : (ist(wrote(nadim),X) => q_Truth(X)).
contemporary(alice,rhaze).
~!believes(alice,transmutate(alice)).
    """
    from qiana.pipeline import Pipeline
    pipeline = Pipeline()
    pipeline.computeQianaClosure(input_text, quotedVariableNumber=5, simplified_input=True, expand_macros=True)
    # text = pipeline.getQianaClosure()