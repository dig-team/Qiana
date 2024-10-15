def test_expandbasic():
    from qianaExtension.SchemeFactory import SchemeFactory
    f = SchemeFactory._expandSimpleMacros
    assert f("ist(c,(a \\!^ b))").replace(" ","") == "ist(c,(qAnd(a,b)))"
    assert f("ist(c,(a \\!^ b) \\!^ c)").replace(" ","") == "ist(c,qAnd((qAnd(a,b)),c))"
    assert f("ist(c,(a\\!^b) \\!^ c)").replace(" ","") == "ist(c,qAnd((qAnd(a,b)),c))"
    assert f("ist(tc, \\!¬\\!¬t1)").replace(" ","") == "ist(tc,qNot(qNot(t1)))"
    assert f("ist(tc, \\!¬ \\!¬ t1)").replace(" ","") == "ist(tc,qNot(qNot(t1)))"

def test_expandOneRepetitionMacro():
    from qianaExtension.SchemeFactory import SchemeFactory
    f = SchemeFactory._expandOneRepetitionMacro
    assert f("ist(tc, \\![t$;^])", 3) == "ist(tc, t1^t2^t3)"

def test_genSchemeInstance():
    from qianaExtension.SchemeFactory import SchemeFactory
    f = SchemeFactory.generateInstance
    assert f("ist(tc, \\![t$;^])", [3]) == "ist(tc, t1^t2^t3)"