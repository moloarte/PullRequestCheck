# Requirements
    pip3 install PyGithub
# Usage
## Check Pull Request
This function will check the open pull request associated with a certain branch against a certain base.

```bash
pullRequest.py --action check --repo nginx/nginx --head somebranch --base master
```

| Argument | Description                   | Values      |
| -------- | ----------------------------- | ----------- |
| action   | Which function to invoke      | check       |
| repo     | Name of the Github repository | nginx/nginx |
| head     | Branch name to merge          | somebranch  |
| base     | Merge Receiving Branch        | master      |

## Create Pull Request
This function will create a new pull request from a certain branch against a certain base.

```bash
pullRequest.py --action create --repo nginx/nginx --title "MyTitle" --body "Some Tale" --head somebranch  --base master    
```

| Argument | Description                       | Values      |
| -------- | --------------------------------- | ----------- |
| action   | Which function to invoke          | create      |
| repo     | Name of the Github repository     | nginx/nginx |
| title    | Title to give to the pull request | "MyTitle"   |
| body     | Description of the pull request   | "Some Tale" |
| head     | Branch name to merge              | somebranch  |
| base     | Merge Receiving Branch            | master      |
