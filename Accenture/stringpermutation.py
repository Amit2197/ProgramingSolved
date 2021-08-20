# string permutations
def strPermutation(a,b):
    return 'yes' if sorted(a)==sorted(b) else 'no'

print(strPermutation('zbk','zkb'))
