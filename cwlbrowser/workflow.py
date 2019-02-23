import cwlbrowser.util as util

class Workflow:
	def __init__(self, name):
		self.name = name;
		self.inputs = []
		self.steps = []
		self.outputs = []

	def getInputsByName(self) :
		temp = []
		for input_ in self.inputs :
			temp.append(input_.name)
		return temp

	def getInputsByType(self) :
		temp = []
		for input_ in self.inputs :
			temp.append(input_.type)
		return temp

	def getOutputsByName(self) :
		temp = []
		for output in self.outputs :
			temp.append(output.name)
		return temp

	def getOutputsByType(self) :
		temp = []
		for output in self.outputs :
			temp.append(output.type)
		return temp

	def getStepsByName(self) :
		temp = []
		for step in self.steps :
			temp.append(step.name)
		return temp

	def getStepsByRun(self) :
		temp = []
		for step in self.steps :
			temp.append(step.run)
		return temp



class Step:
	def __init__(self, name, in_, run, out):
		self.name = name
		self.inputs = util.instantiateInputs(in_)
		self.outputs = util.instantiateOutputs(out)
		self.run = run

		
	def getInputsByName(self) :
		temp = []
		for input_ in self.inputs :
			temp.append(input_.name)
		return temp

	def getInputsByType(self) :
		temp = []
		for input_ in self.inputs :
			temp.append(input_.type)
		return temp

	def getOutputsByName(self) :
		temp = []
		for output in self.outputs :
			temp.append(output.name)
		return temp


	def getOutputsByType(self) :
		temp = []
		for output in self.outputs :
			temp.append(output.type)
		return temp

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