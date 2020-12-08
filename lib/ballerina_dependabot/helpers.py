from retry import retry
import urllib.request
from github import Github, InputGitAuthor, GithubException
import os

HTTP_REQUEST_RETRIES = 3
HTTP_REQUEST_DELAY_IN_SECONDS = 2
HTTP_REQUEST_DELAY_MULTIPLIER = 2

# Return the content in the given url
# Retry decorator will retry the function 3 times, doubling the backoff delay if URLError is raised 
@retry(urllib.error.URLError, tries=HTTP_REQUEST_RETRIES, delay=HTTP_REQUEST_DELAY_IN_SECONDS, 
                                    backoff=HTTP_REQUEST_DELAY_MULTIPLIER)
def urlOpenWithRetry(url):
    return urllib.request.urlopen(url)

# Fetch the repository
def configureGithubRepository():
    g = Github(os.environ['INPUT_TOKEN'])
    try:
        repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
    except Exception as e:
        print("Error fetching repository " + os.environ['GITHUB_REPOSITORY'] + " - " + str(e))

    return repo