#!/bin/python3

import sys

# 10 - factor - 1,2,5,10
# 20 - factor - 1,2,4,5,10,20
# 17 - factor - 1, 17

def euler(N):
    i = 2
    largest_prime = 2
    while i*i <= N:
        while N % i == 0:
            largest_prime = i
            N //= i    
        i += 1
    if N>largest_prime:
        largest_prime = N;
    return largest_prime



# T = int(input())
# for z in range(T):
#     N = int(input())
    
print(euler(10))
print(euler(20))
print(euler(17))
print(euler(25))
print(euler(11))
