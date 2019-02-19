import unittest
import src.util as util
import src.cwlBrowser as c

class WorkFlowInstantiationTest(unittest.TestCase) :

	def setUp(self):
		self.stepInput= {'step input' : {'type' : 'File', 'doc' : 'Belongs to test step'}}
		self.stepOutput = {'step output' : {'type' : 'File', 'doc' : 'This is an output'}}
		self.input1Attributes =  {'type' : 'type1', 'doc' : 'Input test'}
		self.input2Attributes = {'type' : 'type2', 'doc' : 'Input'}
		self.step1Attributes = {'run' : 'run1.cwl', 'doc' : 'Step test', 'in' : self.stepInput, 'out' : self.stepOutput}
		self.step2Attributes = {'run' : 'run2.cwl', 'doc' : 'Step test', 'in' : self.stepInput, 'out' : self.stepOutput}
		self.output1Attributes = {'type' : 'type1', 'doc' : 'Output Test', 'outputSource' : 'something/something'}
		self.output2Attributes = {'type' : 'type2', 'doc' : 'Output test', 'outputSource' : 'something/something'}
		self.output3Attributes = 'example1'
		self.output4Attributes = 'example2'
		self.workFlowGraph = {'something' : []}


	def instantiation_test(self, style, type, attributeDict1, attributeDict2) :
		instantiatedResult = []
		if style == 'dict':		
			array = {}
			#TEST array
			array['example1'] = attributeDict1;
			array['example2'] = attributeDict2;
		elif style == 'list_of_dicts' :
			array = []
			attributeDict1['id'] = 'example1'
			attributeDict2['id'] = 'example2'
			array.append(attributeDict1)
			array.append(attributeDict2)
		else :
			array = []
			array.append(attributeDict1)
			array.append(attributeDict2)
		if type == 'input' :
			instantiatedResult = util.instantiateInputs(array, self.workFlowGraph, step=False)
		elif type == 'step' :
			instantiatedResult = c.instantiateSteps(array, self.workFlowGraph)
		else :
			instantiatedResult = util.instantiateOutputs(array, self.workFlowGraph, step=False)
		self.assertEqual(instantiatedResult[0].name, 'example1')
		self.assertEqual(instantiatedResult[1].name, 'example2')
		if type == 'step' :
			i = 1
			for step in instantiatedResult :
				self.assertEqual(step.run, 'run{}.cwl'.format(i))
				for input_ in step.inputs :
					self.assertEqual(input_.name, "step input")
					self.assertEqual(input_.type, "File")
				for output in step.outputs :
					self.assertEqual(output.name, "step output")
					self.assertEqual(output.type, "File")
				i = i + 1
		#either input or output
		else:
			i = 1
			for io in instantiatedResult :
				if not (io.type == 'not known') :
					self.assertEqual(io.type, 'type{}'.format(i))
				else :
					self.assertEqual(io.type, 'not known')
				i = i + 1
		return


	def test_instantiation(self) :
		self.instantiation_test('dict','input',self.input1Attributes, self.input2Attributes)
		self.instantiation_test('dict','step', self.step1Attributes, self.step2Attributes)
		self.instantiation_test('dict', 'output',self.output1Attributes, self.output2Attributes)
		self.instantiation_test('list_of_dicts','input', self.input1Attributes, self.input2Attributes)
		self.instantiation_test('list_of_dicts', 'step', self.step1Attributes, self.step2Attributes)
		self.instantiation_test('list_of_dicts', 'output', self.output1Attributes, self.output2Attributes)
		self.instantiation_test('list_of_strings', 'output',self.output3Attributes, self.output4Attributes)



if __name__ == '__main__':
    unittest.main()
