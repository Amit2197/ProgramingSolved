# limit = 6
# n1 = 0
# n2 = 1
# n3 = 1
# count = 1
# while count <= limit {
#     count = count + 1
#     print(n3)
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3}
# end

# def fun(x, y):
#     if x>1:
#         fun(x-2, y+2)
#     print(y)

# print(fun(4, 5))


# b = 18
# c = 12
# a = 6
# for c in range(1, a-1):
#     b = b+c+12
#     b=b/5
#     d=b+a
#     print(b)
# c = a+b+c
# print(a,b,c)

# for i in range(4,-1,-1):
#     print(i)

# a=9
# b=4
# c=7
# for c in range(3,4+1):
#     b=(3+8)+c
#     if ((b+4)<(4-b)):
#         continue
#     else:
#         break
#     a=8+c
#     print(a)
# print(a+b)
# a=4
# b=11
# c=10
# c=(7^12)&a
# for c in range(3,7):
#     a=(7+7)+a
#     a=(11+1)^a
#     print(a)
# print(a+b)

# a=1
# b=7
# c=8
# for c in range(2,7):
#     b=2+c
#     a=(3+5)+a
#     print(a)
# print(a)

# def fun(a,b,c):
#     for c in range(4,8):
#         print(f'loop')
#         b=c+c
#         if((a+b)<(c-a)):
#             print('if')
#             continue
#         else:
#             b=3^c
#             c=b+a
#     return a+b

# print(fun(1,8,10))
# a=4
# b=8
# c=11
# for c in range(2,5):
#     a=b+b
#     print(f'{c}={a}')
#     if((b^c)<c):
#         print(f'{c}=if')
#         continue
#     else:
#         a=a
#         print(f'{c}={a}')
#         b=c
#         print(f'{c}={b}')
#     print(f'{c}={c}')
# print(a+b)
# a=7
# b=5
# for c in range(2,5):
#     if(a<b):
#         a=1
#         print(b)
#         b=a
#     else:
#         if a >b:
#             a=b
#         else:
#             a=a+1
#     b=b+11
# print(a+b)

# a = 5
# b = 1
# def fun(a,b):
#     if((b+a or a-b) and (b>a) and 1):
#         a=a+b+b-2
#         return(3-a)
#     else:
#         return(a-b+1)
#     return(a+b)
# print(fun(a,b))

# a=4
# b=9
# c=9
# if(b&(c>>1)):
#     a=a+1
# print(a+b+c)

# s = '3 + 5 = x'
# A = s.split('=')
# print(f'{A[0].strip()} = {eval(A[0])}')
# print(A)
# for i in range(5,0, -1):
#     print(i)
# print(list(1*i for i in range(5,0,-1)))
# # reverse string word wise
# s='Welcome to mettl'
# print(' '.join(s.split(' ')[::-1]))

# def main():
#     a=0
#     b=
# b=5
# a=2
# c=2
# print(0)
# *((a+1==1)?&b:&a)=a?b:c
# x=123
# i={
#     print("c" "++")
# }
# print(len(i))
# for x in i:
#     print(x)

def sample(n):
    i=0
    s=0
    n=127
    while(n>0):
        r=n%10
        p=8^i
        s=s+p*r
        i+=1
        n=n/10
    return s

print(sample(127))