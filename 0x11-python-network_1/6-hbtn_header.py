#!/usr/bin/python3
""" ends a POST req to a given URL """
import sys
import requests


if __name__ == "__main__":
    address = sys.argv[1]
    val = {"email": sys.argv[2]}

    req = requests.post(address, val)

    print(req.text)
