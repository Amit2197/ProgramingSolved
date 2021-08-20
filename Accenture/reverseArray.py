# return array in reverse order
class UserMainCode(object):
    @classmethod
    def reverseOrder(cls, A, n):
        return A[::-1]

a = UserMainCode().reverseOrder
s=[1,2,3]
print(a(s, len(s)))