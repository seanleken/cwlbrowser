import unittest
import cwlBrowser as c
import util
import workflow

class WorkFlowBrowserTest(unittest.TestCase) :
	def test_input_instantiation(self):
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
			self.assertTrue(result.name == "input{}".format(i))
			self.assertTrue(result.type == "string")



if __name__ == '__main__':
    unittest.main()
