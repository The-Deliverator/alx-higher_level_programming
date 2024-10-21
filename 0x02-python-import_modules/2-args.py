#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("Number of argument(s):.")
    else:
        if num_args == 1:
            print("Number of argument(s):argument")

        else:
            print("Number of argument(s):arguments")

        for i in range(1, num_args + 1):
            print(str(i) + ": " + sys.argv[i])
