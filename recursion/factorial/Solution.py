# Recursive implementation of the factorial function, n!.

def factorial(n):
    # precondition: n is a nonnegative integer

    # base case: return directly without making another recursive call
    if n <= 1:
        return 1

    # recursive case: reduce the problem from factorial(n) to factorial(n - 1)
    return n * factorial(n - 1)
