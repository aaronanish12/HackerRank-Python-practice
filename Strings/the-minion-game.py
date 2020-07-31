#!/usr/bin/env python3

def minion_game(string):
    # your code goes here
    straut=0
    kevin=0
    length = len(string)
    for i in range(length):
            if string[i] in 'AEIOU':
                kevin += length - i
            else:
                straut += length - i
    if kevin>straut:
        print(f'Kevin {kevin}')
    elif kevin<straut:
        print(f'Stuart {straut}')
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
