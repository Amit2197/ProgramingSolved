# Q1. Find Large Small Difference


# Write a program to return the difference between the largest and smallest numbers from an array of positive integers.


# Note:

# You are expected to write code in the findLargeSmallDifference function only which will receive the first parameter as the number of items in the array and the second parameter is the array itself. You are not required to take input from the console.



# Example:

# Finding the difference between the largest and smallest from a list of 5 numbers.


# Input

# Input1: 5

# Input2: 10 11 7 12 14


# Output

# 7


# Explanation:

# The first parameter(5) is the size of the array. Next is an array of integers. The difference between largest (14) and smallest(7) is 7.


# Code Solution in C++:

# Input1: 5

# Input2: 10 11 7 12 14


def findLargeSmallDifference(l, arlist):
    arlist.sort()
    return arlist[-1]-arlist[0]

print(findLargeSmallDifference(5, [10, 11, 7, 12, 14]))
