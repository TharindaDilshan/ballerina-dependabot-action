import file_fetcher

def updateFileAndRaisePR(repo, modulesToBeUpdated):
    for module in modulesToBeUpdated:
        latestVersion = modulesToBeUpdated[module]
        tomlFile = file_fetcher.fetchTomlFileFromMainOrExistingBranch(repo, module)
        modifiedTomlFile, currentVersion, commitFlag = updatePropertiesFile(tomlFile, module, latestVersion)

def updatePropertiesFile(tomlFile, module, latestVersion):
    