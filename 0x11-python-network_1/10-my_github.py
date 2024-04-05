#!/usr/bin/python3

"""
Script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id.
The first argument will be your username.
The second argument will be your password (in your case, a personal
access token as password).
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        json_obj = response.json()
        print(json_obj.get("id"))
    except requests.RequestException as e:
        print(f"Error sending GET request: {e}")
    except ValueError:
        print("Response is not valid JSON")
