#!/bin/bash
# Get the byte size of the HTTP response.
curl -s "$1" | wc -c
