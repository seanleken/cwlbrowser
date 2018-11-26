import yaml
import subprocess
import cwltool

stream = open('hello.cwl', 'r')
p = subprocess.run(["cwltool", "--pack", "hello.cwl"], capture_output=True)

if(p.returncode != 0) :
  print ("Something went wrong")
else :
  workflow = yaml.safe_load(p.stdout.decode("utf8"))
  print (workflow)

# wf = {}



"""for step in workflow["steps"] :
	s = {}
	if("id" in step) :
	  print (step["id"])
	 s["name"] = step["id"]  or "step"
	print ("Inputs:")
	for input_ in step["in"] :
	  if("id" in input_) :
	    print (input_["id"])
	  if("name" in input_) :
	  	print (input_["name"])
	print ("\n")"""