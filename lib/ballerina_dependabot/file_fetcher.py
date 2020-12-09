import sys

# Fetch TOML file from a given repository
def fetchTOMLFileFromMainBranch(repo):
    try:
        file = repo.get_contents("Ballerina.toml", ref="master")
        data = file.decoded_content.decode("utf-8")
    except Exception as e:
        print("Failes to fetch Ballerina.toml - " + str(e))
        sys.exit()
    

    return data