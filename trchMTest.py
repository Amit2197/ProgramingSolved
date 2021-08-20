
# def coun(arrt):
#     d = []
#     di = dict()
#     for i in arrt:
#         di.setdefault(i, 0)
#         di[i] += 1
    
#     for key, value in di.items():
#         if value > 1:
#             print(f'{key} {value}')


# arr = [2,2,3,3,4,5,6,4,5]
# coun(arr)


# def happyornot(n, ar):
#     happy = 0
#     max = 0
#     for i in ar:
#         if i >= max:
#             happy += 1
#             max = i
        
#     return happy

# n = 9
# ar = [10, 5, 20, 20, 4, 5, 2, 25, -1]
# print(happyornot(n, ar))

# a={}
# a[2]=1
# a[1]=[2,3,4]
# print(a)

# a = 4 & 5 & 6
# print(a)

# def fun(a, b):
#     for c in range(1, 3):
#         a=c
#         b=a+c
#         if(10):
#             if(a<b):
#                 return b
#             else:
#                 return 0
#     return -1

# print(fun(2,6))
# class UserMainCode(object):
#     def charBraces(cls, input1):
#         cls = 0
#         for i in input1:
#             if cls < 0:
#                 return False
#             if i == '{':
#                 cls += 1
#             if i == '}':
#                 cls -= 1
#         return cls == 0

# cls = UserMainCode().charBraces
# print(cls('input var {'))
# print(cls('input var }'))
# print(cls('input var {}'))
# print(cls('input var { { }'))

# print(cls('input var }'))

# p = 23
# q = 12
# r = 0
# while(2):
#     r = p-q
#     p=r-10
#     if((p+5)>10):
#         break;
#     else:
#         p=p+35
#     print(p)


# def fun(a,b):
#     if(0):
#         for c in range(2,4):
#             a=a+c+2#5,10
#             b=c#2,3
#         if(a>b):
#             if(a<b):
#                 return b
#         return b+5
#     else:
#         return 0

# print(fun(1,1))

# def fun(a,b):
#     if(a>b):
#         if(b&a>a or b&a>b):
#             b=0
#     else:
#         if(b&a>1):
#             a=0
#     return a+b

# print(fun(2,2))

# def fun(a,b,c):
#     if(a+1 and b+1 and c-1):
#         c=a+1
#     return a+b+c

# print(fun(2,7,2))

# def fun(a,b,c):
#     if(b>a):
#         b=a
#     for(b)

a=7
b=21
c=32
d=b<<(a-5)
print(d)
c=c+d
print(c)
a=b+c+a
print(a)
a=a<<1
print(a)
e=a+c
print(e)
if(b or a+2 and c-b):
    e=e*2
if(e and b-12 or d/2):
    e=e/2
print(e)