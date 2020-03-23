
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def num(d):
    return (ord(d) - ord('a'))
def cap(f):
    return chr(ord(str(f)) + ord('A') - ord('a'))     
def solve(s):
    t = len(s)
    for i in range(t-1):
        if i==0:
            if num(s[i]) > -1 and num(s[i])<27:
                C = cap(s[0])
                V = C
            else:
                C = s[0]
                V = C
        if s[i]==" ":
            if num(s[i+1]) > -1 and num(s[i+1])<27:
                C = V + cap(s[i+1])
                V = C
            else:
                C = V + s[i+1]
                V = C

        else: 
            C = V + s[i+1] 
            V = C
    return C

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

