#!/usr/bin/env python3
import yaml
import sys

inputworkflow = str(sys.argv[1])
attribute = str(sys.argv[2])
file = open('doc/{}.cwl'.format(inputworkflow))
wf = yaml.safe_load(file)
outputfilename = 'doc/{}_expected_{}.txt'.format(inputworkflow, attribute)
outputfile = open(outputfilename, 'w+')
steps = wf[attribute]
for key, value in steps.items() :
	if isinstance(value["out"], dict) :
		for k, v in value["out"].items() :
			if "type" in v :
				outputfile.write('"{}", '.format(v["type"]))
			else :
				outputfile.write('"not known", ')
	elif isinstance(value["out"], list) :
		for output in value["out"] :
			if isinstance(output, str) :
				outputfile.write('"not known", ')
			elif isinstance(output, dict) :
				if "type" in output :
					outputfile.write('"{}"'.format(output["type"]))
				else :
					outputfile.write('"not known", ')
			else:
				print("cba")
	outputfile.write("\n")
print('written to {}'.format(outputfilename))
outputfile.close
file.close
