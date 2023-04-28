#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """

import urllib.request

if __name__ == '__main__':

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as reply:
        message = reply.read()
        print("Body response:")
        print("\t- type: {}".format(type(message)))
        print("\t- content: {}".format(message))
        print("\t- utf8 content: {}".format(message.decode('utf-8')))

