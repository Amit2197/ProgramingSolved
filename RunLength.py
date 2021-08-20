#!/usr/bin/env python3
def fun(s):
    l = ""
    count = 0
    param = ""
    for i in s:
        if i != l:
            if l:
                param += str(count)+l
            l = i
            count = 1
        else:
            count += 1
    param += str(count)+l


    return param

print(fun("aaabbcccw"))