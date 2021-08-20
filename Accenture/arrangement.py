# Arrangement
class UserMainCode(object):
    @classmethod
    def reArrange(cls, n, arr):
        return sorted(arr)

a = UserMainCode().reArrange
A=[2,8,9,7,4,2]
print(a(len(A), A))