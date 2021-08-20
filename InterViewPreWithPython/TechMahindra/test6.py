# Q2. Odd Even Difference


# Write a program to return the difference between the sum of odd and even numbers from an array of positive integers.


# Note:

# You are expected to write code in the findOddEvenDifference function only which will receive the first parameter as the number of items in the array and the second parameter is the array itself. You are not required to take input from the console


# Example:

# Finding the difference between the sum of odd-even numbers from a list of 5 numbers


# Input

# 5

# 10 11 7 12 14


# Output

# -18


# Explanation

# Sum of Odd - Sum of Even => 18-36 = -18

def findOddEvenDifference(l, ar):
    diff = 0
    for i in ar:
        if i > 0:
            diff += i if i%2 !=0 else -i
    return diff

print(findOddEvenDifference(5, [10, 11, 7, 12, 14]))