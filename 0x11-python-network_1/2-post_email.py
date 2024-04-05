#!/usr/bin/python3

"""
Script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    """Sends a POST request to the URL with email as a parameter
    and displays the body of the response"""
    params = {"email": email}
    data = urllib.parse.urlencode(params).encode("ascii")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        response_text = response.read().decode("utf-8")
        print(response_text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
