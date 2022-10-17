#!/usr/bin/python3

#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

from hashlib import new


def swap_case(s):
    new_string = ""
    for i in s:
        if i.isupper():
            new_string += i.lower()
        elif i.islower():
            new_string += i.upper()
        else:
            new_string += i
    
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)