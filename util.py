import workflow as wf

def printAttr(attribute, attributeName, subjectName):
	print(subjectName + " " + attributeName + ":")
	print("-----------------")
	for item in attribute:
		if(isinstance(item, dict)):
			print(item["id"])
		else:
			print(item)
	print("\n")

def instantiateInputs(inputs) :
	temp = []
	for key, value in inputs.items() :
		item = wf.Input(key, value["type"])
		temp.append(item)
	return  temp

def instantiateOutputs(outputs) :
	temp = []
	for key, value in outputs.items() :
		item = wf.Output(key, value["type"])
		temp.append(item)
	return  temp


def compare(name1, name2,attributeX, attributeY, attributeName):
	count1 = 0
	count2 = 0
	difference = 0
	for input_ in attributeX:
		count1 = count1 + 1
	for input_2 in attributeY:
		count2 = count2 + 1
	if(count1 >= count2):
		difference = count1 - count2
	else:
		difference = count2 - count1
	print("-------------------------------------")
	print("--------- " + attributeName + " comparison------------")
	print("-------------------------------------")
	print(name1 + "| no. of " + attributeName+ ": " + str(count1))
	print(name2 + "| no. of " + attributeName+ ": " + str(count2))
	print("Difference: " + str(difference))
	print("-------------------------------------")
	print("\n")