# ballerina-dependabot-action ![Test](https://github.com/TharindaDilshan/ballerina-dependabot-action/workflows/Test/badge.svg)

This GitHub action will provide a functionality similar to GitHub [Dependabot](https://github.com/dependabot/) for Ballerina projects. The action will check the [Ballerina Central](https://central.ballerina.io/), for latest versions of the modules found in the Ballerina.toml file and raise Pull Requests for each module with version updates.

# Usage
See this [repo](https://github.com/TharindaDilshan/ballerina-dependabot-extended) for a real world example.

## Inputs

| Input        | Required | Description                 |
|--------------|----------|-----------------------------|
| git_email    | Yes      | GitHub email address        |
| git_username | Yes      | GitHub username             |
| token        | Yes      | GitHub Access Token         |
| file_path    | No       | Path to Ballerina.toml file |

**Note** - File path is required if the Ballerina.toml file does not resides on the repository root.

If Ballerina.toml resides in the `ballerina_project` directory, `file_path: ballerina_project/`. The trailing `/` is required if the file_path is specified explicitly.

## Example

```
- uses: TharindaDilshan/ballerina-dependabot-action@main
  with:
     git_email: ${{ secrets.GITHUB_EMAIL }}
     git_username: ${{ secrets.GITHUB_USERNAME}}
     token: ${{ secrets.GITHUB_TOKEN }}
```

## Full Example

The action is scheduled to run every Sunday at 12:00 a.m.(IST) to check for dependency updates.

```
name: Ballerina Dependabot
on: 
  schedule:
        - cron: '30 18 * * 7'
jobs:
  resolve_dependencies:
    runs-on: ubuntu-latest
    name: Dependabot
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Dependabot Action
        uses: TharindaDilshan/ballerina-dependabot-action@main
        with:
          git_email: ${{ secrets.GITHUB_EMAIL }}
          git_username: ${{ secrets.GITHUB_USERNAME}}
          token: ${{ secrets.GITHUB_TOKEN }}
          file_path: project_1/
```
