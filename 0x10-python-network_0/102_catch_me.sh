#!/bin/bash
# Script that makes a request and receives "you got me"
curl -s -L 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin: HolbertonSchool"
