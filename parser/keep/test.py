import sys
from antlr4 import *
from cwlLexer import cwlLexer
from cwlParser import cwlParser
from cwlListener import cwlListener
def main(argv):
    input = FileStream(argv[1])
    lexer = cwlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = cwlParser(stream)
    tree = parser.workflow()

    cwlListen = cwlListener()
    walker = ParseTreeWalker()
    walker.walk(cwlListen, tree)

if __name__ == '__main__':
    main(sys.argv)
