# Mango Distribution
class UserMainCode(object):
    @classmethod
    def mangoDistribution(cls, input1, input2):
        cls = 1
        N = input1+input2-1
        R=input2 - 1
        for i in range(1, R+1):
            cls *= (N-R + i)
            cls /= i
        return int(cls)

a = UserMainCode().mangoDistribution
print(a(2,2))
print(a(1,12))