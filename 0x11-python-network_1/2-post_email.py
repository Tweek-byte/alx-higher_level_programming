#!/usr/bin/python3
""" takes in a URL and an email, sends a POST req to URL"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    address = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    req = urllib.request.Request(address, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
