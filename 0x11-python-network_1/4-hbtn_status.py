#!/usr/bin/python3

"""
Script that fetches https://alx-intranet.hbtn.io/status.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        print('Body response:')
        print('\t- type: {}'.format(type(content)))
        print('\t- content: {}'.format(content))
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
