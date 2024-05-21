#!/usr/bin/python3
""" Sends a request to a given URL and disps theres. """


import sys
import requests


if __name__ == "__main__":
    address = sys.argv[1]

    req = requests.get(address)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
