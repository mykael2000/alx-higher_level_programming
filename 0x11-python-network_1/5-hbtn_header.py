#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""

import requests
import sys

if __name__ == "__main__":
    link = sys.argv[1]

    reply = requests.get(link)
    print(reply.headers.get("X-Request-Id"))
