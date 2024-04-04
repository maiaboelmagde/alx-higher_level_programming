#!/usr/bin/python3
def fizzbuzz():
    indx=0
    while (indx < 100):
        flag = 1
        indx += 1
        if (indx % 3 == 0):
            print('Fizz',end='')
            flag = 0
        if (indx % 5 == 0):
            print('Buzz',end='')
            flag = 0
        if flag:
            print(indx, end='')
        print(' ', end='')
