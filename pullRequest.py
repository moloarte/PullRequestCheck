from github import Github
import os
import sys
import getopt

argument_list = sys.argv[1::]
short_options = "a:h:b:r:d:t:"
long_options = ["action=", "head=", "base=",
                "repo=",  "body=", "title="]

try:
    arguments, values = getopt.getopt(
        argument_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print(str(err))
    sys.exit(2)

for current_argument, current_value in arguments:
    if current_argument in ("--action"):
        action = current_value
    elif current_argument in ("--head"):
        head = current_value
    elif current_argument in ("--base"):
        base = current_value
    elif current_argument in ("--repo"):
        repo = current_value
    elif current_argument in ("--body"):
        body = current_value
    elif current_argument in ("--title"):
        title = current_value
    else:
        print("'{} = {}' not a valid statement or argument".format(
            current_argument, current_value))
        sys.exit(2)


g = Github(os.environ["githubToken"])
g_repo = g.get_repo(repo)


def createPullRequest(title, body, head, base):
    pr = g_repo.create_pull(
        title=title, body=body, head=head, base=base)
    return(pr)


def checkOpenPullRequest(base, head):
    pulls = g_repo.get_pulls(state='open', head=head, base=base)
    pr_array = []
    for pr in pulls:
        pr_array.append(pr)
    return(pr_array)


try:
    if action == "list":
        print(checkOpenPullRequest(base, head))
    elif action == "create":
        open_pr = checkOpenPullRequest(base, head)
        if len(open_pr) == 0:
            print(createPullRequest(title, body, head, base))
        else:
            for pr in open_pr:
                print("There is already a pull request open for this branch see #{}".format(
                    pr.number))
    else:
        print("{} is not a valid action value".format(action))
        sys.exit(2)
except NameError as error:
    print(error)
