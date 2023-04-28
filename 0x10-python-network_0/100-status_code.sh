#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -so /dev/null -w "$1"  "%{http_code}" 
