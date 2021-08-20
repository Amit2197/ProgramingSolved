# Largest Prime Factor of a number
def LargestPrime(N):
    i = 2
    largest_prime = 2
    while i*i <= N:
        while N % i == 0:
            largest_prime = i
            N //= i    
        i += 1
    if N>largest_prime:
        largest_prime = N
    return largest_prime

print(LargestPrime(120))