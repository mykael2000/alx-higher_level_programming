#!/bin/bash
# Script that sends a JSON POST request to a URL passed as the first argument
curl -sXH "$1" -d "@$2" POST  "Content-Type: application/json"
