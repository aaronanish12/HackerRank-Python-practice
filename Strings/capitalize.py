#!/usr/bin/env python3

import string
# Complete the solve function below.
def solve(s):
    return string.capwords(s,sep=' ')
s = input()
solve(s)
