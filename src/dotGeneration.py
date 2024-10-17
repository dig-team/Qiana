
from interfaceTypes import ReasoningStep

def getDotFromSteps(steps):
    """Returns the dot representation of the reasoning steps"""
    dot = "digraph G {\n"
    for step in steps:
        dot += _stepToNode(step) + "\n"
        dot += _stepToEdges(step) + "\n"
    return dot + "}"

def _stepToNode(step : ReasoningStep) -> str:
    return f'{step.id} [label="{step.toLightText()}"];'

def _stepToEdges(step : ReasoningStep) -> str:
    return "\n".join([f'{step.id} -> {parentId};' for parentId in step.Parents])