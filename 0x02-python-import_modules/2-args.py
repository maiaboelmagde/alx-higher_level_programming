#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys
    if (len(sys.argv) == 1):
        print("0 arguments.")
    elif (len(sys.argv) == 2):
        print("1 argument:\n1: {}".format(sys.argv[1]))
    else:
        list_len = len(sys.argv)
        print("{} arguments:".format(list_len))
        indx = 1
        while indx < list_len:
            print("{}: {}".format(indx, sys.argv[indx]))
            indx += 1