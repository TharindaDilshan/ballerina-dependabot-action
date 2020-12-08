import helpers

def getModulesToBeUpdated(tomlFile):
    lineIdentifier = False
    modulesToBeUpdated = []

    for line in tomlFile.splitlines():
        if lineIdentifier and '=' not in line:
            lineIdentifier = False
            break

        if lineIdentifier and '=' in line:
            module = line.replace(" ", "").split('=')       
            moduleName = module[0][1:-1]                #org/module
            currentVersion = module[1][1:-1]
            updateFlag, latestVersion = isCurrentVersionLatest(moduleName, currentVersion)
            if updateFlag:
                modulesToBeUpdated.append({moduleName + ':' + latestVersion})

        if '[dependencies]' in line:
            lineIdentifier = True

    return modulesToBeUpdated

def isCurrentVersionLatest(moduleName, currentVersion):
    updateFlag = False

    try:
        latestVersion = helpers.urlOpenWithRetry("https://api.central.ballerina.io/1.0/modules/info/" + moduleName)
        if helpers.compareVersion(latestVersion, currentVersion) == 1:
            updateFlag = True
    except
        latestVersion = currentVersion

    return updateFlag, latestVersion

