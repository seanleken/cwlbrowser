import sys
from antlr4 import *
from cwlParser import cwlParser
from cwlListener import cwlListener

class customcwlListener(cwlListener) :
    def __init__(self, output):
        self.output = output

    def enterInputs(self, ctx:cwlParser.InputsContext) :
        self.output.write('Input:\n')

    def exitInputs(self, ctx:cwlParser.InputsContext) :
        for child in ctx.children :
            if isinstance(child, cwlParser.Input_Context) :
                self.output.write(child.getText())
                self.output.write("--")
                self.output.write("\n")

    def enterOutputs(self, ctx:cwlParser.OutputsContext) :
        self.output.write('Output:\n')

    def exitOutputs(self, ctx:cwlParser.OutputsContext) :
        for child in ctx.children :
            if isinstance(child, cwlParser.OutputContext) :
                self.output.write(child.getText())
                self.output.write("--\n")

    def enterStep(self, ctx:cwlParser.StepContext) :
        self.output.write("\nstep found")

    def exitStep(self, ctx:cwlParser.StepContext) :
        self.output.write("\nstep exited")
        for child in ctx.children :
            self.output.write(child.getText())

    """def exitTool(self, ctx:cwlParser.ToolContext) :
        for child in ctx.children :
            self.output.write(child.getText())"""


   
