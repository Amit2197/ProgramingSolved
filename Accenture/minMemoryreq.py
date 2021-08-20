# Minimum Memory required
class UserMainCode(object):
    @classmethod
    def MinMemory(cls, arr, n):
        k = 0
        if not arr:
            return -1
        while pow(2,k)<sum(arr):
            k += 1
        return pow(2,k)
a = UserMainCode().MinMemory
s = []
print(a(s,len(s)))