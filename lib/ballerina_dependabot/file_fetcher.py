import sys

from github import GithubException


# Fetch toml file from a given repository
def fetchTomlFileFromMainBranch(repo):
    try:
        file = repo.get_contents("Ballerina.toml", ref="main")
        tomlFile = file.decoded_content.decode("utf-8")
    except Exception as e:
        print("Failed to fetch Ballerina.toml - " + str(e))
        sys.exit()
    

    return tomlFile

# Fetch toml file from main branch or existing dependabot branch
def fetchTomlFileFromMainOrExistingBranch(repo, module):
    try:
        branch = repo.get_branch(branch="dependabot/" + module)
        file = repo.get_contents("Ballerina.toml", ref="dependabot")
    except GithubException:
        file = repo.get_contents("Ballerina.toml", ref="main")

    tomlFile = file.decoded_content.decode("utf-8")

    return tomlFile
