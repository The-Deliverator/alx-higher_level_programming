#!/usr/bin/python3
def pow(a, b):
    result = 1
    for _ in range(abs(b)):
        result *= a
    return result if b >= 0 else 1 / result
