from retry import retry
import urllib.request

HTTP_REQUEST_RETRIES = 3
HTTP_REQUEST_DELAY_IN_SECONDS = 2
HTTP_REQUEST_DELAY_MULTIPLIER = 2

# Return the content in the given url
# Retry decorator will retry the function 3 times, doubling the backoff delay if URLError is raised 
@retry(urllib.error.URLError, tries=HTTP_REQUEST_RETRIES, delay=HTTP_REQUEST_DELAY_IN_SECONDS, 
                                    backoff=HTTP_REQUEST_DELAY_MULTIPLIER)
def urlOpenWithRetry(url):
    return urllib.request.urlopen(url)