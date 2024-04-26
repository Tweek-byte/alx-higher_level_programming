#!/usr/bin/python3
""" Sends a POST request to http://0.0.0.0:5000/search_user """


import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        harf = " "
    else sys.argv[1]:
        pd = {"q": harf}

    req = requests.post("http://0.0.0.0:5000/search_user", pd)
    try:
        res = req.json()

        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
