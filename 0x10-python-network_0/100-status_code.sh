#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -sow /dev/null "$1"  "%{http_code}" 
