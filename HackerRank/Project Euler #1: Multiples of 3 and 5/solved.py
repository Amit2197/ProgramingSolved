#!/bin/python3
import sys
def sum(n, k):
    d = n // k
    return k * (d * (d+1)) // 2
  
def euler(n):
    return sum(n, 3) + sum(n, 5) - sum(n, 15)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler(n-1))