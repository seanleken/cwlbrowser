from antlr4 import *
from cwlLexer import cwlLexer
from cwlParser import cwlParser
#from HtmlChatListener import HtmlChatListener
from cwlErrorListener import cwlErrorListener
import unittest
import io

class TestcwlParser(unittest.TestCase):

    def setup(self, text):
        lexer = cwlLexer(InputStream(text))
        stream = CommonTokenStream(lexer)
        parser = cwlParser(stream)

        self.output = io.StringIO()
        self.error = io.StringIO()

        parser.removeErrorListeners()
        errorListener = cwlErrorListener(self.error)
        parser.addErrorListener(errorListener)

        self.errorListener = errorListener

        return parser

    def test_valid_doc(self):
        parser = self.setup('doc: "This a doc" ')
        tree = parser.doc()

        cwlListen = cwlListener(self.output)
        walker = ParseTreeWalker()
        walker.walk(cwlListen, tree)

        # let's check that there aren't any symbols in errorListener
        self.assertEqual(len(self.errorListener.symbol), 0)

    def test_invalid_name(self):
        parser = self.setup('doc: "This is a doc"- ')
        tree = parser.doc()

        cwlListen = cwlListener(self.output)
        walker = ParseTreeWalker()
        walker.walk(cwlListen, tree)

        # let's check the symbol in errorListener
        self.assertEqual(self.errorListener.symbol, '-')

if __name__ == '__main__':
    unittest.main()
