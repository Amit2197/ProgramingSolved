def cuckoo(n):
    Cockoo = {
        1: 0,
        2: 1
    }
    if n>2:
        for i in range(3,n+1):
            Cockoo[i] = 1*Cockoo[i-1]+2*Cockoo[i-2]+3*1
    return Cockoo[n]

print(cuckoo(1))