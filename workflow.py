import util

class Workflow:
	def __init__(self, name, inputs, outputs, steps):
		self.name = name;
		self.inputs = inputs
		self.inputArray = []
		self.outputArray = []
		self.stepArray = []
		self.outputs = outputs
		self.steps = steps
		self.graph = {}


	def printInputs(self):
		util.printInputArray(self.name, self.inputArray)


	def printOutputs(self):
		util.printOutputArray(self.name, self.outputArray)

	def printSteps(self, detailed=False):
		print("------------------------------------------------")
		print(self.name + " STEPS")
		if(detailed == True) :
			for step in self.stepArray:
				print("-------------------------------------------------")
				print("STEP Name: {0}".format(step.name))
				print("-----------------------------------------------")
				util.printInputArray(step.name, step.inputArray)
				util.printOutputArray(step.name, step.outputArray)
				print("")
		else:
			run = []
			for step in self.stepArray :
				if not (isinstance(step.run, str)) :
					run = "local CommandLineTool"
				else :
					run = step.run
				print("STEP Name: {0} Run: {1}".format(step.name, run))

		print("-------------------------------------------------")

	def printGraph(self):
		print(self.graph)

	





class Step:
	def __init__(self, name, in_, run, out, workflowGraph):
		self.name = name
		self.in_ = in_
		self.out = out
		self.inputArray = util.instantiateInputs(in_, workflowGraph, step=True, stepName=name)
		self.outputArray = util.instantiateOutputs(out, workflowGraph, step=True)
		self.run = run
		#__str__(self) ==

class Input:
	def __init__(self, name, type, source="WORKFLOW"):
		self.name = name
		self.type = type
		self.source = source

class Output:
	def __init__(self, name, type, source="WORKFLOW"):
		self.name = name
		self.type = type
		self.source = source