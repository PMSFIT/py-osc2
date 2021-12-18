import sys
from antlr4 import *
from openscenario2Parser import openscenario2Parser
from openscenario2Lexer import openscenario2Lexer
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = openscenario2Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = openscenario2Parser(stream)
    tree = parser.osc_file()
    print(tree.toStringTree(openscenario2Parser.ruleNames))
 
if __name__ == '__main__':
    main(sys.argv)
