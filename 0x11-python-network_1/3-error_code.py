#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and disps the res """


import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    address = sys.argv[1]

    req = urllib.request.Request(address)
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode("ascii"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
