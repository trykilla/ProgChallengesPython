#!/usr/bin/python3

# You are given a string S
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.


def main(string, res):

    for i in str(string):
        res[0].append(i.isalnum())
        res[1].append(i.isalpha())
        res[2].append(i.isdigit())
        res[3].append(i.islower())
        res[4].append(i.isupper())

    for i in res:
        print(any(i))

if __name__ == '__main__':
    string = input()
    res = [[], [], [], [], []]
    main(string, res)
