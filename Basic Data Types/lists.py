#!/usr/bin/env python3
n= int(input())
lst=[]
for i in range(0,n):
    com = input()
    command = com.split(" ")
    if(command[0] == "insert"):
        i = int(command[1])
        e = int(command[2])
        lst.insert(i,e)
    elif(command[0]== "print"):
        print(lst)
    elif(command[0] == "remove"):
        lst.remove(int(command[1]))
    elif(command[0] == 'append'):
        lst.append(int(command[1]))
    elif(command[0] == "pop"):
        lst.pop()
    elif(command[0] == "sort"):
        lst.sort()
    elif(command[0] == "reverse"):
        lst.reverse()

    else:
        pass


