#!/usr/bin/python3
""" send request and show value of the x-request-id found in the header """

from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as reply:
            message = reply.read()
            print(message.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
