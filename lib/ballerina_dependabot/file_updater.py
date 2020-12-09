import file_fetcher
import commons
import toml
import sys
from github import Github, InputGitAuthor, GithubException

def updateFileAndRaisePR(repo, modulesToBeUpdated):
    for module in modulesToBeUpdated:
        latestVersion = modulesToBeUpdated[module]
        tomlFile = file_fetcher.fetchTomlFileFromMainOrExistingBranch(repo, module)
        modifiedTomlFile, currentVersion, commitFlag = updatePropertiesFile(tomlFile, module, latestVersion)
        if commitFlag:
            commitChanges(modifiedTomlFile, currentVersion, repo, module, latestVersion)
            createPullRequest(repo, currentVersion, module, latestVersion)

def updatePropertiesFile(tomlFile, module, latestVersion):
    modifiedTomlFile = ''
    commitFlag = False

    currentVersion = toml.loads(tomlFile)['dependencies'][module]
    # update only if the current version < latest version
    isCurrentVersionLatest = commons.compareVersion(latestVersion, currentVersion)

    for line in tomlFile.splitlines():
        if module in line and isCurrentVersionLatest == 1:
            update = line.split('=')[0] + '= "' + latestVersion '"\n'
            modifiedTomlFile += update
            commitFlag = True
        else:
            update = line + '\n'
            modifiedTomlFile += update
    
    return modifiedTomlFile, currentVersion, commitFlag

# Checkout branch and commit changes
def commitChanges(modifiedTomlFile, currentVersion, repo, module, latestVersion):
    try:
        author = InputGitAuthor(os.environ['INPUT_GIT_USERNAME'], os.environ['INPUT_GIT_EMAIL'])
    except Exception as e:
        print('Failed to initialize github author - ' + str(e))
        sys.exit()

    # If branch already exists checkout and commit else create new branch from master branch and commit
    try:
        source = repo.get_branch(branch="dependabot/" + module)
    except GithubException:
        source = repo.get_branch("master")
        repo.create_git_ref(ref=f"refs/heads/dependabot/" + module, sha=source.commit.sha)

    contents = repo.get_contents("Ballerina.toml", ref="dependabot/" + module)
    repo.update_file(contents.path, 
                    "[Automated] Bump " + module + " from " + currentVersion + " to " + latestVersion, 
                    modifiedTomlFile, 
                    contents.sha, 
                    branch="dependabot/" + module, 
                    author=author)

# Create a PR from the branch created
def createPullRequest(repo, currentVersion, module, latestVersion):
    pulls = repo.get_pulls(state='open', head='dependabot/' + module, base='master')
    PRExists = 0

    # Check if a PR already exists for the module
    for pull in pulls:
        if module in pull.title:
            PRExists = pull.number
            minVersion = pull.title.split()[3]
            break

    # If PR exists update the title else create a new PR
    if PRExists:
        existingPR = repo.get_pull(PRExists)
        existingPR.edit(title="Bump " + module + " from " + minVersion + " to " + latestVersion)
    else:
        repo.create_pull(title="Bump " + module + " from " + currentVersion + " to " + latestVersion, 
                        body='$subject', 
                        head="dependabot/" + module, 
                        base="master")