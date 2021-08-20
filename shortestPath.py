# def shrtPath(T, K, N, A):
#     shortest = 9999999
#     for i in range(len(A)):
#         if A[1][i]-A[0][i] >= 0:
#             if A[2][i]-A[1][i] >= 0:
#                 if A[3][i]-A[2][i] >= 0:
#                     total = 2*(abs(A[1][i]-A[0][i]) + abs(A[2][i]-A[1][i]) + abs(A[3][i]-A[2][i]))
#                     if shortest > total:
#                         shortest = total

#     return shortest


# T = 1
# K = 2
# N = 4
# A = [(0, 1, 15, 6), (2,0,7,3),(9,6,0,12),(10,4,8,0)]
# print(shrtPath(T, K, N, A))
A = [1,2,5,4,6,4,2]
print("\n".join(str(i) for i in A[::-1]))