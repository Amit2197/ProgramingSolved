def prod(string):
    total = 0
    price = {
        'A':{
            1: 35,
            4: 100
        },
        'B':{
            1:65
        },
        'C':{
            1:50,
            6:250
        },
        'D':{
            1:85
        }
    }
    count = {e:string.count(e) for e in set(string)}
    for c in sorted(count):
        for k,v in reversed(price[c].items()):
            if count[c] > k:
                total += (count[c]//int(k))*int(v)
                count[c] = count[c] - k
            else:
                total += (count[c]//int(k))*int(v)
    return total


print(prod('ABCADABAA'))
print(prod('CCCACCCC'))
print(prod('ABCD'))

