#!/usr/bin/env python3
import os
import helpers
import file_fetcher

# print(os.environ)
print("It works!")
# print(os.environ['GITHUB_REPOSITORY'])
print(helpers.HTTP_REQUEST_DELAY_IN_SECONDS)

repo = helpers.configureGithubRepository()
tomlFile = file_fetcher.fetchTOMLFile(repo)

exit(0)