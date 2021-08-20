# Reverse String
# source code suggestion from leetcode
class UserMainCode(object):
    @classmethod
    def ReverseString(cls, s):
        letter = [i for i in s if i.isalpha()]
        ans = [letter.pop() if i.isalpha() else i for i in s]
        return "".join(ans)

a = UserMainCode().ReverseString
s= 'a^bk$c'
print(a(s))