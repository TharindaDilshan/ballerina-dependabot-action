import os
import sys
import semver
import urllib.request
from retry import retry
from github import Github, InputGitAuthor, GithubException
import toml

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
    return semver.compare(latestVersion, currentVersion)

# Fetch the repository
def configureGithubRepository():
    g = Github(os.environ['INPUT_TOKEN'])
    try:
        repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    except Exception as e:
        print("Error fetching repository " + os.environ['GITHUB_REPOSITORY'] + " - " + str(e))
        sys.exit()

    return repo
