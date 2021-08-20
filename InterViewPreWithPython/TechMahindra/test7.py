# Q4. Calculate Total Tax


# Write a program to calculate the total bill tax amount for a list of billing amounts passed as an array of long integers.

# Up to the amount 1000, there is no tax applicable, subsequently, a flat tax of 10% is applicable for the remaining amount as per the tax rate.


# Note: 

# All calculations and results should be integer-based ignoring fractions

# You are expected to write code int the calcTotalTax function only which will receive the first parameter as the number of items in the array and the second parameter is the array itself. You are not required to take input from the console.


# Example

# Calculating total tax for a list of 5 billing amount


# Input

# 5

# 1000 2000 3000 4000 5000


# Output

# 1000


# Explanation

# The first parameter (5) is the size of the array. Next is an array of billing amounts For the first amount there will be 0 tax and for the next amount, it will be 10% of(2000-1000)=100 and so on.

# The sum of all the tax amounts will be (0+100+200+300+400=1000)

def calcTotalTax(l, billarr):
    totaltax = 0
    for i in billarr:
        totaltax += ((i-1000) * 10 // 100)
    return totaltax


print(calcTotalTax(5, [1000, 2000, 3000, 4000, 5000]))