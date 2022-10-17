#!/usr/bin/python3

# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

import re


def count_substring(string, sub_string):
    pattern = re.compile(sub_string)
    pos = 0
    count = 0
    for i in range(pos, len(string)):
        s = re.search(pattern, string[pos:])
        if s:
            count += 1
            pos += s.start() + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
