# Recursive implementation of the factorial function, n!.

def factorial(n):
    # precondition: n is a non-negative integer

    # base case: returns directly without making another recursive call
    if n <= 1:
        return 1

    # recursive case: reduces the problem from factorial(n) to factorial(n - 1)
    return n * factorial(n - 1)
