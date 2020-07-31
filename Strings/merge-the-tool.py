#!/usr/bin/env python3

def merge_the_tools(string, k):
    list1=[]
    
    i=0
    while string:
        s = string[0:k]
        seen = ''
        for c in s:
            if c not in seen:
                seen += c
        print(seen)
        string = string[k:]
        # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

