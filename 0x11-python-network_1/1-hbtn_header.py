#!/usr/bin/python3
""" takes in a URL, sends a request to the url"""


import sys
import urllib.request


if __name__ == "__main__":
    address = sys.argv[1]

    req = urllib.request.Request(address)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
