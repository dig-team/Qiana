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
    assert f("ist(tc, f(\![eval(t_$);,]))", 3) == "ist(tc, f(eval(t_1),eval(t_2),eval(t_3)))"

def test_genSchemeInstance():
    from qianaExtension.SchemeFactory import SchemeFactory
    f = SchemeFactory.generateInstance
    assert f("ist(tc, \\!¬ \\!¬ t1)",[]).replace(" ","") == "ist(tc,qNot(qNot(t1)))"
    assert f("ist(tc, \\![t$;^])", [3]) == "ist(tc, t1^t2^t3)"
    assert f("ist(tc, f(\![eval(t_$);,]))", [3]) == "ist(tc, f(eval(t_1),eval(t_2),eval(t_3)))"
    assert f("\![ist(tc, p$);^] => ist(tc, \![p$;^])", [3,3]) == "ist(tc, p1)^ist(tc, p2)^ist(tc, p3) => ist(tc, p1^p2^p3)"
    assert f("\![ist(tc,p$);^] => ist(tc,\![p$;\!^])", [3,3]).replace(" ","") == "ist(tc,p1)^ist(tc,p2)^ist(tc,p3)=>ist(tc,qAnd(p1,qAnd(p2,p3)))"