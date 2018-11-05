import sys
from antlr4 import *
from cwlParser import cwlParser
from cwlListener import cwlListener
from antlr4.error.ErrorListener import *
import io

class cwlErrorListener(ErrorListener):

    def __init__(self, output):
        self.output = output
        self._symbol = ''

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.output.write(msg)
        self._symbol = offendingSymbol.text

    @property
    def symbol(self):
        return self._symbol
