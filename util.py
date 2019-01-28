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
	if(isinstance(inputs, dict)) :
		for key, value in inputs.items() :
			type_ = "not known" if not ("type" in value) else value["type"]
			item = wf.Input(key, type_)
			temp.append(item)
	else :
		for input_ in inputs :
			type_ = "not known" if not ("type" in input_) else input_["type"]
			inputName= input_ if not ("id" in input_) else input_["id"]
			inputObj = wf.Input(inputName, type_)
			temp.append(inputObj)
	return  temp

def instantiateOutputs(outputs) :
	temp = []
	if(isinstance(outputs, dict)) :
		for key, value in outputs.items() :
			type_ = "not known" if not ("type" in value) else value["type"]
			item = wf.Output(key, type_)
			temp.append(item)
	else :
		for output in outputs :
			if (isinstance(output, dict)) :
				type_ = "not known" if not ("type" in output) else output["type"]
				outputName = output if not ("id" in output) else output["id"]
				outputObj = wf.Output(outputName, type_)
			else :
				outputObj = wf.Output(output, "not known")
			temp.append(outputObj)
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


def printInputArray(name, inputArray):
	print(name + " INPUTS:")
	for input_ in inputArray:
		if not(input_.type == "not known"):
			print("Name: {0} Type: {1}".format(input_.name, input_.type))
		else :
			print("Name: {0}".format(input_.name))

def printOutputArray(name, outputArray):
	print(name + " OUTPUTS:")
	for output in outputArray:
		if not(output.type == "not known") :
			print("Name: {0} Type: {1}".format(output.name, output.type))
		else :
			print("Name: {0}".format(output.name))