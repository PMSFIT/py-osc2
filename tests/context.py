import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import osc2parser

__examples__ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'examples'))

def example_file(name):
    return os.path.join(__examples__,name)
