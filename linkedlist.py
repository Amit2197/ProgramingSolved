def func(A):
    last = A[-1]
    A = [A[i] for i in range(len(A)-1) if A[i] > A[i+1]]
    A.append(last)
    return A


A = list(map(int, input().split(' ')))
print(func(A))