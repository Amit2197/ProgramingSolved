# Replace X with Value
class UserMainCode(object):
    @classmethod
    def ReplaceX(cls, s):
        s = s.split('=')
        if 'X' in s[0]:
            s1 = [i for i in s[0] if i != ' ']
            evalOperator = {
                '+': '-',
                '-': '+',
                '*': '/',
                '/': '*'
            }
            if 'X' in s1[0]:
                subs = eval(s[1]+ evalOperator[s1[1]] +s1[2])
                s1[0] = str(int(subs) if subs%1 == 0 else round(subs,2))
            if 'X' in s1[2]:
                subs = eval(s[1]+ evalOperator[s1[1]] +s1[0])
                s1[2] = str(int(subs) if subs%1 == 0 else round(subs,2))
            s[0] = f'{s1[0].strip()} {s1[1].strip()} {s1[2].strip()}'
        else:
            return f'{s[0].strip()} = {eval(s[0])}'
        return f'{s[0].strip()} = {s[1].strip()}'

        


a = UserMainCode().ReplaceX
s = '3 + X = 8'
print(a(s))