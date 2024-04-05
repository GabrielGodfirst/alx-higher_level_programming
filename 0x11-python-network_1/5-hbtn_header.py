#!/usr/bin/python3

"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        value = response.headers.get("X-Request-Id")
        print(value)
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
