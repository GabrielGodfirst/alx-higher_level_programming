#!/usr/bin/python3

"""
Script that takes 2 arguments in order to list 10 commits (from the most
recent to oldest) of the repository "rails" by the user "rails".
Print all commits by: `<sha>: <author name>` (one by line)
The first argument will be the repository name
The second argument will be the owner name
"""

import sys
import requests


def list_commits(repo_name, username):
    try:
        access_token = "YOUR_ACCESS_TOKEN"
        commits_url = (
                f"https://api.github.com/repos/{username}/{repo_name}/commits")
        headers = {"Authorization": f"token {access_token}"}
        response = requests.get(commits_url, headers=headers)
        response.raise_for_status()
        json_obj = response.json()
        for i, obj in enumerate(json_obj):
            if i == 10:
                break
            if isinstance(obj, dict):
                name = obj.get('commit').get('author').get('name')
                print(f"{obj.get('sha')}: {name}")
    except requests.RequestException as e:
        print(f"Error sending GET request: {e}")
    except ValueError:
        print("Response is not valid JSON")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    username = sys.argv[2]
    list_commits(repo_name, username)
