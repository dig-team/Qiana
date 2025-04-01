import pytest

def test_getAllSchemeInfos_basic():
    """
    Test getAllSchemeInfos with basic input.
    """
    from src.qianaExtension.patternParsing import getAllSchemeInfos, _getSymbolAndArity, _readSchemeInfo, SchemeInfo
    from src.qianaExtension.signature import Signature
    lines = [
        "FUNCTION f OF ARITY 2",
        "PREDICATE p OF ARITY 1",
        "FORMULA testFormula",
        "BODY $f(x, y)",
        "DOT_ARITIES $f",
        "RANGE $f IN BASE_FUNCTION",
        "WITH $qf QUOTING $f"
    ]
    schemeInfos, signature = getAllSchemeInfos(lines)
    assert len(schemeInfos) == 1
    assert isinstance(schemeInfos[0], SchemeInfo)
    assert schemeInfos[0].getName() == "testFormula"
    assert schemeInfos[0].getBody() == "$f(x, y)"
    assert schemeInfos[0].getAritySymbols() == ["$f"]
    assert schemeInfos[0].getSymbolTargets() == {"$f": "BASE_FUNCTION"}
    assert schemeInfos[0].symbolQuotationMatchings == {"$qf": "$f"}

def test_arityRanges():
    """
    Test getAllSchemeInfos with arity ranges.
    """
    from src.qianaExtension.patternParsing import getAllSchemeInfos, _getSymbolAndArity, _readSchemeInfo, SchemeInfo
    from src.qianaExtension.signature import Signature
    lines = [
        "FUNCTION f0 OF ARITY 0",
        "FUNCTION f1 OF ARITY 1",
        "FUNCTION f2 OF ARITY 2",
        "FUNCTION f3 OF ARITY 3",
        "FORMULA testFormula",
        "BODY ![X1,...,X#] : $p(f(X1,...,X#))",
        "DOT_ARITIES $f $f",
        "RANGE $f[1;2] IN BASE_FUNCTION",
    ]
    schemeInfos, signature = getAllSchemeInfos(lines)
    assert len(schemeInfos) == 1
    assert isinstance(schemeInfos[0], SchemeInfo)
    assert schemeInfos[0].getName() == "testFormula"
    assert schemeInfos[0].getBody() == "![X1,...,X#] : $p(f(X1,...,X#))"
    assert schemeInfos[0].getAritySymbols() == ["$f", "$f"]
    assert "$f" in schemeInfos[0].getSymbolTargets() 
    
def test_getAllSchemeInfos_empty():
    """
    Test getAllSchemeInfos with empty input.
    """
    from qianaExtension.patternParsing import getAllSchemeInfos, _getSymbolAndArity, _readSchemeInfo, SchemeInfo
    from qianaExtension.signature import Signature
    lines = []
    schemeInfos, signature = getAllSchemeInfos(lines)
    assert len(schemeInfos) == 0
    assert isinstance(signature, Signature)

def test_getAllSchemeInfos_comments():
    """
    Test getAllSchemeInfos with comments and empty lines.
    """
    from src.qianaExtension.patternParsing import getAllSchemeInfos, _getSymbolAndArity, _readSchemeInfo, SchemeInfo
    from src.qianaExtension.signature import Signature

    lines = [
        "% This is a comment",
        "",
        "FUNCTION f OF ARITY 2",
        "% Another comment",
        "PREDICATE p OF ARITY 1",
        "FORMULA testFormula",
        "BODY f(x, y)",
        "DOT_ARITIES $f",
        "RANGE $f IN BASE_FUNCTION",
        "WITH $qf QUOTING $f"
    ]
    schemeInfos, signature = getAllSchemeInfos(lines)
    assert len(schemeInfos) == 1
    assert isinstance(schemeInfos[0], SchemeInfo)
    assert schemeInfos[0].getName() == "testFormula"
    assert schemeInfos[0].getBody() == "f(x, y)"
    assert schemeInfos[0].getAritySymbols() == ["$f"]
    assert schemeInfos[0].getSymbolTargets() == {"$f": "BASE_FUNCTION"}
    assert schemeInfos[0].symbolQuotationMatchings == {"$qf": "$f"}

def test_getSymbolAndArity_function():
    """
    Test _getSymbolAndArity with a function line.
    """
    from src.qianaExtension.patternParsing import getAllSchemeInfos, _getSymbolAndArity, _readSchemeInfo, SchemeInfo
    from src.qianaExtension.signature import Signature

    line = "FUNCTION f OF ARITY 2"
    symbol, arity = _getSymbolAndArity(line)
    assert symbol == "f"
    assert arity == 2

def test_getSymbolAndArity_predicate():
    """
    Test _getSymbolAndArity with a predicate line.
    """
    from src.qianaExtension.patternParsing import getAllSchemeInfos, _getSymbolAndArity, _readSchemeInfo, SchemeInfo
    from src.qianaExtension.signature import Signature

    line = "PREDICATE p OF ARITY 1"
    symbol, arity = _getSymbolAndArity(line)
    assert symbol == "p"
    assert arity == 1

def test_getSymbolAndArity_invalid():
    """
    Test _getSymbolAndArity with an invalid line.
    """
    from src.qianaExtension.patternParsing import getAllSchemeInfos, _getSymbolAndArity, _readSchemeInfo, SchemeInfo
    from src.qianaExtension.signature import Signature

    line = "INVALID LINE"
    with pytest.raises(AssertionError):
        _getSymbolAndArity(line)

def test_readSchemeInfo_basic():
    """
    Test _readSchemeInfo with basic input.
    """
    from src.qianaExtension.patternParsing import getAllSchemeInfos, _getSymbolAndArity, _readSchemeInfo, SchemeInfo
    from src.qianaExtension.signature import Signature

    lines = [
        "FORMULA testFormula",
        "BODY f(x, y)",
        "DOT_ARITIES $f",
        "RANGE $f IN BASE_FUNCTION",
        "WITH $qf QUOTING $f"
    ]
    schemeInfo = _readSchemeInfo(lines)
    assert schemeInfo.getName() == "testFormula"
    assert schemeInfo.getBody() == "f(x, y)"
    assert schemeInfo.getAritySymbols() == ["$f"]
    assert schemeInfo.getSymbolTargets() == {"$f": "BASE_FUNCTION"}
    assert schemeInfo.symbolQuotationMatchings == {"$qf": "$f"}

def test_readSchemeInfo_no_DOT_ARITIES():
    """
    Test _readSchemeInfo without DOT_ARITIES line.
    """
    from src.qianaExtension.patternParsing import getAllSchemeInfos, _getSymbolAndArity, _readSchemeInfo, SchemeInfo
    from src.qianaExtension.signature import Signature

    lines = [
        "FORMULA testFormula",
        "BODY f(x, y)",
        "RANGE $f IN BASE_FUNCTION",
        "WITH $qf QUOTING $f"
    ]
    schemeInfo = _readSchemeInfo(lines)
    assert schemeInfo.getName() == "testFormula"
    assert schemeInfo.getBody() == "f(x, y)"
    assert schemeInfo.getAritySymbols() == []
    assert schemeInfo.getSymbolTargets() == {"$f": "BASE_FUNCTION"}
    assert schemeInfo.symbolQuotationMatchings == {"$qf": "$f"}

def test_readSchemeInfo_no_quotations():
    """
    Test _readSchemeInfo without WITH line.
    """
    from src.qianaExtension.patternParsing import getAllSchemeInfos, _getSymbolAndArity, _readSchemeInfo, SchemeInfo
    from src.qianaExtension.signature import Signature

    lines = [
        "FORMULA testFormula",
        "BODY f(x, y)",
        "DOT_ARITIES $f",
        "RANGE $f IN BASE_FUNCTION"
    ]
    schemeInfo = _readSchemeInfo(lines)
    assert schemeInfo.getName() == "testFormula"
    assert schemeInfo.getBody() == "f(x, y)"
    assert schemeInfo.getAritySymbols() == ["$f"]
    assert schemeInfo.getSymbolTargets() == {"$f": "BASE_FUNCTION"}
    assert schemeInfo.symbolQuotationMatchings == {}

