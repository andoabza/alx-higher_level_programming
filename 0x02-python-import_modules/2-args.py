#!/usr/bin/python3
import sys
lent = len(sys.argv)-1
char = sys.argv[1: lent]
if lent == 0:
    print("{:d} arguments.".format(lent))
elif lent == 1:
    print("{:d} argument :".format(lent))
else:
    print("{:d} arguments :".format(lent))
i = 0
for i in range(lent + 1):
    print("{}: {}".format(i + 1, str(sys.argv[i])))
    i = i + 1
print(char)