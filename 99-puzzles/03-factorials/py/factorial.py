#!/usr/bin/env python3

import sys

def factorial(n):
    factorials = [1] * n
    for i in range(1,n):
        factorials[i] = factorials[i-1] * i
    return factorials[n-1] * n

print(factorial(int(sys.argv[1])))
