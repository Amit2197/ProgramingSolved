# Superior Array Element
class UserMainCode(object):
    @classmethod
    def FindNumberOfSuperiorElements(cls, arr, n):
        count = 0
        for i in range(n-1):
            maximum = max(arr[i+1:])
            if arr[i] > maximum:
                count+=1
        count+=1

        return count

a = UserMainCode().FindNumberOfSuperiorElements
A=[2,8,9,7,4,2]
A1 = [7, 9, 5, 2, 8, 7]
print(a(A1, len(A1)))