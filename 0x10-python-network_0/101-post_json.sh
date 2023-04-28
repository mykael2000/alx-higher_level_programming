#!/bin/bash
# Script that sends a JSON POST request to a URL passed as the first argument
curl -sXH -d "$(cat"$2")" "$1" POST  "Content-Type: application/json"
