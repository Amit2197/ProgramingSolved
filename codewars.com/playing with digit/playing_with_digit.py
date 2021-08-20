def dig_pow(n, p):
    # your code
    sum = 0
    for x in range(len(str(n))):
        power = pow(int(str(n)[x]), p + x)
        sum += power
    if sum % n == 0:
        return sum // n
    return -1



dig_pow(89, 1)
dig_pow(92, 1)
dig_pow(46288, 3)