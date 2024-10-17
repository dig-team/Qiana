def test_genDotFile():
    from dotGeneration import getDotFromSteps
    from interfaceTypes import ReasoningStep
    step1 = ReasoningStep("1", "phi 1", "transfo", [2])
    step2 = ReasoningStep("2", "phi 2", "input", [])
    steps = [step1, step2]
    dot = getDotFromSteps(steps)
    assert True

def test_genDotImage():
    from dotGeneration import getImgFromSteps
    from interfaceTypes import ReasoningStep
    step1 = ReasoningStep("1", "phi 1", "transfo", [2])
    step2 = ReasoningStep("2", "phi 2", "input", [])
    steps = [step1, step2]
    img = getImgFromSteps(steps)
    assert True
