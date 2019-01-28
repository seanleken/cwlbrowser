import requests
import base64
import yaml
import os
import cwltool
import subprocess
import workflow as wf
import util
from IPython.display import SVG, display
import time
import os

out_workflow = {}
steps = []

def retrieveFileThruLink(link, path):
	req = requests.get(link)
	if req.status_code != 200:
	    print(req.status_code)
	    if req.status_code == 404:
	    	print ("cwl file not found. Maybe due to incorrect url")
	    	print("\n")
	else:
		req = req.json()  	    
		content = base64.b64decode(req['content'])
		content = content.decode("utf-8")
		try:
			out_workflow = yaml.safe_load(content)
			#print (out_workflow)
			return createWorkflowObject(path, out_workflow)
		except (yaml.YAMLError) as yamlError:
			print ("Error in loading the cwl file")
			print (yamlError)

#Loads workflow via github API
#In order to use this method you must provide it with the name of the owner (according to github),
#name of the repo, and the path (use copy path on the github page for the file)
def loadGitHub(owner, repo, path):
	global out_workflow
	link = "https://api.github.com/repos/" + owner + "/" + repo + "/contents/" + path
	return retrieveFileThruLink(link, path)
	


#You can use this method if you have the .cwl file locally.
#Make sure that you provide the method with the correct path to the 
#.cwl file
def load(workflow):
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

#loads workflow when given full url
def loadWithLink(link, branch='master') :
	lhs, rhs = link.split("/blob/", 1)
	path = rhs.replace(branch, "")
	ownerrepo = lhs.replace('https://github.com', "")
	finallink = "https://api.github.com/repos" + ownerrepo + "/contents" + path
	return retrieveFileThruLink(finallink, path)






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
	workflowInputs = []
	workflowObject.inputArray = util.instantiateInputs(workflow["inputs"])
	workflowObject.outputArray = util.instantiateOutputs(workflow["outputs"])
	workflowObject.stepArray = instantiateSteps(workflow["steps"])
	return workflowObject


def displayGraphSVG(link):
	BASE_URL = 'https://view.commonwl.org'

	HEADERS = {
	    'user-agent': 'my-app/0.0.1',
		'accept': 'application/json'
	}

	addResponse = requests.post(BASE_URL + '/workflows', 
							data={'url': link},		
							headers=HEADERS)
	if (addResponse.status_code == 200) :
		postExistingWorkflowGraph(link)
	elif (addResponse.status_code == requests.codes.accepted):
		qLocation = addResponse.headers['location']

		# Get the queue item until success
		qResponse = requests.get(BASE_URL + qLocation,
								headers=HEADERS,
								allow_redirects=False)
		maxAttempts = 5
		while qResponse.status_code == requests.codes.ok and qResponse.json()['cwltoolStatus'] == 'RUNNING' and maxAttempts > 0:
			time.sleep(5)
			qResponse = requests.get(BASE_URL + qLocation,
									headers=HEADERS,
									allow_redirects=False)
			maxAttempts -= 1
		if 'location' in qResponse.headers:
		# Success, get the workflow
			workflowResponse = requests.get(BASE_URL + qResponse.headers['location'], headers=HEADERS)
			if (workflowResponse.status_code == requests.codes.ok):
				workflowJson = workflowResponse.json()
				# Do what you want with the workflow JSON
				# Include details in documentation files etc
				display(SVG(BASE_URL + workflowJson['visualisationSvg']))
			else:
				print('Could not get returned workflow')
		elif (qResponse.json()['cwltoolStatus'] == 'ERROR'):
			# Cwltool failed to run here
			print(qResponse.json()['message'])
		elif (maxAttempts == 0):
			print('Timeout: Cwltool did not finish')
		else :
			print('Something is not right')

	else:
		print (addResponse.status_code)
		print('Error adding workflow')

	"""
	"""
def postExistingWorkflowGraph(link) :
	BASE_URL = 'https://view.commonwl.org'

	HEADERS = {
		'accept': 'application/json'
	}
	shortenedLink = link.replace("https://", "")
	finishedlink = BASE_URL + "/workflows/" + shortenedLink
	req = requests.get(finishedlink, headers=HEADERS)
	if req.status_code != 200:
		print(req.status_code)
	else:
		req = req.json()     
		display(SVG(BASE_URL + req['visualisationSvg']))


def compareNoOfInputs(workflow1, workflow2):
    util.compare(workflow1.name, workflow2.name, workflow1.inputs, workflow2.inputs, "inputs")

def compareNoOfOutputs(workflow1, workflow2):
	util.compare(workflow1.name, workflow2.name, workflow1.outputs, workflow2.outputs, "outputs")

def compareNoOfSteps(workflow1, workflow2):
	util.compare(workflow1.name, workflow2.name, workflow1.steps, workflow2.steps, "steps")


def instantiateSteps(steps) :
	temp = []
	#print (steps)
	if (isinstance(steps, dict)) :
		for key, value in steps.items() :
			item = wf.Step(key, value["in"], value["run"], value["out"])
			temp.append(item)
	else :
		for step in steps :
			stepObj = wf.Step(step["id"], step["in"], step["run"], step["out"])
			temp.append(stepObj)
	return temp

def similarityCheckSteps(workflow1, workflow2):
	denominator = 0
	stepsThatDoNotMatchSmaller = []
	stepsThatDoNotMatchBigger = []
	stepsThatMatch = []
	biggerworkflowSteps = []
	smallerworkflowSteps = []
	if len(workflow1.stepArray) >= len(workflow2.stepArray) :
		biggerworkflow = workflow1
		smallerworkflow = workflow2
	else :
		biggerworkflow = workflow2
		smallerworkflow = workflow1
	denominator =  0 if not (len(biggerworkflow.stepArray) > 0) else len(biggerworkflow.stepArray)
	numerator = 0;
	for step in biggerworkflow.stepArray :
		biggerworkflowSteps.append(step.name)
	for step in smallerworkflow.stepArray :
		smallerworkflowSteps.append(step.name)
	stepsThatMatch = set(smallerworkflowSteps).intersection(biggerworkflowSteps)
	if (len(stepsThatMatch) != len(biggerworkflowSteps)) :
		stepsThatDoNotMatchSmaller = set(smallerworkflowSteps).difference(biggerworkflowSteps)
		stepsThatDoNotMatchBigger = set(biggerworkflowSteps).difference(smallerworkflowSteps)
	numerator = len(stepsThatMatch)
	print("SIMILARITY CHECK BETWEEN {} AND {}:".format(workflow1.name, workflow2.name))
	similarityPercentage = (numerator / denominator) * 100
	print ("Overall match: {}".format(similarityPercentage))
	if (len(stepsThatDoNotMatchSmaller) > 0) :
		print ("THE FOLLOWING ARE THE STEPS THAT DIFFER")
		print ("----------------------------------------------------------")
		print(smallerworkflow.name)
		for step in stepsThatDoNotMatchSmaller :
			print (step)
		print()
		print(biggerworkflow.name)
		for step in stepsThatDoNotMatchBigger : 
			print(step)
	print("\n")












	
