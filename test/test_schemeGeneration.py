def test_expandbasic():
    from qianaExtension.SchemeFactory import SchemeFactory
    f = SchemeFactory._expandSimpleMacros
    assert f("(a \\!^ b)") == "(qAnd(a,b))"
    assert f("(a \\!^ b) \\!^ c") == "(qAnd(qAnd(a,b),c)"
    assert f("(a\\!^b) \\!^ c") == "(qAnd(qAnd(a,b),c)"