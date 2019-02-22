import cwlbrowser.util as util

class Workflow:
	def __init__(self, name):
		self.name = name;
		self.inputs = []
		self.inputNames = []
		self.inputTypes = []
		self.steps = []
		self.outputs = []


class Step:
	def __init__(self, name, in_, run, out):
		self.name = name
		self.inputs = util.instantiateInputs(in_)
		self.outputs = util.instantiateOutputs(out)
		self.run = run

	def __str__(self):
		return "Step: {0} | Run: {1}".format(self.name, self.run)

class Input:
	def __init__(self, name, type):
		self.name = name
		self.type = type

	def __str__(self):
		return "Input: {0} | Type: {1}".format(self.name, self.type)

class Output:
	def __init__(self, name, type):
		self.name = name
		self.type = type

	def __str__(self):
		return "Output: {0} | Type: {1}".format(self.name, self.type)