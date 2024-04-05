#!/usr/bin/python3
indx = 90
cur = 0
while (indx > 64):
    if (indx % 2):
        cur = indx
    else:
        cur = indx + 32
    print("{}".format(chr(cur)), end='')
    indx -= 1
