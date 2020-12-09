import sys

# Fetch toml file from a given repository
def fetchTomlFileFromMainBranch(repo):
    try:
        file = repo.get_contents("Ballerina.toml", ref="master")
        data = file.decoded_content.decode("utf-8")
    except Exception as e:
        print("Failes to fetch Ballerina.toml - " + str(e))
        sys.exit()
    

    return data

# Fetch toml file from main branch or existing dependabot branch
def fetchTomlFileFromMainOrExistingBranch(repo, module):
    try:
        branch = repo.get_branch(branch="dependabot-" + module)
        file = repo.get_contents("gradle.properties", ref="dependabot")
    except GithubException:
        file = repo.get_contents("gradle.properties", ref="master")

    data = file.decoded_content.decode("utf-8")

    return data