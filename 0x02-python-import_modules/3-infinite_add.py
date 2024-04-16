#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys

    indx = 1
    sum = 0
    while indx < len(sys.argv):
        sum += int(sys.argv[indx])
        indx += 1
    print("{}".format(sum))
