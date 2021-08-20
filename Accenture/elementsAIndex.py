# Elements and Indexes count if equal
class UserMainCode(object):
    @classmethod
    def eleAIndex(cls, arr, n):
        cls = 0
        if n == 0:
            return -1
        for i in range(n):
            if i==arr[i]:
                cls += 1
        return cls

a = UserMainCode().eleAIndex
arr = [10,1,12,3,5,8,9,7,12,23]
print(a(arr,len(arr)))
arr1 = []
print(a(arr1,len(arr1)))