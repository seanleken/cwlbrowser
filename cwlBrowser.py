import requests
import base64
import yaml
import os
import cwltool
import subprocess
import workflow as wf

out_workflow = {}
steps = []

#Loads workflow via github API
#In order to use this method you must provide it with the name of the owner (according to github),
#name of the repo, and the path (use copy path on the github page for the file)
def loadWorkflowFromGitHub(owner, repo, path):
	global out_workflow
	link = "https://api.github.com/repos/" + owner + "/" + repo + "/contents/" + path
	req = requests.get(link)
	if req.status_code != 200:
	    print(req.status_code)
	    if req.status_code == 404:
	    	print ("cwl file not found. Maybe due to incorrect url")
	else:
		req = req.json()  	    
		content = base64.b64decode(req['content'])
		content = content.decode("utf-8")
		try:
			out_workflow = yaml.safe_load(content)
			return createWorkflowObject(path, out_workflow)
		except (yaml.YAMLError):
			print ("Error in loading the cwl file")


#You can use this method if you have the .cwl file locally.
#Make sure that you provide the method with the correct path to the 
#.cwl file
def loadWorkflow(workflow):
	global out_workflow
	if os.path.exists(workflow):
		file = open(workflow, 'rb')
		try:
			out_workflow = yaml.safe_load(file)
			return createWorkflowObject(workflow, out_workflow)
		except (yaml.YAMLError):
			print ("Error in loading the cwl file")
	else:
		print("File not located")
		return -1;


#print the specified attribute you want 
#pass the attribute as a string to the method
#E.G. printWorfklow("inputs")
def printWorkflowAttr(attribute) :
	if attribute in out_workflow.keys() :
		print(attribute + ":")
		for item in out_workflow[attribute] :
			print (item)
		print ("\n")
	else :
		print("No such attribute as: " + attribute + " found in workflow")

#creates fully expanded workflow
def packWorkflow(workflow) :
	p = subprocess.run(["cwltool", "--pack", workflow], capture_output=True)
	if(p.returncode != 0) :
		print ("Something went wrong")
	else :
		try:
			out_workflow = yaml.safe_load(file)
			print (out_workflow)
		except (yaml.YAMLError, exc):
			print ("Error in loading the cwl file")

#creates workflow object from dict
def createWorkflowObject(name, workflow) :
	workflowObject = wf.Workflow(name, workflow["inputs"], workflow["outputs"]
										, workflow["steps"])
	return workflowObject

#prints steps of workflow in neat form
def printWorkflowSteps(workflow):
	printAttr(workflow.steps, "Steps")

#prints inputs of workflow in neat form
def printWorkflowInputs(workflow):
	printAttr(workflow.inputs, "Inputs")

#prints outputs of workflow in neat form
def printWorkflowOutputs(workflow):
	printAttr(workflow.outputs, "Outputs")

def printAttr(attribute, attributeName):
	print(attributeName + ":")
	print("-----------------")
	for item in attribute:
		if("id" in item):
			print(item["id"])
		else:
			print(item)
	print("\n")



def compareNoOfInputs(workflow1, workflow2):
    compare(workflow1.name, workflow2.name, workflow1.inputs, workflow2.inputs, "inputs")

def compareNoOfOutputs(workflow1, workflow2):
	compare(workflow1.name, workflow2.name, workflow1.outputs, workflow2.outputs, "outputs")

def compareNoOfSteps(workflow1, workflow2):
	compare(workflow1.name, workflow2.name, workflow1.steps, workflow2.steps, "steps")


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






	
