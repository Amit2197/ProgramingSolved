def square(n):
    total = sum([int(i)**2 for i in str(n) if int(i)%2==0])
    return total


print(square(2798))