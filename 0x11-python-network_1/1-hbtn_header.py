#!/usr/bin/python3

"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys


def display_x_request_id(url):
    """Fetches the value of the X-Request-Id variable from the header of
    the response"""
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    display_x_request_id(url)
