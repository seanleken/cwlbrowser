import unittest
import cwlbrowser.browser as c 
import cwlbrowser.workflow as wf
import cwlbrowser.similaritychecker as s
lobstrDict = {'cwlVersion': 'v1.0', 'class': 'Workflow', 
						'inputs': {'p0': {'type': 'File[]?', 'description': 'list of files containing the first end of paired end reads in fasta or fastq format'}, 'p2': {'type': 'File[]?', 'description': 'list of files containing the second end of paired end reads in fasta or fastq format'}, 'output_prefix': {'type': 'string', 'description': 'prefix for output files. will output prefix.aligned.bam and prefix.aligned.stats'}, 'reference': {'type': 'File', 'description': "lobSTR's bwa reference files"}, 'rg-sample': {'type': 'string', 'description': 'Use this in the read group SM tag'}, 'rg-lib': {'type': 'string', 'description': 'Use this in the read group LB tag'}, 'strinfo': {'type': 'File', 'description': 'File containing statistics for each STR.'}, 'noise_model': {'type': 'File', 'description': 'File to read noise model parameters from (.stepmodel)', 'secondaryFiles': ['^.stuttermodel']}}, 
						'outputs': {'bam': {'type': 'File', 'outputSource': 'samindex/bam_with_bai'}, 'bam_stats': {'type': 'File', 'outputSource': 'lobSTR/bam_stats'}, 'vcf': {'type': 'File', 'outputSource': 'allelotype/vcf'}, 'vcf_stats': {'type': 'File', 'outputSource': 'allelotype/vcf_stats'}}, 'hints': {'DockerRequirement': {'dockerPull': 'rabix/lobstr'}}, 
						'steps': {'lobSTR': {'run': 'lobSTR-tool.cwl', 'in': {'p1': 'p1', 'p2': 'p2', 'output_prefix': 'output_prefix', 'reference': 'reference', 'rg-sample': 'rg-sample', 'rg-lib': 'rg-lib'}, 'out': ['bam', 'bam_stats']}, 'samsort': {'run': 'samtools-sort.cwl', 'in': {'input': 'lobSTR/bam', 'output_name': {'default': 'aligned.sorted.bam'}}, 'out': ['output_file']}, 'samindex': {'run': 'samtools-index.cwl', 'in': {'input': 'samsort/output_file'}, 'out': ['bam_with_bai']}, 'allelotype': {'run': 'allelotype.cwl', 'in': {'bam': 'samindex/bam_with_bai', 'reference': 'reference', 'output_prefix': 'output_prefix', 'noise_model': 'noise_model', 'strinfo': 'strinfo'}, 'out': ['vcf', 'vcf_stats']}}}

lobstrDifferentInputDict = {'cwlVersion': 'v1.0', 'class': 'Workflow', 
						'inputs': {'p1': {'type': 'File[]?', 'description': 'list of files containing the first end of paired end reads in fasta or fastq format'}, 'p2': {'type': 'File[]?', 'description': 'list of files containing the second end of paired end reads in fasta or fastq format'}, 'output_prefix': {'type': 'string', 'description': 'prefix for output files. will output prefix.aligned.bam and prefix.aligned.stats'}, 'reference': {'type': 'File', 'description': "lobSTR's bwa reference files"}, 'rg-sample': {'type': 'string', 'description': 'Use this in the read group SM tag'}, 'rg-lib': {'type': 'string', 'description': 'Use this in the read group LB tag'}, 'strinfo': {'type': 'File', 'description': 'File containing statistics for each STR.'}, 'noise_model': {'type': 'File', 'description': 'File to read noise model parameters from (.stepmodel)', 'secondaryFiles': ['^.stuttermodel']}}, 
						'outputs': {'bam': {'type': 'File', 'outputSource': 'samindex/bam_with_bai'}, 'bam_stats': {'type': 'File', 'outputSource': 'lobSTR/bam_stats'}, 'vcf': {'type': 'File', 'outputSource': 'allelotype/vcf'}, 'vcf_stats': {'type': 'File', 'outputSource': 'allelotype/vcf_stats'}}, 'hints': {'DockerRequirement': {'dockerPull': 'rabix/lobstr'}}, 
						'steps': {'lobSTR': {'run': 'lobSTR-tool.cwl', 'in': {'p1': 'p1', 'p2': 'p2', 'output_prefix': 'output_prefix', 'reference': 'reference', 'rg-sample': 'rg-sample', 'rg-lib': 'rg-lib'}, 'out': ['bam', 'bam_stats']}, 'samsort': {'run': 'samtools-sort.cwl', 'in': {'input': 'lobSTR/bam', 'output_name': {'default': 'aligned.sorted.bam'}}, 'out': ['output_file']}, 'samindex': {'run': 'samtools-index.cwl', 'in': {'input': 'samsort/output_file'}, 'out': ['bam_with_bai']}, 'allelotype': {'run': 'allelotype.cwl', 'in': {'bam': 'samindex/bam_with_bai', 'reference': 'reference', 'output_prefix': 'output_prefix', 'noise_model': 'noise_model', 'strinfo': 'strinfo'}, 'out': ['vcf', 'vcf_stats']}}}

lobstrDifferentStepDict = {'cwlVersion': 'v1.0', 'class': 'Workflow', 
						'inputs': {'p1': {'type': 'File[]?', 'description': 'list of files containing the first end of paired end reads in fasta or fastq format'},'extra input' : 'extra-input', 'p2': {'type': 'File[]?', 'description': 'list of files containing the second end of paired end reads in fasta or fastq format'}, 'output_prefix': {'type': 'string', 'description': 'prefix for output files. will output prefix.aligned.bam and prefix.aligned.stats'}, 'reference': {'type': 'File', 'description': "lobSTR's bwa reference files"}, 'rg-sample': {'type': 'string', 'description': 'Use this in the read group SM tag'}, 'rg-lib': {'type': 'string', 'description': 'Use this in the read group LB tag'}, 'strinfo': {'type': 'File', 'description': 'File containing statistics for each STR.'}, 'noise_model': {'type': 'File', 'description': 'File to read noise model parameters from (.stepmodel)', 'secondaryFiles': ['^.stuttermodel']}}, 
						'outputs': {'bam': {'type': 'File', 'outputSource': 'samindex/bam_with_bai'}, 'bam_stats': {'type': 'File', 'outputSource': 'lobSTR/bam_stats'}, 'vcf': {'type': 'File', 'outputSource': 'allelotype/vcf'}, 'vcf_stats': {'type': 'File', 'outputSource': 'allelotype/vcf_stats'}}, 'hints': {'DockerRequirement': {'dockerPull': 'rabix/lobstr'}}, 
						'steps': {'lobSTR5': {'run': 'lobSTR-tool.cwl', 'in': {'p1': 'p1', 'p2': 'p2', 'output_prefix': 'output_prefix', 'reference': 'reference', 'rg-sample': 'rg-sample', 'rg-lib': 'rg-lib'}, 'out': ['bam', 'bam_stats']}, 'samsort': {'run': 'samtools-sort.cwl', 'in': {'input': 'lobSTR/bam', 'output_name': {'default': 'aligned.sorted.bam'}}, 'out': ['output_file']}, 'samindex': {'run': 'samtools-index.cwl', 'in': {'input': 'samsort/output_file'}, 'out': ['bam_with_bai']}, 'allelotype': {'run': 'allelotype.cwl', 'in': {'bam': 'samindex/bam_with_bai', 'reference': 'reference', 'output_prefix': 'output_prefix', 'noise_model': 'noise_model', 'strinfo': 'strinfo'}, 'out': ['vcf', 'vcf_stats']}}}
lobstrDifferentOutputDict = {'cwlVersion': 'v1.0', 'class': 'Workflow', 
						'inputs': {'p0': {'type': 'File[]?', 'description': 'list of files containing the first end of paired end reads in fasta or fastq format'}, 'p2': {'type': 'File[]?', 'description': 'list of files containing the second end of paired end reads in fasta or fastq format'}, 'output_prefix': {'type': 'string', 'description': 'prefix for output files. will output prefix.aligned.bam and prefix.aligned.stats'}, 'reference': {'type': 'File', 'description': "lobSTR's bwa reference files"}, 'rg-sample': {'type': 'string', 'description': 'Use this in the read group SM tag'}, 'rg-lib': {'type': 'string', 'description': 'Use this in the read group LB tag'}, 'strinfo': {'type': 'File', 'description': 'File containing statistics for each STR.'}, 'noise_model': {'type': 'File', 'description': 'File to read noise model parameters from (.stepmodel)', 'secondaryFiles': ['^.stuttermodel']}}, 
						'outputs': {'bam45': {'type': 'File', 'outputSource': 'samindex/bam_with_bai'}, 'bam_stats': {'type': 'File', 'outputSource': 'lobSTR/bam_stats'}, 'vcf': {'type': 'File', 'outputSource': 'allelotype/vcf'}, 'vcf_stats': {'type': 'File', 'outputSource': 'allelotype/vcf_stats'}}, 'hints': {'DockerRequirement': {'dockerPull': 'rabix/lobstr'}}, 
						'steps': {'lobSTR': {'run': 'lobSTR-tool.cwl', 'in': {'p1': 'p1', 'p2': 'p2', 'output_prefix': 'output_prefix', 'reference': 'reference', 'rg-sample': 'rg-sample', 'rg-lib': 'rg-lib'}, 'out': ['bam', 'bam_stats']}, 'samsort': {'run': 'samtools-sort.cwl', 'in': {'input': 'lobSTR/bam', 'output_name': {'default': 'aligned.sorted.bam'}}, 'out': ['output_file']}, 'samindex': {'run': 'samtools-index.cwl', 'in': {'input': 'samsort/output_file'}, 'out': ['bam_with_bai']}, 'allelotype': {'run': 'allelotype.cwl', 'in': {'bam': 'samindex/bam_with_bai', 'reference': 'reference', 'output_prefix': 'output_prefix', 'noise_model': 'noise_model', 'strinfo': 'strinfo'}, 'out': ['vcf', 'vcf_stats']}}}

orfPredictionDict = {'cwlVersion': 'v1.0', 'class': 'Workflow', 'label': 'Find reads with predicted coding sequences above 60 AA in length', 'requirements': [{'class': 'SchemaDefRequirement', 'types': [{'$import': '../tools/FragGeneScan-model.yaml'}]}], 
					'inputs': {'sequence': {'type': 'File', 'format': 'edam:format_1929'}, 'completeSeq': 'boolean', 'model': '../tools/FragGeneScan-model.yaml#model'}, 
					'outputs': {'predictedCDS': {'type': 'File', 'format': 'edam:format_1929', 'outputSource': 'remove_short_pCDS/filtered_sequences'}}, 
					'steps': {'ORF_prediction': {'doc': 'Find reads with predicted coding sequences (pCDS)\n', 'run': '../tools/FragGeneScan1_20.cwl', 'in': {'sequence': 'sequence', 'completeSeq': 'completeSeq', 'model': 'model'}, 'out': ['predictedCDS']}, 'remove_short_pCDS': {'run': '../tools/discard_short_seqs.cwl', 'in': {'sequences': 'ORF_prediction/predictedCDS', 'minimum_length': {'default': 60}}, 'out': ['filtered_sequences']}}, '$namespaces': {'edam': 'http://edamontology.org/', 's': 'http://schema.org/'}, '$schemas': ['http://edamontology.org/EDAM_1.16.owl', 'https://schema.org/docs/schema_org_rdfa.html'], 's:license': 'https://www.apache.org/licenses/LICENSE-2.0', 's:copyrightHolder': 'EMBL - European Bioinformatics Institute'}

class TestForIdenticalWorkflows(unittest.TestCase) :
	@classmethod
	def setUpClass(cls):
		global lobstr, lobstrCopy, lobstrDifferentInput, lobstrDifferentStep, lobstrDifferentOutput
		global orfPrediction
		global similarityChecker
		lobstr = wf.Workflow('lobstr.cwl',lobstrDict)
		lobstrCopy = wf.Workflow('lobstr.cwl',lobstrDict)
		lobstrDifferentInput = wf.Workflow('lobstr1.cwl', lobstrDifferentInputDict)
		lobstrDifferentStep = wf.Workflow('lobstr1.cwl', lobstrDifferentStepDict)
		lobstrDifferentOutput = wf.Workflow('lobstr1.cwl', lobstrDifferentOutputDict)
		orfPrediction = wf.Workflow('orfPrediction.cwl', orfPredictionDict)
		similarityChecker = s.SimilarityChecker()



	def test_overall_match_is_a_hundred(self) :
		#call similarity check
		similarityChecker.similarityCheck(lobstr, lobstrCopy)
		self.assertEqual(similarityChecker.getOverallMatch(), 100)

	def test_workflows_differing_by_one_input(self) :
		similarityChecker.similarityCheck(lobstr, lobstrDifferentInput)
		self.assertNotEqual(similarityChecker.getOverallMatch(), 100)
		self.assertEqual(similarityChecker.inputSimilarityChecker.getDifferingItems(), ["p0", "p1"])

	def test_workflows_differing_by_a_step(self) :
		similarityChecker.similarityCheck(lobstr, lobstrDifferentStep)
		self.assertNotEqual(similarityChecker.getOverallMatch(), 100)
		self.assertEqual(similarityChecker.stepSimilarityChecker.getDifferingItems(), ["lobSTR", "lobSTR5"])

	def test_workflows_differing_by_an_output(self) :
		similarityChecker.similarityCheck(lobstr, lobstrDifferentOutput)
		self.assertNotEqual(similarityChecker.getOverallMatch(), 100)
		self.assertEqual(similarityChecker.outputSimilarityChecker.getDifferingItems(), ["bam", "bam45"])

	def test_completely_differing_workflows(self) :
		similarityChecker.similarityCheck(lobstr, orfPrediction)
		self.assertEqual(similarityChecker.getOverallMatch(), 0)


