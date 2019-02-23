import cwlbrowser.workflow as wf
import cwlbrowser.input_output as io


def printAttr(attribute, attributeName, subjectName):
	print(subjectName + " " + attributeName + ":")
	print("-----------------")
	for item in attribute:
		if(isinstance(item, dict)):
			print(item["id"])
		else:
			print(item)
	print("\n")


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

def createInputOutputArray(elements) :
	temp =[]
	if(isinstance(elements, dict)) :
		for key, value in elements.items() :
			obj = io.InputOutput(value, name=key) 
			temp.append(obj)
	elif (isinstance(elements, list)) :
		for e in elements :
			obj = io.InputOutput(e) 
			temp.append(obj)
	else :
		temp = []
	return temp








	

