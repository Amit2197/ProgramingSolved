# Find Frequency
class UserMainCode(object):
    @classmethod
    def findFrequency(cls, ch, s, n):
        return s.count(ch)

a = UserMainCode().findFrequency
ch = 'a'
s= 'abrakadabra'
print(a(ch, s, len(s)))