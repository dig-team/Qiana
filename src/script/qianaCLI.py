import argparse
import sys
from os.path import dirname

sys.path.insert(0, dirname(dirname(__file__)))

from qiana.cli import main

if __name__ == "__main__":
    main()