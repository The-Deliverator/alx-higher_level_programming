#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    x_ele = 0
    for el in range(x):
        try:
            print("{:d}".format(my_list[el]), end="")
            x_ele += 1
        except (ValueError, TypeError):
            pass
    print()
    return (x_ele)
