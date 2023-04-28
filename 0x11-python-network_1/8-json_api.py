#!/usr/bin/python3
"""
Python script that sends a POST request to the URL and
to an URL with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    item = {'q': ""}

    try:
        item['q'] = sys.argv[1]
    except:
        pass

    reply = requests.post('http://0.0.0.0:5000/search_user', item)

    try:
        obj = reply.json()
        if not obj:
            print("No result")
        else:
            print("[{}] {}".format(obj.get('id'), obj.get('name')))
    except:
        print("Not a valid JSON")
