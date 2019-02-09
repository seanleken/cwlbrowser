import unittest
import cwlBrowser as c

class WorkFlowBrowserTest(unittest.TestCase) :
	def test_loading(self):
		link = "https://github.com/seanleken/workflowtest/blob/master/workflows/arithmeticfunction1.cwl"
		
		c.load(link, link=True)
		self.assertTr