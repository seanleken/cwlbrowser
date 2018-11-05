import sys
from antlr4 import *
from cwlParser import cwlParser
from cwlListener import cwlListener

class customcwlListener(cwlListener) :
    def __init__(self, output):
        self.output = output
