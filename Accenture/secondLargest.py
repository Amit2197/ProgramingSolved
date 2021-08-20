# Arrangement
class UserMainCode(object):
    @classmethod
    def secondLargest(cls, n, arr):
        return sorted(arr)[-2] if arr else -1


a = UserMainCode().secondLargest
A=[]
A1 = [7, 9, 5, 2, 8, 7]
print(a(len(A1), A1))