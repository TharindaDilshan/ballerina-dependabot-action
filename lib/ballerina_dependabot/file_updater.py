import file_fetcher
import helpers

def updateFileAndRaisePR(repo, modulesToBeUpdated):
    for module in modulesToBeUpdated:
        latestVersion = modulesToBeUpdated[module]
        tomlFile = file_fetcher.fetchTomlFileFromMainOrExistingBranch(repo, module)
        modifiedTomlFile, currentVersion, commitFlag = updatePropertiesFile(tomlFile, module, latestVersion)

def updatePropertiesFile(tomlFile, module, latestVersion):
    modifiedTomlFile = ''
    commitFlag = False

    for line in tomlFile.splitlines():
        if module in line:
            currentVersion = line.split('=')[-1].replace(" ","")[1:-1]
            # update only if the current version < latest version
            if helpers.compareVersion(latestVersion, currentVersion) == 1:
                update = line.split('=')[0] + '= "' + latestVersion '"\n'
                modifiedTomlFile += update
                commitFlag = True
        else:
            update = line + '\n'
            modifiedTomlFile += update
    
    return modifiedTomlFile, currentVersion, commitFlag