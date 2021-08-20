#!/bin/python3

import sys

def euler(n):
    sum = 2
    n1 = 1
    n2 = 2
    n3 = n1+n2
    while n3 <= n:
        n1 = n2
        n2 = n3
        n3 = n1+n2
        if n2%2==0:
            sum += n2
    return sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler(n-1))