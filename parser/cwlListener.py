# Generated from cwl.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cwlParser import cwlParser
else:
    from cwlParser import cwlParser

# This class defines a complete listener for a parse tree produced by cwlParser.
class cwlListener(ParseTreeListener):

    # Enter a parse tree produced by cwlParser#main_file.
    def enterMain_file(self, ctx:cwlParser.Main_fileContext):
        pass

    # Exit a parse tree produced by cwlParser#main_file.
    def exitMain_file(self, ctx:cwlParser.Main_fileContext):
        pass


    # Enter a parse tree produced by cwlParser#workflow.
    def enterWorkflow(self, ctx:cwlParser.WorkflowContext):
        pass

    # Exit a parse tree produced by cwlParser#workflow.
    def exitWorkflow(self, ctx:cwlParser.WorkflowContext):
        pass


    # Enter a parse tree produced by cwlParser#tool.
    def enterTool(self, ctx:cwlParser.ToolContext):
        pass

    # Exit a parse tree produced by cwlParser#tool.
    def exitTool(self, ctx:cwlParser.ToolContext):
        pass


    # Enter a parse tree produced by cwlParser#label.
    def enterLabel(self, ctx:cwlParser.LabelContext):
        pass

    # Exit a parse tree produced by cwlParser#label.
    def exitLabel(self, ctx:cwlParser.LabelContext):
        pass


    # Enter a parse tree produced by cwlParser#doc.
    def enterDoc(self, ctx:cwlParser.DocContext):
        pass

    # Exit a parse tree produced by cwlParser#doc.
    def exitDoc(self, ctx:cwlParser.DocContext):
        pass


    # Enter a parse tree produced by cwlParser#description.
    def enterDescription(self, ctx:cwlParser.DescriptionContext):
        pass

    # Exit a parse tree produced by cwlParser#description.
    def exitDescription(self, ctx:cwlParser.DescriptionContext):
        pass


    # Enter a parse tree produced by cwlParser#inputs.
    def enterInputs(self, ctx:cwlParser.InputsContext):
        pass

    # Exit a parse tree produced by cwlParser#inputs.
    def exitInputs(self, ctx:cwlParser.InputsContext):
        pass


    # Enter a parse tree produced by cwlParser#outputs.
    def enterOutputs(self, ctx:cwlParser.OutputsContext):
        pass

    # Exit a parse tree produced by cwlParser#outputs.
    def exitOutputs(self, ctx:cwlParser.OutputsContext):
        pass


    # Enter a parse tree produced by cwlParser#steps.
    def enterSteps(self, ctx:cwlParser.StepsContext):
        pass

    # Exit a parse tree produced by cwlParser#steps.
    def exitSteps(self, ctx:cwlParser.StepsContext):
        pass


    # Enter a parse tree produced by cwlParser#step.
    def enterStep(self, ctx:cwlParser.StepContext):
        pass

    # Exit a parse tree produced by cwlParser#step.
    def exitStep(self, ctx:cwlParser.StepContext):
        pass


    # Enter a parse tree produced by cwlParser#in_.
    def enterIn_(self, ctx:cwlParser.In_Context):
        pass

    # Exit a parse tree produced by cwlParser#in_.
    def exitIn_(self, ctx:cwlParser.In_Context):
        pass


    # Enter a parse tree produced by cwlParser#out_.
    def enterOut_(self, ctx:cwlParser.Out_Context):
        pass

    # Exit a parse tree produced by cwlParser#out_.
    def exitOut_(self, ctx:cwlParser.Out_Context):
        pass


    # Enter a parse tree produced by cwlParser#in_or_out.
    def enterIn_or_out(self, ctx:cwlParser.In_or_outContext):
        pass

    # Exit a parse tree produced by cwlParser#in_or_out.
    def exitIn_or_out(self, ctx:cwlParser.In_or_outContext):
        pass


    # Enter a parse tree produced by cwlParser#run.
    def enterRun(self, ctx:cwlParser.RunContext):
        pass

    # Exit a parse tree produced by cwlParser#run.
    def exitRun(self, ctx:cwlParser.RunContext):
        pass


    # Enter a parse tree produced by cwlParser#input_.
    def enterInput_(self, ctx:cwlParser.Input_Context):
        pass

    # Exit a parse tree produced by cwlParser#input_.
    def exitInput_(self, ctx:cwlParser.Input_Context):
        pass


    # Enter a parse tree produced by cwlParser#output.
    def enterOutput(self, ctx:cwlParser.OutputContext):
        pass

    # Exit a parse tree produced by cwlParser#output.
    def exitOutput(self, ctx:cwlParser.OutputContext):
        pass


    # Enter a parse tree produced by cwlParser#source.
    def enterSource(self, ctx:cwlParser.SourceContext):
        pass

    # Exit a parse tree produced by cwlParser#source.
    def exitSource(self, ctx:cwlParser.SourceContext):
        pass


    # Enter a parse tree produced by cwlParser#name.
    def enterName(self, ctx:cwlParser.NameContext):
        pass

    # Exit a parse tree produced by cwlParser#name.
    def exitName(self, ctx:cwlParser.NameContext):
        pass


    # Enter a parse tree produced by cwlParser#type_.
    def enterType_(self, ctx:cwlParser.Type_Context):
        pass

    # Exit a parse tree produced by cwlParser#type_.
    def exitType_(self, ctx:cwlParser.Type_Context):
        pass


    # Enter a parse tree produced by cwlParser#tag.
    def enterTag(self, ctx:cwlParser.TagContext):
        pass

    # Exit a parse tree produced by cwlParser#tag.
    def exitTag(self, ctx:cwlParser.TagContext):
        pass


    # Enter a parse tree produced by cwlParser#inputBinding.
    def enterInputBinding(self, ctx:cwlParser.InputBindingContext):
        pass

    # Exit a parse tree produced by cwlParser#inputBinding.
    def exitInputBinding(self, ctx:cwlParser.InputBindingContext):
        pass


    # Enter a parse tree produced by cwlParser#position.
    def enterPosition(self, ctx:cwlParser.PositionContext):
        pass

    # Exit a parse tree produced by cwlParser#position.
    def exitPosition(self, ctx:cwlParser.PositionContext):
        pass


    # Enter a parse tree produced by cwlParser#prefix.
    def enterPrefix(self, ctx:cwlParser.PrefixContext):
        pass

    # Exit a parse tree produced by cwlParser#prefix.
    def exitPrefix(self, ctx:cwlParser.PrefixContext):
        pass


    # Enter a parse tree produced by cwlParser#identification.
    def enterIdentification(self, ctx:cwlParser.IdentificationContext):
        pass

    # Exit a parse tree produced by cwlParser#identification.
    def exitIdentification(self, ctx:cwlParser.IdentificationContext):
        pass


    # Enter a parse tree produced by cwlParser#outputSource.
    def enterOutputSource(self, ctx:cwlParser.OutputSourceContext):
        pass

    # Exit a parse tree produced by cwlParser#outputSource.
    def exitOutputSource(self, ctx:cwlParser.OutputSourceContext):
        pass


    # Enter a parse tree produced by cwlParser#class_.
    def enterClass_(self, ctx:cwlParser.Class_Context):
        pass

    # Exit a parse tree produced by cwlParser#class_.
    def exitClass_(self, ctx:cwlParser.Class_Context):
        pass


    # Enter a parse tree produced by cwlParser#baseCommand.
    def enterBaseCommand(self, ctx:cwlParser.BaseCommandContext):
        pass

    # Exit a parse tree produced by cwlParser#baseCommand.
    def exitBaseCommand(self, ctx:cwlParser.BaseCommandContext):
        pass


    # Enter a parse tree produced by cwlParser#stdin_.
    def enterStdin_(self, ctx:cwlParser.Stdin_Context):
        pass

    # Exit a parse tree produced by cwlParser#stdin_.
    def exitStdin_(self, ctx:cwlParser.Stdin_Context):
        pass


    # Enter a parse tree produced by cwlParser#stdout_.
    def enterStdout_(self, ctx:cwlParser.Stdout_Context):
        pass

    # Exit a parse tree produced by cwlParser#stdout_.
    def exitStdout_(self, ctx:cwlParser.Stdout_Context):
        pass


    # Enter a parse tree produced by cwlParser#default.
    def enterDefault(self, ctx:cwlParser.DefaultContext):
        pass

    # Exit a parse tree produced by cwlParser#default.
    def exitDefault(self, ctx:cwlParser.DefaultContext):
        pass


    # Enter a parse tree produced by cwlParser#version.
    def enterVersion(self, ctx:cwlParser.VersionContext):
        pass

    # Exit a parse tree produced by cwlParser#version.
    def exitVersion(self, ctx:cwlParser.VersionContext):
        pass


