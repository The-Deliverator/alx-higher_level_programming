#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("Number of argument(s):.")
    else:
        arg_word = "argument" if num_args == 1 else "arguments"
        print("Number of argument(s):{}".format(arg_word))

        for i in range(1, num_args + 1):
            print("{}: {}".format(i, sys.argv[i]))
