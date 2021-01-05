import os
import sys
import urllib.request

import semver
import toml
from github import Github, GithubException, InputGitAuthor
from retry import retry

HTTP_REQUEST_RETRIES = 3
HTTP_REQUEST_DELAY_IN_SECONDS = 2
HTTP_REQUEST_DELAY_MULTIPLIER = 2

# Return the content in the given url
# Retry decorator will retry the function 3 times, doubling the backoff delay if URLError is raised 
@retry(urllib.error.URLError, tries=HTTP_REQUEST_RETRIES, delay=HTTP_REQUEST_DELAY_IN_SECONDS, 
                                    backoff=HTTP_REQUEST_DELAY_MULTIPLIER)
def urlOpenWithRetry(url):
    return urllib.request.urlopen(url)

# Compare latest version with current version
# Return 1 if latest version > current version
# Return 0 if latest version = current version
# Return -1 if latest version < current version
def compareVersion(latestVersion, currentVersion):
    try:
        comparedOutput = semver.compare(latestVersion, currentVersion)
    except:
        comparedOutput = 0

    return comparedOutput

# Fetch the repository
def configureGithubRepository():
    g = Github(os.environ['INPUT_TOKEN'])
    try:
        repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    except Exception as e:
        print("Error fetching repository " + os.environ['GITHUB_REPOSITORY'] + " - " + str(e))
        sys.exit()

    return repo

# Get file path
def getTomlFilePath():
    if 'INPUT_FILE_PATH' in os.environ:
        if 'Ballerina.toml' in os.environ['INPUT_FILE_PATH'] or os.environ['INPUT_FILE_PATH'][-1] != '/':
            print("Invalid path format - " + os.environ['INPUT_FILE_PATH'])
            sys.exit()
        return os.environ['INPUT_FILE_PATH'] + 'Ballerina.toml'
    else:
        return 'Ballerina.toml'