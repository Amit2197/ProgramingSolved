# find maximum index product
# code from codescript.in
class UserMainCode(object):
    @classmethod
    def maxIndexProduct(cls, arr, n):
        product = 0
        if n==0:
            return -1
        for j in range(1, n-1):
            left = 0
            right = 0
            for k in range(j-1,-1,-1):
                if arr[k]>arr[j]:
                    left = k
                    break
            for l in range(j+1,n):
                if arr[l]>arr[j]:
                    right = l
                    break
            if product < left*right:
                product = left*right
        cls = product
        return cls


a = UserMainCode().maxIndexProduct
input1 = [-3,4,3,6,4,5,-2]
input2 = [1,5,4,3,5,2]
print(a(input1,len(input1)))
print(a(input2, len(input2)))