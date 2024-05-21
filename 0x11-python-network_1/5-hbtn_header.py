#!/usr/bin/python3
""" Displays the X-Request-Id Header """


import sys
import requests


if __name__ == "__main__":
    address = sys.argv[1]

    req = requests.get(address)

    print(req.headers.get("X-Request-Id"))
