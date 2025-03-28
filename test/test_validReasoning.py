# TODO More inputs attempting to elicit wrong answers

def test_input_tautologies():
    from os.path import join, dirname
    from src.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testFiles","onlyTautologies.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.computeProofTree()
    assert not pipeline.contradiction()