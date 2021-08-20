# sum of product in two array
class UserMainCode(object):
    @classmethod
    def sumOfProduct(cls, arr1, arr2, n):
        total = sum([arr1[i]*arr2[::-1][i] for i in range(n)])
        return total

a = UserMainCode().sumOfProduct
arr1 = [22,7,1,-5,5,-2]
arr2 = [4, -1, 21,12,10,-3]
print(a(arr1, arr2,len(arr1)))