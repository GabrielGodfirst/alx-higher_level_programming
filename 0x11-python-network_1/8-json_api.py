#!/usr/bin/python3

"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q.
If no argument is given, set q="".
If the response body is properly JSON formatted and not empty, display the
id and name like this: [<id>] <name>, Otherwise: Display Not a valid JSON
if the JSON is invalid and Display No result if the JSON is empty
"""

import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {"q": q}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        json_outp = response.json()

        if not json_outp:
            print("No result")
        else:
            my_id = json_outp.get("id")
            my_name = json_outp.get("name")
            print("[{}] {}".format(my_id, my_name))
    except requests.RequestException as e:
        print(f"Error sending POST request: {e}")
    except ValueError:
        print("Not a valid JSON")
