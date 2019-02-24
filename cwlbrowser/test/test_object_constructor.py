import unittest
import cwlbrowser.browser as c 
import cwlbrowser.util as util
import cwlbrowser.workflow as wf

lobstrDict = {'cwlVersion': 'v1.0', 'class': 'Workflow', 
				'inputs': 
				{'p1': {'type': 'File[]?', 'description': 'list of files containing the first end of paired end reads in fasta or fastq format'}, 
				'p2': {'type': 'File[]?', 'description': 'list of files containing the second end of paired end reads in fasta or fastq format'}, 
				'output_prefix': {'type': 'string', 'description': 'prefix for output files. will output prefix.aligned.bam and prefix.aligned.stats'}, 
				'reference': {'type': 'File', 'description': "lobSTR's bwa reference files"}, 
				'rg-sample': {'type': 'string', 'description': 'Use this in the read group SM tag'}, 
				'rg-lib': {'type': 'string', 'description': 'Use this in the read group LB tag'}, 
				'strinfo': {'type': 'File', 'description': 'File containing statistics for each STR.'}, 
				'noise_model': {'type': 'File', 'description': 'File to read noise model parameters from (.stepmodel)', 
				'secondaryFiles': ['^.stuttermodel']}}, 
				'outputs': {'bam': {'type': 'File', 'outputSource': 'samindex/bam_with_bai'}, 'bam_stats': {'type': 'File', 'outputSource': 'lobSTR/bam_stats'}, 'vcf': {'type': 'File', 'outputSource': 'allelotype/vcf'}, 'vcf_stats': {'type': 'File', 'outputSource': 'allelotype/vcf_stats'}}, 'hints': {'DockerRequirement': {'dockerPull': 'rabix/lobstr'}}, 'steps': {'lobSTR': {'run': 'lobSTR-tool.cwl', 'in': {'p1': 'p1', 'p2': 'p2', 'output_prefix': 'output_prefix', 'reference': 'reference', 'rg-sample': 'rg-sample', 'rg-lib': 'rg-lib'}, 'out': ['bam', 'bam_stats']}, 'samsort': {'run': 'samtools-sort.cwl', 'in': {'input': 'lobSTR/bam', 'output_name': {'default': 'aligned.sorted.bam'}}, 'out': ['output_file']}, 'samindex': {'run': 'samtools-index.cwl', 'in': {'input': 'samsort/output_file'}, 'out': ['bam_with_bai']}, 'allelotype': {'run': 'allelotype.cwl', 'in': {'bam': 'samindex/bam_with_bai', 'reference': 'reference', 'output_prefix': 'output_prefix', 'noise_model': 'noise_model', 'strinfo': 'strinfo'}, 'out': ['vcf', 'vcf_stats']}}}

concordanceDict = {'class': 'Workflow', 'doc': 'Workflow to compare overlapping variants in two VCFs using GATK Concordance tool.\n', 'cwlVersion': 'v1.0', 'id': 'concordance-test-workflow', 
							'requirements': [{'class': 'InlineJavascriptRequirement'}, {'class': 'ShellCommandRequirement'}], 
							'inputs': [{'id': 'reference', 'type': 'File', 'secondaryFiles': ['^.dict', '.fai']}, {'id': 'eval', 'type': 'File', 'secondaryFiles': ['.tbi']}, {'id': 'truth', 'type': 'File', 'secondaryFiles': ['.tbi']}, {'id': 'summary', 'type': 'string'}], 'outputs': [{'id': 'concordance_summary', 'type': 'File', 'outputSource': 'GATKConcordance/concordance_summary'}], 'steps': [{'id': 'GATKConcordance', 'run': './GATKConcordance.yaml.cwl', 'in': 
							[{'id': 'reference', 'source': 'reference'}, {'id': 'eval', 'source': 'eval'}, {'id': 'truth', 'source': 'truth'}, {'id': 'summary', 'source': 'summary'}], 'out': None}]}

#Tests processing of workflows after being parsed by YAML parser
class LobstrTest(unittest.TestCase) :
	def setUp(self) :
        #expected attributes for lobSTR.cwl, a non-id type workflow

        #names of inputs/outputs/steps
		self.expectedInputs = ['p1', 'p2', 'output_prefix', 'reference', 'rg-sample',
									 'rg-lib', 'strinfo', 'noise_model']
		self.expectedOutputs= ['bam', 'bam_stats', 'vcf', 'vcf_stats']
		self.expectedSteps = ['lobSTR', 'samsort', 'samindex', 'allelotype' ]

		#types of inputs/outputs
		self.expectedInputTypes = ["File[]?","File[]?","string","File","string","string","File","File"]	
		self.expectedOutputTypes = ["File","File","File","File"]

		#runs(implementations) of steps
		self.expectedStepRuns = ["lobSTR-tool.cwl","samtools-sort.cwl","samtools-index.cwl","allelotype.cwl"]

		#workflow after being parsed by workflow parser
		self.lobSTR = lobstrDict

	"""Tests the creation of a workflow object for a non-id type workflow (workflow whose elements are
	  not identified with an id field)"""
	def test_instantiation_for_lobstr(self) :
		lobstr_workflow = wf.Workflow('lobSTR.cwl', self.lobSTR)
		self.assertEqual(lobstr_workflow.getInputsByName(), self.expectedInputs)
		self.assertEqual(lobstr_workflow.getOutputsByName(), self.expectedOutputs)
		self.assertEqual(lobstr_workflow.getStepsByName(), self.expectedSteps)
		self.assertEqual(lobstr_workflow.getInputsByType(), self.expectedInputTypes)
		self.assertEqual(lobstr_workflow.getOutputsByType(), self.expectedOutputTypes)
		self.assertEqual(lobstr_workflow.getStepsByRun(), self.expectedStepRuns)

class LobstrStepTest(unittest.TestCase) :
	def setUp(self) :
		self.expectedInputs = ["p1", "p2", "output_prefix", "reference", "rg-sample", "rg-lib"]
		self.expectedOutputs = ["bam", "bam_stats"]
		self.expectedOutputTypes = ["not known", "not known"]
		self.expectedInputTypes = ["not known", "not known", "not known", "not known", "not known", "not known"]
		self.lobstr = lobstrDict
	def test_instantiation_of_lobstr_step(self) :
		lobstr_workflow = wf.Workflow('lobstr', self.lobstr)
		self.assertEqual(lobstr_workflow.steps[0].getInputsByName(), self.expectedInputs)
		self.assertEqual(lobstr_workflow.steps[0].getOutputsByName(), self.expectedOutputs)
		self.assertEqual(lobstr_workflow.steps[0].getInputsByType(), self.expectedInputTypes)
		self.assertEqual(lobstr_workflow.steps[0].getOutputsByType(), self.expectedOutputTypes)

	
class ConcordanceTest(unittest.TestCase) :
	def setUp(self) :
		#expected attributes for Concordance.cwl, an ID type workflow
		self.expectedInputs = ["reference","eval","truth","summary"]
		self.expectedOutputs = ["concordance_summary"]
		self.expectedSteps =["GATKConcordance"]
		self.expectedInputTypes = ["File","File","File","string"]
		self.expectedOutputTypes = ["File"]
		self.expectedStepRuns = ["./GATKConcordance.yaml.cwl"]
		#parsed concordance workflow file
		self.concordance = concordanceDict

	"""Test the creation of a workflow object for an id type workflow (workflow whose elements are 
		identified with an id field)"""
	def test_instantiation_of_concordance(self) :
		concordance_workflow = wf.Workflow('concordance.cwl', self.concordance)
		self.assertEqual(concordance_workflow.getInputsByName(), self.expectedInputs)
		self.assertEqual(concordance_workflow.getOutputsByName(), self.expectedOutputs)
		self.assertEqual(concordance_workflow.getStepsByName(), self.expectedSteps)
		self.assertEqual(concordance_workflow.getInputsByType(), self.expectedInputTypes)
		self.assertEqual(concordance_workflow.getOutputsByType(), self.expectedOutputTypes)
		self.assertEqual(concordance_workflow.getStepsByRun(), self.expectedStepRuns)

class ConcordanceStepTest(unittest.TestCase) :
	def setUp(self) :
		self.expectedInputs = ["reference" ,"eval" ,"truth" ,"summary" ]
		self.expectedInputTypes = ["not known", "not known", "not known", "not known"]
		self.expectedOutputs = []
		self.concordance = concordanceDict

	def test_instantiation_of_concordance_step(self) :
		concordance_workflow = wf.Workflow('concordance_workflow', self.concordance)
		self.assertEqual(concordance_workflow.steps[0].getInputsByName(), self.expectedInputs)
		self.assertEqual(concordance_workflow.steps[0].getInputsByType(), self.expectedInputTypes)
		self.assertEqual(concordance_workflow.steps[0].getOutputsByName(), self.expectedOutputs)
		self.assertEqual(concordance_workflow.steps[0].getOutputsByType(), self.expectedOutputs)

if __name__ == '__main__':
    unittest.main()
