#!/usr/bin/python3
""" 10 recent commits in a particular GitHub repository"""

import requests
import sys

if __name__ == "__main__":
    link = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    reply = requests.get(link)
    gitcom = reply.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                gitcom[i].get("sha"),
                gitcom[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
