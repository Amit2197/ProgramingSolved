# Number of Unique Character
class UserMainCode(object):
    @classmethod
    def numberUniqueCharacter(cls, s):
        if s == '':
            return -1
        cls = len(set(i for i in s))
        return cls

a = UserMainCode().numberUniqueCharacter
print(a('efeefhjg'))