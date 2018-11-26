import yaml
import subprocess
import cwltool


def loadWorkflowFromGitHub(owner, repo, path):
	link = "https://api.github.com/repos/" + owner + "/" + repo + "/contents/" + path
