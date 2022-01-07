import sys
import re
import argparse
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl

from . import __version__
from .openscenario2Parser import openscenario2Parser
from .openscenario2Lexer import openscenario2Lexer
 
def create_argparser():
    parser = argparse.ArgumentParser(
        description='Check OpenSCENARIO 2.x File for Syntax.'
    )
    parser.add_argument('-v', '--version', action='version',
        version=f"{parser.prog} version {__version__}")
    parser.add_argument('-t', '--tree', action='store_true', help='Produce tree output of parsed content')
    parser.add_argument('-q', '--quiet', action='store_true', help='Avoid producing any output')
    parser.add_argument('files', nargs='+', help='a file to parse')
    return parser

def main():
    argparser = create_argparser()
    args = argparser.parse_args()
    result = 0
    for file in args.files:
        result += parse_file(file, args.quiet, args.tree)
    return 0 if result==0 else 1

def parse_file(file, quiet, print_tree):
    input_stream = FileStream(file)
    lexer = openscenario2Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = openscenario2Parser(stream)
    if quiet:
        parser.removeErrorListeners()
    tree = parser.osc_file()
    errors = parser.getNumberOfSyntaxErrors()
    if not quiet:
        print(f"Parse of {file} completed {'without' if errors==0 else f'with {errors}'} error{'s' if abs(errors)!=1 else ''}.", file=sys.stderr)
    if print_tree:
        print_tree(tree, parser.ruleNames)
    return 0 if errors==0 else 1

def print_tree(tree, ruleNames, indent = 0):
    if isinstance(tree, TerminalNodeImpl):
        if not re.match(r"\r?\n[ \t]*",tree.getText()):
            print("{0}TOKEN '{1}'".format("  " * indent, tree.getText()))
    else:
        print("{0}{1}".format("  " * indent, ruleNames[tree.getRuleIndex()]))
        for child in tree.children:
            print_tree(child,ruleNames,indent+1)

