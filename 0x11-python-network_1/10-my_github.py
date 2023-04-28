#!/usr/bin/python3
""" displays id using github api  """

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    gitauth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    reply = requests.get("https://api.github.com/user", auth=gitauth)
    print(reply.json().get("id"))
