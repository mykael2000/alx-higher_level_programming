#!/bin/bash
# bash script that takes in a URL and displays allow options
curl -s -I -X | grep "Allow:" | cut -d " " -f 2-
