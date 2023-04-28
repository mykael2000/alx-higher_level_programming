#!/bin/bash
# takes an argument and sends a GET request to the URL
curl -s -H "X-School-User-Id: 98" "${1}"
