#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    char = chr(i)
    if char not in ['q', 'e']:
        print('{}'.format(char), end='')
