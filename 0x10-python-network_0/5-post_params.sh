#!/bin/bash
# send key-value pair
curl -sX POST "email: test@gmail.com, subject: I will always be here for PLD" "$1"
