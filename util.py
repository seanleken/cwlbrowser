import workflow as wf
TOP = "WORKFLOW"
UNKNOWN = "not known"

def printAttr(attribute, attributeName, subjectName):
	print(subjectName + " " + attributeName + ":")
	print("-----------------")
	for item in attribute:
		if(isinstance(item, dict)):
			print(item["id"])
		else:
			print(item)
	print("\n")

def instantiateInputs(inputs, workflowGraph=[]) :
	temp = []
	#input list is in the form of a dict ({})
	if(isinstance(inputs, dict)) :
		for key, value in inputs.items() :
			source = TOP
			#checks if input is in form of string(reference to declared input)
			if(isinstance(value, str)) :
				type_ = UNKNOWN
				source = findSource(value)
			#input itself is a dict
			else :
				type_ = UNKNOWN if not ("type" in value) else value["type"]
			item = wf.Input(key, type_, source)
			if(isinstance(workflowGraph, dict)) :
				workflowGraph[key] = []
			temp.append(item)
	#input list is in the form of a list ([])
	else :
		for input_ in inputs :
			source = TOP
			if(isinstance(input_, str)) :
				type_ = UNKNOWN
				source = findSource(input_)
				inputName = input_
			#input is a dict 
			else :
				type_ = UNKNOWN if not ("type" in input_) else input_["type"]
				inputName= input_ if not ("id" in input_) else input_["id"]
				if ("source" in input_) :
					if(isinstance(input_["source"], str)) :
						source = findSource(input_["source"])
					elif(isinstance(input_["source"], list)) :
						type_ = "list"
					else :
						print("Invalid input type")
			inputObj = wf.Input(inputName, type_, source)
			temp.append(inputObj)
	return  temp

def instantiateOutputs(outputs) :
	temp = []
	if(isinstance(outputs, dict)) :
		for key, value in outputs.items() :
			type_ = UNKNOWN if not ("type" in value) else value["type"]
			item = wf.Output(key, type_)
			temp.append(item)
	else :
		for output in outputs :
			if (isinstance(output, dict)) :
				type_ = UNKNOWN if not ("type" in output) else output["type"]
				outputName = output if not ("id" in output) else output["id"]
				outputObj = wf.Output(outputName, type_)
			else :
				outputObj = wf.Output(output, UNKNOWN)
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
		if not(input_.type == UNKNOWN):
			print("INPUT Name: {0} Type: {1} Source: {2}".format(input_.name, input_.type, input_.source))
		else :
			print("INPUT Name: {0} Source: {1}".format(input_.name, input_.source))
	print()



def printOutputArray(name, outputArray):
	print(name + " OUTPUTS:")
	for output in outputArray:
		if not(output.type == UNKNOWN) :
			print("OUTPUT Name: {0} Type: {1}".format(output.name, output.type))
		else :
			print("OUTPUT Name: {0}".format(output.name))
	print()

def similarityCheckItems(workflow1, workflow2, attribute, weighting):
	denominator = 0
	numerator = 0
	biggerList = []
	smallerList = []
	matchingItems = []
	differingItemsForSmallerList  = []
	differingItemsForBiggerList = []
	if attribute == "steps" :
		list1 = workflow1.stepArray
		list2 = workflow2.stepArray
	elif attribute == "inputs" :
		list1 = workflow1.inputArray
		list2 = workflow2.inputArray
	elif attribute == "outputs" :
		list1 = workflow1.outputArray
		list2 = workflow2.outputArray
	else :
		print("Invalid attribute")
		return

	if(len(list1) >= len(list2)) :
		for item in list1 :
			biggerList.append(item.name)
		biggerWorkflow = workflow1.name
		smallerWorkflow = workflow2.name
		for item in  list2 :
			smallerList.append(item.name)
	else :
		for item in list2 :
			biggerList.append(item.name)
		biggerWorkflow = workflow2.name
		smallerWorkflow = workflow1.name
		for item in list1 :
			smallerList.append(item.name)
	denominator = 0 if not (len(biggerList) > 0) else len(biggerList)
	matchingItems = set(smallerList).intersection(biggerList) 
	if(len(matchingItems) != len(biggerList)) :
		differingItemsForSmallerList = set(smallerList).difference(biggerList)
		differingItemsForBiggerList = set(biggerList).difference(smallerList)
	numerator =len(matchingItems)
	return ((numerator /  denominator) * weighting), differingItemsForSmallerList, differingItemsForBiggerList, smallerWorkflow, biggerWorkflow

def printItemSimilarityStats(diffSmall, diffBig, smallerWorkflow, biggerWorkflow, attribute) :
	if ((len(diffSmall)) > 0 or (len(diffBig)) > 0) :
		print ("THE FOLLOWING ARE THE {} THAT DIFFER".format(attribute))
		print ("----------------------------------------------------------")
		print(smallerWorkflow)
		print("-----------------------------------------------------------")
		for item in diffSmall :
			print (item)
		print()
		print(biggerWorkflow)
		print("-----------------------------------------------------------")
		for item in diffBig : 
			print(item)
		print("\n")

def findSource(value):
	if(value.find("/") != -1):
		source, rhs = value.split("/", 1)
		return source
	else:
		return TOP

	

