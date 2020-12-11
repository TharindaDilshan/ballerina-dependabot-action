#!/usr/bin/env python3
import os

import commons
import file_fetcher
import file_parser
import file_updater

repo = commons.configureGithubRepository()
tomlFile = file_fetcher.fetchTomlFileFromMainBranch(repo)
modulesToBeUpdated = file_parser.getModulesToBeUpdated(tomlFile)

if len(modulesToBeUpdated) > 0:
    file_updater.updateFileAndRaisePR(repo, modulesToBeUpdated)  
    print("Module versions updated successfully")
else:
    print("Module versions are up to date")

exit(0)
