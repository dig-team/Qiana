def test_expandbasic():
    from qianaExtension.SchemeFactory import SchemeFactory
    f = SchemeFactory._expandSimpleMacros
    assert f("ist(c,(a \\!^ b))").replace(" ","") == "ist(c,(qAnd(a,b)))"
    assert f("ist(c,(a \\!^ b) \\!^ c)").replace(" ","") == "ist(c,qAnd((qAnd(a,b)),c))"
    assert f("ist(c,(a\\!^b) \\!^ c)").replace(" ","") == "ist(c,qAnd((qAnd(a,b)),c))"