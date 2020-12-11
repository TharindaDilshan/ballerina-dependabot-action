import sys

import toml

import commons
import update_checker

# Parse the Ballerina.toml file and get a list of modules with version updates available
def getModulesToBeUpdated(tomlFile):
    try:
        parsedToml = toml.loads(tomlFile)
    except Exception as e:
        print('Failed to parse toml file - ' + str(e))
        sys.exit()

    try:
        if len(parsedToml['dependencies']) == 0:
            print('No dependencies found in Ballerina.toml')
            sys.exit()
    except:
        print('No dependencies found in Ballerina.toml')
        sys.exit()

    modulesToBeUpdated = []

    for module in parsedToml['dependencies']:
        currentVersion = parsedToml['dependencies'][module]
        updateFlag, latestVersion = isCurrentVersionLatest(module, currentVersion)
        if updateFlag:
            modulesToBeUpdated.append({module: latestVersion})

    return modulesToBeUpdated

# Compare current version with the latest version fetched from Ballerina Central
# Update flag is set to true if current version < latest version
def isCurrentVersionLatest(module, currentVersion):
    updateFlag = False

    try:
        latestVersion = update_checker.fetchLatestVersion(module)
    except:
        latestVersion = currentVersion

    if commons.compareVersion(latestVersion, currentVersion) == 1:
            updateFlag = True

    return updateFlag, latestVersion

