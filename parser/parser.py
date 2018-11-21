import yaml

stream = open('compile.cwl', 'r')

workflow = yaml.safe_load(stream)

for input in workflow["$graph"] :
	print (input)
	print ("\n")