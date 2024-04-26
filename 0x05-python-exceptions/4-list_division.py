#!/usr/bin/python3
'''function that divides element by element 2 lists.'''


def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for i in range(list_length):
        try:
            newList.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print('wrong type')
            newList.append(0)
        except ZeroDivisionError:
            print('division by 0')
            newList.append(0)
        except Exception:
            print('out of range')
            newList.append(0)
        finally:
            pass
    return newList
