import sys

import toml

import commons
import update_checker


def getModulesToBeUpdated(tomlFile):
    try:
        parsedToml = toml.loads(tomlFile)
    except Exception as e:
        print('Failed to parse toml file - ' + str(e))
        sys.exit()

    modulesToBeUpdated = []

    for module in parsedToml['dependencies']:
        currentVersion = parsedToml['dependencies'][module]
        updateFlag, latestVersion = isCurrentVersionLatest(module, currentVersion)
        if updateFlag:
            modulesToBeUpdated.append({module: latestVersion})

    return modulesToBeUpdated

def isCurrentVersionLatest(module, currentVersion):
    updateFlag = False

    try:
        latestVersion = update_checker.fetchLatestVersion(module)
    except:
        latestVersion = currentVersion

    if commons.compareVersion(latestVersion, currentVersion) == 1:
            updateFlag = True

    return updateFlag, latestVersion

