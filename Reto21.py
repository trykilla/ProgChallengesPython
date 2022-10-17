#!/usr/bin/python3

#You are given a string. Split the string on a " " delimeter and join using a- hyphen.


def split_and_join(line):
    new_line = line.split(" ")
    new_line = "__".join(new_line)
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

