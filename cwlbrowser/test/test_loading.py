import unittest
import cwlbrowser.browser as c 
import cwlbrowser.util as util
#Tests processing of workflows after being parsed by YAML parser
class LoadTest(unittest.TestCase) :
	expectedInputsForLobstr = []
	expectedOutputsForLobstr = []
	expectedStepsForLobstr = []
	expectedInputsForConcordance = []
	expectedOutputsForConcordance = []
	expectedStepsForConcordance = []
	expectedInputsForMain = []
	expectedOutputsForMain = []
	expectedStepsForMain = []
	lobSTR = {}
	concordance = {}
	main = {}

	@classmethod
	def setUpClass(cls) :
		global expectedInputsForLobstr
		global expectedOutputsForLobstr
		global expectedStepsForLobstr
		global expectedInputsForConcordance
		global expectedOutputsForConcordance
		global expectedStepsForConcordance
		global expectedInputsForMain
		global expectedOutputsForMain
		global expectedStepsForMain
		global lobSTR
		global concordance
		global main 

		expectedInputsForLobstr = ['p1', 'p2', 'output_prefix', 'reference', 'rg-sample',
									 'rg-lib', 'strinfo', 'noise_model']	
		expectedOutputsForLobstr = ['bam', 'bam_stats', 'vcf', 'vcf_stats']
		expectedStepsForLobstr = ['lobSTR', 'samsort', 'samindex', 'allelotype' ]
		expectedInputsForConcordance = ["reference","eval","truth","summary"]
		expectedOutputsForConcordance = ["concordance_summary"]
		expectedStepsForConcordance =["GATKConcordance"]
		expectedInputsForMain = ["TUMOR_FASTQ_1","TUMOR_FASTQ_2","cndaFa","gtffile","sqlitefile","txAnnofile"]
		lobSTR = {'cwlVersion': 'v1.0', 'class': 'Workflow', 
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

		concordance = {'class': 'Workflow', 'doc': 'Workflow to compare overlapping variants in two VCFs using GATK Concordance tool.\n', 'cwlVersion': 'v1.0', 'id': 'concordance-test-workflow', 
						'requirements': [{'class': 'InlineJavascriptRequirement'}, {'class': 'ShellCommandRequirement'}], 
						'inputs': [{'id': 'reference', 'type': 'File', 'secondaryFiles': ['^.dict', '.fai']}, {'id': 'eval', 'type': 'File', 'secondaryFiles': ['.tbi']}, {'id': 'truth', 'type': 'File', 'secondaryFiles': ['.tbi']}, {'id': 'summary', 'type': 'string'}], 'outputs': [{'id': 'concordance_summary', 'type': 'File', 'outputSource': 'GATKConcordance/concordance_summary'}], 'steps': [{'id': 'GATKConcordance', 'run': './GATKConcordance.yaml.cwl', 'in': 
						[{'id': 'reference', 'source': 'reference'}, {'id': 'eval', 'source': 'eval'}, {'id': 'truth', 'source': 'truth'}, {'id': 'summary', 'source': 'summary'}], 'out': None}]}


		main =  {'class': 'Workflow', 'cwlVersion': 'v1.0', 'dct:creator': {'@id': 'http://orcid.org/0000-0002-7681-6415', 'foaf:mbox': 'tnv@synapse.org', 'foaf:name': 'tnv'}, 'doc': 'SMC-RNA challenge fusion detection submission\nFusionRnadt workflow: gunzip, indexing,  fusion count, gene-fusion detection', 
					'hints': [], 'id': 'main', 
					'inputs': [{'id': 'TUMOR_FASTQ_1', 'type': 'File'}, {'id': 'TUMOR_FASTQ_2', 'type': 'File'}, {'id': 'cndaFa', 'type': 'File'}, {'id': 'gtffile', 'type': 'File'}, {'id': 'sqlitefile', 'type': 'File'}, {'id': 'txAnnofile', 'type': 'File'}], 'name': 'main', 
					'outputs': [{'id': 'OUTPUT', 'outputSource': 'runRscript/fusionout', 'type': 'File'}], 
					'steps': [{'id': 'FusionRnadt_counting', 'in': [{'id': 'fastq1', 'source': 'gunzipfastq1/output'}, 
					{'id': 'fastq2', 'source': 'gunzipfastq2/output'}, {'id': 'gtffn', 'source': 'gunzipgtffile/output'}, 
					{'id': 'indexDir', 'source': 'FusionRnadt_indexing/output'}, {'default': 'ISR', 'id': 'libtype'}, {'default': 'fusionCountRes', 'id': 'output_name'}, {'default': 8, 'id': 'threads'}], 'out': ['output'], 'run': 'extractFusionCount.cwl'}, {'id': 'FusionRnadt_indexing', 'in': [{'default': 'sailfish_Homo_sapiens_GRCh3775_cdna_all_idx', 'id': 'output_name'}, {'id': 'txFasta', 'source': 'gunzipcndaFa/output'}], 'out': ['output'], 'run': 'createIndex.cwl'}, {'id': 'gunzipcndaFa', 'in': [{'id': 'input', 'source': 'cndaFa'}], 'out': ['output'], 'run': 'gunzip.cwl'}, {'id': 'gunzipfastq1', 'in': [{'id': 'input', 'source': 'TUMOR_FASTQ_1'}], 'out': ['output'], 'run': 'gunzip.cwl'}, 
					{'id': 'gunzipfastq2', 'in': [{'id': 'input', 'source': 'TUMOR_FASTQ_2'}], 'out': ['output'], 'run': 'gunzip.cwl'}, {'id': 'gunzipgtffile', 'in': [{'id': 'input', 'source': 'gtffile'}], 'out': ['output'], 'run': 'gunzip.cwl'}, {'id': 'runRscript', 'in': [{'default': '/opt/tmpCodes/Rscripts/detectFusionGenes2.R', 'id': 'RscriptFile'}, {'id': 'fusionCountDir', 'source': 'FusionRnadt_counting/output'}, {'id': 'gtfSqlite', 'source': 'sqlitefile'}, {'default': 'fusionGenes.bedpe', 'id': 'output_name'}, {'id': 'txAnno', 'source': 'txAnnofile'}], 'out': ['fusionout'], 'run': 'detectFusionGenes.cwl'}]}
		

	"""Tests the creation of a workflow object for a non-id type workflow (workflow whose elements are
	  not identified with an id field)"""
	def test_instantiation_for_lobstr(self) :
		lobstr_workflow = c.createWorkflowObject('lobSTR.cwl', lobSTR)
		self.assertEqual(util.getInputNames(lobstr_workflow), expectedInputsForLobstr)
		self.assertEqual(util.getOutputNames(lobstr_workflow), expectedOutputsForLobstr)
		self.assertEqual(util.getStepNames(lobstr_workflow), expectedStepsForLobstr)

	"""Test the creation of a workflow object for an id type workflow (workflow whose elements are 
		identified with an id field)"""
	def test_instantiation_for_concordance(self) :
		concordance_workflow = c.createWorkflowObject('concordance.cwl', concordance)
		self.assertEqual(util.getInputNames(concordance_workflow), expectedInputsForConcordance)
		self.assertEqual(util.getOutputNames(concordance_workflow), expectedOutputsForConcordance)
		self.assertEqual(util.getStepNames(concordance_workflow), expectedStepsForConcordance)
	
	def test_instantiation_for_main(self) :
		main_workflow = c.createWorkflowObject('main.cwl', main)
		self.assertEqual(util.getInputNames(main_workflow), expectedInputsForMain)



if __name__ == '__main__':
    unittest.main()
