#!/usr/bin/env python3
import yaml
import sys

inputworkflow = str(sys.argv[1])
attribute = str(sys.argv[2])
file = open('doc/{}.cwl'.format(inputworkflow))
wf = yaml.safe_load(file)
outputfilename = 'doc/{}_expected_{}.txt'.format(inputworkflow, attribute)
outputfile = open(outputfilename, 'w+')
temp = [] 
if (isinstance(wf[attribute], dict)) :  
	for element in wf[attribute] :
		outputfile.write('"{}", '.format(element))
elif isinstance(wf[attribute], list) :
	for element in wf[attribute] :
		if "id" in element :
			outputfile.write('"{}",'.format(element["id"]))
		else :
			outputfile.write('{}'.format(element))
print('written to {}'.format(outputfilename))
outputfile.close
file.close
