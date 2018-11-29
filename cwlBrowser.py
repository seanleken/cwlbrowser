import requests
import base64
import yaml
import os
import cwltool
import subprocess
import workflow as wf
import util

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


def compareNoOfInputs(workflow1, workflow2):
    util.compare(workflow1.name, workflow2.name, workflow1.inputs, workflow2.inputs, "inputs")

def compareNoOfOutputs(workflow1, workflow2):
	util.compare(workflow1.name, workflow2.name, workflow1.outputs, workflow2.outputs, "outputs")

def compareNoOfSteps(workflow1, workflow2):
	util.compare(workflow1.name, workflow2.name, workflow1.steps, workflow2.steps, "steps")








	
