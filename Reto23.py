#!/usr/bin/python3

#You are given an immutable string, and you want to make changes to it.
#Read a given string, change the character at a given index and then print it.

def mutate_string(string, position, character):
    
    new_string = list(string)
    new_string[position] = character
    new_string = "".join(new_string)
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)