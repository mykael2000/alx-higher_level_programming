#!/usr/bin/python3
""" sends a request toa url """
import requests
import sys

if __name__ == "__main__":
    link = sys.argv[1]

    reply = requests.get(link)
    if reply.status_code >= 400:
        print("Error code: {}".format(reply.status_code))
    else:
        print(reply.text)
