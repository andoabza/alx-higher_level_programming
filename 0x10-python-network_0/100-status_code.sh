#!/bin/bash
# prins status code
curl -o /dev/null -sIw '%{http_code}\n' "$1"
