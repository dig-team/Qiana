from typing import Dict, List

from interfaceTypes import ReasoningStep

def getHtml(steps : List[ReasoningStep]) -> str:
    """Returns the html representation of the reasoning steps"""
    idToStep = {step.id:step for step in steps}
    html = "<html>\n<head>\n<title>Reasoning steps</title>\n</head>\n<body>\n"
    html += _getStepHtml(steps[-1], idToStep)
    return html + "</body>\n</html>"

# def _getStepHtml(step : ReasoningStep, idToStep : Dict[str, ReasoningStep]) -> str:
#     """Returns the html representation of a single step"""
#     html = "<p>" + step.id + ". " + step.text + "<br>"
#     if step.Parents == []: return html + "</p>"
#     html += "Previous steps: "
#     html += '<div style="margin-left: 20px;">\n'
#     for parent in step.Parents:
#         html += f'<details>\n<summary>{parent}</summary>\n'
#         html += _getStepHtml(idToStep[parent], idToStep)
#     html += '</details>\n</div>\n'
#     return html[:-2] + "</p>"

def _getStepHtml(step : ReasoningStep, idToStep : Dict[str, ReasoningStep]) -> str:
    """Returns the html representation of a single step"""
    
    if not step.Parents : return step.toLightText()
    html = f'<details>\n<summary>{step.toLightText()}</summary>\n'
    html += '<div style="margin-left: 20px;">\n'
    for parentId in step.Parents:
        parent = idToStep[parentId]
        html += _getStepHtml(parent, idToStep)
    html += '</div>\n</details>\n'
    return html