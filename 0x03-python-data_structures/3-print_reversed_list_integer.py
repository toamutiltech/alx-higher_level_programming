#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = len(my_list)
    for i in my_list:
        print("{:d}".format(i))
        i -= 1
