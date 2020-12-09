import file_fetcher

def updateFileAndRaisePR(repo, modulesToBeUpdated):
    for module in modulesToBeUpdated:
        tomlFile = file_fetcher.fetchTomlFileFromMainOrExistingBranch(repo, module)