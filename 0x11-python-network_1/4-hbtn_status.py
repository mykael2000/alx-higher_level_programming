#!/usr/bin/python3
"""fetch of https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    reply = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(reply.text)))
    print("\t- content: {}".format(reply.text))
