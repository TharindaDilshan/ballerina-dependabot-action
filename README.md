# ballerina-dependabot 

This GitHub action will provide a functionality similar to GitHub Dependabot for Ballerina projects. The action will check the Ballerina Central, for latest versions of the modules found in the Ballerina.toml file and raise Pull Requests for each module with version updates.

# Usage
See the [repo](https://github.com/TharindaDilshan/ballerina-dependabot-extended) for a real world example.

## Inputs

| Input        | Required | Description |
|--------------|----------|-------------|
| git_email    | Yes      |             |
| git_username | Yes      |             |
| token        | Yes      |             |
| file_path    | No       |             |

## Example

```
 - uses: TharindaDilshan/ballerina-dependabot-extended@main
   with:
      git_email: ${{ secrets.BALLERINA_BOT_EMAIL }}
      git_username: ${{ secrets.BALLERINA_BOT_USERNAME}}
      token: ${{ secrets.BALLERINA_BOT_TOKEN }}
```

## Full Example
