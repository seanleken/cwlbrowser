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
for element in wf[attribute] :
	outputfile.write('{}\n'.format(element))
print('written to {}'.format(outputfilename))
outputfile.close
file.close
