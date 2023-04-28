#!/usr/bin/python3
""" sends request to the URL and shows the X-Request-Id variable found in the header ofthe response."""

import urllib.request
import sys
if __name__ == "__main__":
    link = sys.argv[1]

    message = urllib.request.Request(link)
    with urllib.message.urlopen(request) as reply:
        print(dict(reply.headers).get("X-Request-Id"))
