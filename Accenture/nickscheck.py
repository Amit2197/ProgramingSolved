# Nick's Check
# return 1 if consucative number else 0
def cons(n, arr):
    arr.sort()
    check = arr[1]-arr[0]
    cls = 0
    for i in range(2,n):
        if arr[i]-arr[i-1] == check:
            cls = 1
        else:
            cls = 0
            break;
    return cls

print(cons(6,[3,7,2,5,4,6]))

