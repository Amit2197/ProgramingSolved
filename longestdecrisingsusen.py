# def lds(n, A):
#     ldcA = [A[0]]
#     ldcB = []
#     for i in A:
#         if i < ldcA[-1]:
#             ldcA.append(i)
#         else:
#             ldcB = ldcA[:] if len(ldcA) > len(ldcB) else ldcB
#             ldcA = [i]
#     ldcB = ldcA[:] if len(ldcA) > len(ldcB) else ldcB

#     return len(ldcB)

# print(lds(5, [41, 18467, 6334, 26500, 19169]))
# print(lds(7, [4, 6, 5, 7, 2, 9, 1]))

# def longest_decreasing_sublist(a):
#   lds, current = [], [a[0]]
#   for val in a[1:]:
#     if val < current[-1]: current.append(val)
#     else:
#       lds = current[:] if len(current) > len(lds) else lds
#       current = [val]
#   lds = current[:] if len(current) > len(lds) else lds
#   return lds

# L = [1, 2, 1, 2, 1, 2, 1, 2, 1]
# print (longest_decreasing_sublist(L))

def lds(n, A):
    ldsA = {1: [A[0]]}
    for i in A[1:]:
        for j in ldsA:
            if i < ldsA[j][-1]:
                ldsA[j].append(i)
        ldsA[len(ldsA)+1] = [i]
    lenM = max(len(value) for value in ldsA.values())
    return lenM


print(lds(5, [41, 18467, 6334, 26500, 19169]))
print(lds(7, [4, 6, 5, 7, 2, 9, 1]))