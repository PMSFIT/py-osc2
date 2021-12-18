import sys
import re
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from openscenario2Parser import openscenario2Parser
from openscenario2Lexer import openscenario2Lexer
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = openscenario2Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = openscenario2Parser(stream)
    tree = parser.osc_file()
    process(tree, parser.ruleNames)

def process(tree, ruleNames, indent = 0):
    if isinstance(tree, TerminalNodeImpl):
        if not re.match(r"\r?\n[ \t]*",tree.getText()):
            print("{0}TOKEN '{1}'".format("  " * indent, tree.getText()))
    else:
        print("{0}{1}".format("  " * indent, ruleNames[tree.getRuleIndex()]))
        for child in tree.children:
            process(child,ruleNames,indent+1)

if __name__ == '__main__':
    main(sys.argv)
