#!/usr/bin/python3

"""
Script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {"email": email}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print(response.text)
    except requests.RequestException as e:
        print(f"Error sending POST request: {e}")
