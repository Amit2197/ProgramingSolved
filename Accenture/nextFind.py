# Find next Letter
class UserMainCode(object):
    @classmethod
    def nextFind(cls, ch1, ch2):
        s = ord(ch2) - ord(ch1)
        cls = chr((ord(ch2)+s-97)%26+97)
        return cls

a = UserMainCode().nextFind
print(a('c', 'g'))
print(a('r', 'l'))