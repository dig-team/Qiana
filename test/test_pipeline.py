import pytest

def test_onEmptyClosure():
    from src.pipeline import Pipeline
    pipeline = Pipeline()
    pipeline.computeQianaClosure("")


def test_nonEmptyClosure():
    from src.pipeline import Pipeline
    pipeline = Pipeline()
    tptp = """
    fof(p, axiom, p(X1)).
    fof(q, axiom, q(X2)).
    fof(r, axiom, r(f(X1), 
        g(X2))).
    """
    pipeline.computeQianaClosure("p(X1) & q(X2) => r(f(X1), g(X2))")

def test_runComputeForCLI():
    from src.pipeline import Pipeline
    pipeline = Pipeline()
    tptp = """
    fof(p, axiom, p(X1)).
    fof(q, axiom, q(X2)).
    fof(r, axiom, r(f(X1), 
        g(X2))).
    """
    pipeline.computeQianaClosure(tptp)
    pipeline.computeProofTree()

def test_input_example_noindent():
    from os.path import join, dirname
    from src.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","inputBasicNoIndent.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.computeProofTree()

def test_input_example1():
    from os.path import join, dirname
    from src.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","inputBasic.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.computeProofTree()

def test_input_example2():
    from os.path import join, dirname
    from src.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","RJbasic.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.computeProofTree()