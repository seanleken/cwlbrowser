import unittest
import cwlbrowser.util as util

parentLink = "https://github.com/alexbarrera/GGR-cwl/blob/master/v1.0/RNA-seq_pipeline/02-trim-pe.cwl"
run = "../trommatic/trommatic.cwl"
run2 = "trommatic.cwl"
expected = "https://github.com/alexbarrera/GGR-cwl/blob/master/v1.0/trommatic/trommatic.cwl"
expected2 = "https://github.com/alexbarrera/GGR-cwl/blob/master/v1.0/RNA-seq_pipeline/trommatic.cwl"

class LinkConstructorTest(unittest.TestCase) :
	def test_correct_final_link_higher_level(self) :
		finallink = util.constructLink(parentLink, run)
		self.assertEqual(finallink, expected)

	def test_correct_final_link_same_level(self) :
		finallink = util.constructLink(parentLink, run2)
		self.assertEqual(finallink, expected2)

