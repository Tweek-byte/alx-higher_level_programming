#!/usr/bin/python3
"""Fetches the given link"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as res:
        message = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(message)))
        print("\t- content: {}".format(message))
        print("\t- utf8 content: {}".format(message.decode("utf-8")))
