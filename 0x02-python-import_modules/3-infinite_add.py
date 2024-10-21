#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_sum = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            total_sum += int(arg)

            print(total_sum)
