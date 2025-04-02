from os.path import join, dirname

example_dir = dirname(__file__)

with open(join(example_dir, 'RJbasic.p'), 'r') as f:
    Example_RJbasic = f.read()

with open(join(example_dir, 'SignatureTest.p'), 'r') as f:
    Example_SingatureTest = f.read()

with open(join(example_dir, 'RJsimple.p'), 'r') as f:
    Example_RJsimple = f.read()