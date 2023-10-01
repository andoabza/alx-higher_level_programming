#!/bin/bash
# prins status code
curl -o /dev/null -s --head --write-out '%{http_code}\n' "$1"
