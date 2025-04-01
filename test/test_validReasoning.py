# TODO More inputs attempting to elicit wrong answers

def test_onlyTautologies():
    from os.path import join, dirname
    from src.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","onlyTautologies.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert not pipeline.contradiction()

def test_pureFOLcontradiction():
    from os.path import join, dirname
    from src.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","pureFOLcontradiction.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert pipeline.contradiction()

def test_RJbasic():
    from os.path import join, dirname
    from src.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","RJbasic.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert pipeline.contradiction()

def test_RJbasic_noResult():
    from os.path import join, dirname
    from src.pipeline import Pipeline
    pipeline = Pipeline()
    with open(join("..","test","testInputs","RJbasic_noResult.p")) as file:
        tptp = file.read()
    pipeline.computeQianaClosure(tptp)
    pipeline.runCompute_CLI()
    assert not pipeline.contradiction()