import sys
from antlr4 import *
from cwlLexer import cwlLexer
from cwlParser import cwlParser
from customcwlListener import customcwlListener
def main(argv):
    input = FileStream(argv[1])
    lexer = cwlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = cwlParser(stream)
    tree = parser.workflow()

    output = open('cwl.txt', 'w')
    customcwlListen = customcwlListener(output)
    walker = ParseTreeWalker()
    walker.walk(customcwlListen, tree)

    output.close()

if __name__ == '__main__':
    main(sys.argv)
