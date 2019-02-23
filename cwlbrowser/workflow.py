import cwlbrowser.util as util
import cwlbrowser.step as s
UNKNOWN = "not known"

class Workflow:
	def __init__(self, name, workflow):
		self.name = name;
		self.inputs = self.createInputOutputArray(workflow["inputs"])
		self.outputs = self.createInputOutputArray(workflow["outputs"])
		self.steps = self.createStepArray(workflow["steps"])

	def createStepArray(self, steps) :
		temp = []
		#print (steps)
		if (isinstance(steps, dict)) :
			for key, value in steps.items() :
				stepObj = s.Step(value, name=key)
				temp.append(stepObj)
		else :
			for step in steps :
				stepObj = s.Step(step)
				temp.append(stepObj)
		return temp


	def createInputOutputArray(self, elements) :
		return util.createInputOutputArray(elements)


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



