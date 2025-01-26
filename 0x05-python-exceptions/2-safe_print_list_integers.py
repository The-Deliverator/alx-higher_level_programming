def safe_print_list_integers(my_list=[], x=0):
    count = 0
    gen = (i for i in range(x))
    for i in gen:
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            continue
    print("")
    return count
