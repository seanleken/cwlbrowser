import util

class Workflow:
	def __init__(self, name, inputs, outputs, steps):
		self.name = name;
		self.inputs = inputs
		self.outputs = outputs
		self.steps = steps

	def printSteps(self):
		util.printAttr(self.steps, "Steps", self.name)


	def printInputs(self):
		util.printAttr(self.inputs, "Inputs", self.name)

	def printOutputs(self):
		util.printAttr(self.outputs, "Outputs", self.name)

	





"""class Step:
	def __init__(self, name, in_, out, run, baseCommand):
		self.in_ = in_
		self.out = out
		self.run = run
		self.baseCommand

for k, v in self.step.items()
	step = Step(k, v[in_], v[out], v[run], v[baseCommand])
	util.printAttr(step.in, step)
class Input:
	def __init__(self, type)
		self.type = type

class Output:
	def __init__(self, type)
		self.type = type"""