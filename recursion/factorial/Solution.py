# Recursive implementation of n! (n-factorial) calculation

# this is not a Leetcode level problem but it does help me understand recursion and how it works

def factorial(n):
    # base case: n = 0 or 1
    if n <= 1:
        return 1

    # recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)