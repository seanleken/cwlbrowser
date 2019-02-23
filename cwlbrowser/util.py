import cwlbrowser.workflow as wf
TOP = "WORKFLOW"
UNKNOWN = "not known"
NAME = 1
TYPE = 2
RUN = 3

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
	temp =[]
	if(isinstance(inputs, dict)) :
		for key, value in inputs.items() :
			setUpInputs(value, temp, name=key)
	elif (isinstance(inputs, list)) :
		for input_ in inputs :
			setUpInputs(input_, temp, name=input_)
	else :
		temp = []
	return temp


def setUpInputs(value, temp, name="input") :
	#checks if input is in form of string(reference to declared input)
	if(isinstance(value, str)) :
		type_ = UNKNOWN
		inputName = name
	#input itself is a dict
	else :
		type_ = UNKNOWN if not ("type" in value) else value["type"]
		inputName= name if not ("id" in value) else value["id"]
	item = wf.Input(inputName, type_)
	temp.append(item)



def instantiateOutputs(outputs) :
	temp = []
	if(isinstance(outputs, dict)) :
		for key, value in outputs.items() :
			setUpOutputs(value, temp, key)
	elif(isinstance(outputs, list)) :
		for output in outputs :
			setUpOutputs(output, temp, output)
	else :
		temp = []
	return temp


def setUpOutputs(value, temp, name="output") :
	if (isinstance(value, dict)) :
		type_ = UNKNOWN if not ("type" in value) else value["type"]
		outputName = name if not ("id" in value) else value["id"]
		outputObj = wf.Output(outputName, type_)
    #string
	else :
		outputName = name
		outputObj = wf.Output(outputName, UNKNOWN)
	temp.append(outputObj)

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


def similarityCheckItems(workflow1, workflow2, attribute, weighting):
	denominator = 0
	numerator = 0
	biggerList = []
	smallerList = []
	matchingItems = []
	differingItemsForSmallerList  = []
	differingItemsForBiggerList = []
	if attribute == "steps" :
		list1 = workflow1.steps
		list2 = workflow2.steps
	elif attribute == "inputs" :
		list1 = workflow1.inputs
		list2 = workflow2.inputs
	elif attribute == "outputs" :
		list1 = workflow1.outputs
		list2 = workflow2.outputs
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




def getInputTypes(workflow) :
	return getObjectAttribute(workflow.inputs, TYPE)



def getOutputTypes(workflow) :
	return getObjectAttribute(workflow.outputs, TYPE)



def getStepRuns(workflow) :
	return getObjectAttribute(workflow.steps, RUN)





	

