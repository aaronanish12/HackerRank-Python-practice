#!/usr/bin/env python3

def count_substring(string, sub_string):
    i=0
    lis1=[]
    while i <= len(string)-3:
        lis1.append(string[i:(i+len(sub_string))])
        i+=1
    return lis1.count(sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
