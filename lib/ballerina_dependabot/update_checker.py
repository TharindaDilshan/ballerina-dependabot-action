import json

import commons


# Get the latest version of a Ballerina Stdlib module from the Ballerina Central
def fetchLatestVersion(module):
    try:
        data = commons.urlOpenWithRetry("https://api.central.ballerina.io/1.0/modules/info/" + module)
        dataToString = data.read().decode("utf-8")
        latestVersion = json.loads(dataToString)['module']['version']
    except Exception as e:
        print("Failed to fetch the version of " + module + ": " + str(e))
        latestVersion = e

    return latestVersion

# fetchLatestVersion('wso2', 'gmail')
# isinstance(latestVersion, Exception)
