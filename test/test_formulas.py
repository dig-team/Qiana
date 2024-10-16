def test_Not():
    from qianaExtension.Formulas import Formula
    from qianaExtension.FormulaParser import parse

    formula = parse("~p()")
    assert str(formula) == "~p()"