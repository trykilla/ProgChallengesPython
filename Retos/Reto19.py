#!/usr/bin/python3

#Consider a list (list = []). You can perform the following commands:
#1. insert i e: Insert integer  at position . 
#2. print: Print the list.
#3. remove e: Delete the first occurrence of integer .
#4. append e: Insert integer  at the end of the list.
#5. sort: Sort the list.
#6. pop: Pop the last element from the list.
#7. reverse: Reverse the list.
#Initialize your list and read in the value of  followed by  lines of commands 
# where each command will be of the  types listed above. Iterate through each command in order 
# and perform the corresponding operation on your list.


if __name__ == '__main__':
    lista = []
    N = int(input())
    
    for i in range(N):
        com, *rest = input().split()
        if com == "insert":
            lista.insert(int(rest[0]), int(rest[1]))
        elif com == "print":
            print(lista)
        elif com == "remove":
            lista.remove(int(rest[0]))
        elif com == "append":
            lista.append(int(rest[0]))
        elif com == "sort":
            lista.sort()
        elif com == "pop":
            lista.pop()
        elif com == "reverse":
            lista.reverse()
            

            
    
            