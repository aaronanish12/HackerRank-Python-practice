#!/usr/bin/env python3
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxx = max(arr)
    while max(arr) == maxx:
        arr.remove(maxx)
    print(max(arr))

