STEPS_WEIGHTING = 70
IO_WEIGHTING = 15

class SimilarityChecker:
	def __init__(self) :
		self.overallMatch = 0
		self.workflow1 = []
		self.workflow2 = []
		self.inputsThatDifferWorkflow1 = []
		self.inputsThatDifferWorkflow2 = []
		self.outputsThatDifferWorkflow1 = []
		self.outputsThatDifferWorkflow2 = []
		self.stepsThatDifferWorkflow1 = []
		self.stepsThatDifferWorkflow2 = []
		self.matchingItems = []


	def similarityCheck(self, workflow1, workflow2):
		self.workflow1 = workflow1
		self.workflow2 = workflow2
		stepSimilarity = self.similarityCheckSteps()
		inputSimilarity = self.similarityCheckInputs()
		outputSimilarity = self.similarityCheckOutputs()
		self.overallMatch = stepSimilarity + inputSimilarity + outputSimilarity

	def similarityCheckSteps(self):
		workflow1Steps =self.workflow1.getStepsByName()
		workflow2Steps = self.workflow2.getStepsByName()
		(diff1, diff2) = self.getDifferences(workflow1Steps, workflow2Steps)
		self.stepsThatDifferWorkflow1 = diff1
		self.stepsThatDifferWorkflow2 = diff2

		return self.getPercentageMatch(workflow1Steps, workflow2Steps, STEPS_WEIGHTING)


	def similarityCheckInputs(self):
		workflow1Inputs =self.workflow1.getInputsByName()
		workflow2Inputs = self.workflow2.getInputsByName()
		(diff1, diff2) = self.getDifferences(workflow1Inputs, workflow2Inputs)
		self.inputsThatDifferWorkflow1 = diff1
		self.inputsThatDifferWorkflow2 = diff2
		return self.getPercentageMatch(workflow1Inputs, workflow2Inputs, IO_WEIGHTING)

	def similarityCheckOutputs(self):
		workflow1Outputs =self.workflow1.getOutputsByName()
		workflow2Outputs = self.workflow2.getOutputsByName()
		(diff1, diff2) = self.getDifferences(workflow1Outputs, workflow2Outputs)
		self.outputsThatDifferWorkflow1 = diff1
		self.outputsThatDifferWorkflow2 = diff2
		return self.getPercentageMatch(workflow1Outputs, workflow2Outputs, IO_WEIGHTING)


	def getPercentageMatch(self, workflow1Attributes, workflow2Attributes, weighting) :
		if len(workflow1Attributes) >= len(workflow2Attributes) :
			matchingItems = set(workflow2Attributes).intersection(workflow1Attributes)
			denominator = len(workflow1Attributes)
		else :
			matchingItems = set(workflow1Attributes).intersection(workflow2Attributes)
			denominator = len(workflow2Attributes)
		if denominator <= 0 :
			denominator = 1
		return len(matchingItems) / denominator * weighting

	def getDifferences(self, workflow1Attributes, workflow2Attributes) :
		difference1 = set(workflow1Attributes).difference(workflow2Attributes)
		difference2 = set(workflow2Attributes).difference(workflow1Attributes)
		return difference1, difference2

	def getOverallMatch(self) :
		return self.overallMatch

	def getDifferingInputs(self) :
		return self.getDifferingItems(self.inputsThatDifferWorkflow1, self.inputsThatDifferWorkflow2)

	def getDifferingSteps(self) :
		return self.getDifferingItems(self.stepsThatDifferWorkflow1, self.stepsThatDifferWorkflow2)

	def getDifferingOutputs(self) :
		return self.getDifferingItems(self.outputsThatDifferWorkflow1, self.outputsThatDifferWorkflow2)


	def getDifferingItems(self, set1, set2) :
		differingItems = []
		for i in set1 :
			differingItems.append(i)
		for i in set2 :
			differingItems.append(i)
		return differingItems