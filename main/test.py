import unittest
import util

class WorkFlowInstantiationTest(unittest.TestCase) :

	def test_input_instantiation_dict(self, ):
		inputs = {}
		resultArray = []
		workFlowGraph = {}
		inputs['input1'] = {'type' : 'string', 'doc' : 'First input'}
		inputs['input2'] = {'type' : 'string', 'doc' : 'Second input'}
		inputs['input3'] = {'type' : 'string', 'doc' : 'Third input'}
		resultArray = util.instantiateInputs(inputs, workFlowGraph, step=False)
		i = 0
		for result in resultArray :
			i = i + 1
			self.assertEqual(result.name, "input{}".format(i))
			self.assertEqual(result.type, "string")

	def test_input_instantiation_list(self):
		inputs = []
		resultArray = []
		workFlowGraph = {}
		inputs.append({'id' : 'input1','type' : 'string', 'doc' : 'First input'})
		inputs.append({'id' : 'input2','type' : 'string', 'doc' : 'Second input'})
		inputs.append({'id' : 'input3','type' : 'string', 'doc' : 'Third input'})
		resultArray = util.instantiateInputs(inputs, workFlowGraph, step=False)
		i = 0
		for result in resultArray :
			i = i + 1
			self.assertEqual(result.name, "input{}".format(i))
			self.assertEqual(result.type, "string")




if __name__ == '__main__':
    unittest.main()
