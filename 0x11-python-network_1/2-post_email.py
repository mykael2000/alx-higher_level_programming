#!/usr/bin/python3
""" SEnds a post request to a url """

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    link = sys.argv[1]
    result = {"email": sys.argv[2]}
    info = urllib.parse.urlencode(result).encode("ascii")

    met = urllib.request.Request(link, info)
    with urllib.request.urlopen(met) as reply:
        print(reply.read().decode("utf-8"))
