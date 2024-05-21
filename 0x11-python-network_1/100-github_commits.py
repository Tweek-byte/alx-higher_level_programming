#!/usr/bin/python3
""" Lists the 10 most recent on a given repo """


import sys
import requests


if __name__ == "__main__":
    address = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(address)
    commit = req.json()

    try:
        for j in range(10):
            print("{}: {}".format(
                commit[j].get("sha"),
                commit[j].get("commit").get("author").get("name")))
    except IndexError:
        pass
