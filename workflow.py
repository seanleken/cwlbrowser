import util

class Workflow:
	def __init__(self, name, inputs, outputs, steps):
		self.name = name;
		self.inputs = inputs
		self.inputArray = []
		self.outputArray = []
		self.StepArray = []
		self.outputs = outputs
		self.steps = steps

	def printSteps(self):
		util.printAttr(self.steps, "Steps", self.name)


	def printInputs(self):
		util.printAttr(self.inputs, "Inputs", self.name)

	def printOutputs(self):
		util.printAttr(self.outputs, "Outputs", self.name)

	def printInputArray(self):
		print("Inputs")
		for input_ in self.inputArray:
			print("Name: {0} Type: {1}".format(input_.name, input_.type))

	def printOutputArray(self):
		print("Outputs")
		for output in self.outputArray:
			print("Name {0} Type: {1}".format(output.name, output.type))

	def printStepArray(self):
		print("Steps")
		for step in self.stepArray:
			print("Name {0}".format(step.name))
			print("Inputs{0}".format(step.in_))

	





class Step:
	def __init__(self, name, in_, run, out=[]):
		self.name = name
		self.in_ = in_
		#self.inputArray = util.instantiateInputs(in_)
		#self.outputArray = util.instantiateOutputs(out)
		self.out = out
		self.run = run


class Input:
	def __init__(self, name, type):
		self.name = name
		self.type = type

class Output:
	def __init__(self, name, type):
		self.name = name
		self.type = type