#!/usr/bin/python3

"""
Script that takes in a URL, sends a request to the URL, and displays the
body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions and
print: Error code: followed by the HTTP status code.
"""

import urllib.request
import urllib.error
import sys


def fetch_url_body(url):
    """Fetches the body of the response from the provided URL"""
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode("utf-8")
            print(response_text)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    fetch_url_body(url)
