def test_stripParenthesis():
    from qiana.qianaExtension.tptpParsing import _removeTopLevelParenthesis
    assert _removeTopLevelParenthesis("(p(X1))") == "p(X1)"
    assert _removeTopLevelParenthesis("((p(X1)))") == "p(X1)"
    assert _removeTopLevelParenthesis("(p(X1)) => (q(X2))") == "(p(X1)) => (q(X2))"

def test_splitOnComma():
    from qiana.qianaExtension.tptpParsing import _splitOnCommas
    assert _splitOnCommas("p(X1), g(X2)") == ["p(X1)", "g(X2)"]

def test_parseTopLevel():
    from qiana.qianaExtension.tptpParsing import _parseTopLevel
    assert _parseTopLevel("p(f(X1), g(X2))") == ["p", "f(X1)", "g(X2)"]
    assert _parseTopLevel("(p(X1)) => (q(X2))") == ["=>", "(p(X1))", "(q(X2))"]
    assert _parseTopLevel("p(f(X1), g(X2))") == ["p", "f(X1)", "g(X2)"]
    assert _parseTopLevel("(p(X1)) => (q(X2))") == ["=>", "(p(X1))", "(q(X2))"]
    assert _parseTopLevel("p(X1) & q(X2)") == ["&", "p(X1)", "q(X2)"]
    assert _parseTopLevel("p(X1) | q(X2)") == ["|", "p(X1)", "q(X2)"]
    assert _parseTopLevel("~p(X1)") == ["~", "p(X1)"]
    assert _parseTopLevel("p(X1) & q(X2) => r(f(X1), g(X2))") == ['=>', 'p(X1) & q(X2)', 'r(f(X1), g(X2))']

    try:
        _parseTopLevel("f())")
        raise Exception("_parseTopLevel returned on an ill formated input")
    except AssertionError:
        assert True

def test_parseStruct():
    from qiana.qianaExtension.tptpParsing import _parseStruct
    assert _parseStruct("p(f(X1), g(X2))") == ["p", ["f", ["X1"]], ["g", ["X2"]]]
    assert _parseStruct("(p(X1)) => (q(X2))") == ["=>", ["p", ["X1"]], ["q", ["X2"]]]
    assert _parseStruct("p(X1) & q(X2)") == ["&", ["p", ["X1"]], ["q", ["X2"]]]
    assert _parseStruct("p(X1) | q(X2)") == ["|", ["p", ["X1"]], ["q", ["X2"]]]
    assert _parseStruct("~p(X1)") == ["~", ["p", ["X1"]]]
    assert _parseStruct("p(X1) & q(X2) => r(f(X1), g(X2))") == ['=>', ['&', ['p', ['X1']], ['q', ['X2']]], ['r', ['f', ['X1']], ['g', ['X2']]]]

def test_parseSymbols():
    from qiana.qianaExtension.tptpParsing import parseSymbols
    assert parseSymbols("p(f(X1), g(X2))") == {'p': (2, False), 'f': (1, True), 'g': (1, True), 'X1': (0, True), 'X2': (0, True)}
    assert parseSymbols("(p(X1)) => (q(X2))") == {'p': (1, False), 'X1': (0, True), 'q': (1, False), 'X2': (0, True)}
    assert parseSymbols("p(X1) & q(X2)") == {'p': (1, False), 'X1': (0, True), 'q': (1, False), 'X2': (0, True)}
    assert parseSymbols("p(X1) | q(X2)") == {'p': (1, False), 'X1': (0, True), 'q': (1, False), 'X2': (0, True)}
    assert parseSymbols("~p(X1)") == {'p': (1, False), 'X1': (0, True)}
    assert parseSymbols("p(X1) & q(X2) => r(f(X1), q_g(X2))") == {'p': (1, False), 'X1': (0, True), 'q': (1, False), 'X2': (0, True), 'r': (2, False), 'f': (1, True), 'q_g': (1, True)}