def test_import_qianaExtension():
    from qianaExtension.formulaExtension import getAllSchemesInstances

def test_schemes_clear():
    from qianaExtension.formulaExtension import getAllSchemesInstances
    from qianaExtension.signature import Signature
    with open("examples/exampleSchemes.schemes","r") as f:
        lines = f.readlines()
    sig = Signature(functions={"f":2})
    allInstances = getAllSchemesInstances(lines, sig)
    for instance in allInstances: assert "..." not in instance
