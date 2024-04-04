#!/bin/bash
# Script that sends request and displays size of the body of the response.

curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
