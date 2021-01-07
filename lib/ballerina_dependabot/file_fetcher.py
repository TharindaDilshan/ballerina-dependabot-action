import sys

from github import GithubException

import commons

# Fetch toml file from a given repository
def fetchTomlFileFromMainBranch(repo):
    path = commons.getTomlFilePath()
    try:
        try:
            file = repo.get_contents(path, ref="main")
        except GithubException:
            file = repo.get_contents(path, ref="master")
        tomlFile = file.decoded_content.decode("utf-8")
    except Exception as e:
        print("Failed to fetch Ballerina.toml from the root directory - " + str(e))
        sys.exit()
    

    return tomlFile

# Fetch toml file from main branch or existing dependabot branch
def fetchTomlFileFromMainOrExistingBranch(repo, module):
    path = commons.getTomlFilePath()

    try:
        branch = repo.get_branch(branch="dependabot/" + module)
        file = repo.get_contents(path, ref="dependabot/" + module)
    except GithubException:
        try:
            file = repo.get_contents(path, ref="main")
        except GithubException:
            file = repo.get_contents(path, ref="master")

    tomlFile = file.decoded_content.decode("utf-8")

    return tomlFile
