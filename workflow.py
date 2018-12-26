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


	def printInputs(self):
		util.printInputArray(self.name, self.inputArray)


	def printOutputs(self):
		util.printOutputArray(self.name, self.outputArray)

	def printSteps(self):
		print(self.name + " STEPS")
		for step in self.stepArray:
			print("Name: {0}".format(step.name))
			util.printInputArray(step.name, step.inputArray)
			util.printOutputArray(step.name, step.outputArray)
			print("\n")

	





class Step:
	def __init__(self, name, in_, run, out):
		self.name = name
		self.in_ = in_
		self.out = out
		self.inputArray = util.instantiateInputs(in_)
		self.outputArray = util.instantiateOutputs(out)
		self.run = run


class Input:
	def __init__(self, name, type):
		self.name = name
		self.type = type

class Output:
	def __init__(self, name, type):
		self.name = name
		self.type = type