#!/bin/bash
# send json file
echo"$(curl -s -X POST -d "$2" -H "Content-Type: application/json" "$1")"
