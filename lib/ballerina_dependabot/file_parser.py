import helpers
import toml
import sys

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
            modulesToBeUpdated.append({
                'name' : module,
                'version' : latestVersion})

    return modulesToBeUpdated

def isCurrentVersionLatest(module, currentVersion):
    updateFlag = False

    try:
        latestVersion = helpers.urlOpenWithRetry("https://api.central.ballerina.io/1.0/modules/info/" + module)
    except:
        latestVersion = currentVersion

    if helpers.compareVersion(latestVersion, currentVersion) == 1:
            updateFlag = True

    return updateFlag, latestVersion

