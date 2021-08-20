# Majority of Element of Array
class UserMainCode(object):
    @classmethod
    def MajorityElement(cls, arr, n):
        arr = {i:arr.count(i) for i in arr}
        return max(arr.values())

a = UserMainCode().MajorityElement
s = [1,1,2,1,2,1,4,4,1,1]
print(a(s,len(s)))