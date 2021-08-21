# Straight or not equation
class UserMainCode(object):
    @classmethod
    def checkStraight(cls, n, arr):
        x = [arr[i] for i in range(0, len(arr), 2)]
        y = [arr[i+1] for i in range(0, len(arr), 2)]
        m = (y[1] - y[0])/(x[1]-x[0])
        for i in range(1,n-1):
            m1 = (y[i+1] - y[i])/(x[i+1]-x[i])
            if m != m1:
                return 0
        c = (y[0]*x[1])-(x[0]*y[1])
        a=1
        y=eval(str(y[0]-m*x[0]))
        # eval(str([y[0]-m*x[0]]))
        return f'{a}x {y}y = {c}'

check = UserMainCode().checkStraight
print(check(3,[1,1,2,2,3,3]))