import sys
from antlr4 import *
from cwlParser import cwlParser
from cwlListener import cwlListener

class customcwlListener(cwlListener) :
    def __init__(self, output):
        self.output = output

    def enterInputs(self, ctx:cwlParser.InputsContext) :
        self.output.write('\nInput:')

    def exitInputs(self, ctx:cwlParser.InputsContext) :
        for child in ctx.children :
            self.output.write(child.getText())
            self.output.write("--")
            self.output.write("\n\n")

    def enterOutputs(self, ctx:cwlParser.OutputsContext) :
        self.output.write('\nOutput:')

    def exitOutputs(self, ctx:cwlParser.OutputsContext) :
        for child in ctx.children :
            self.output.write(child.getText())

    def enterStep(self, ctx:cwlParser.StepContext) :
        self.output.write("\nstep found")

    def exitStep(self, ctx:cwlParser.StepContext) :
        self.output.write("\nstep exited")
