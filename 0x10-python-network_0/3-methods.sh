#!/bin/bash
# display a;ll http methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
