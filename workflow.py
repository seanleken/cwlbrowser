class Workflow:
	def __init__(self, name, inputs, outputs, steps):
		self.name = name;
		self.inputs = inputs
		self.outputs = outputs
		self.steps = steps


"""class Step:
	def __init__(self, in_, out, baseCommand):
		self.in_ = in_
		self.out = out
		self.baseCommand

class Input:
	def __init__(self, type)
		self.type = type

class Output:
	def __init__(self, type)
		self.type = type"""