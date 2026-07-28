def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

def permutation_without_replacement(n, r):
    if n < 0 or r < 0:
        raise ValueError("Inputs must be non-negative.")
    # if r > n, return 0, since it's not feasible
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)

def permutation_with_replacement(n, r):
    if n < 0 or r < 0:
        raise ValueError("Inputs must be non-negative.")
    return n**r

def combination_without_replacement(n, r):
    if n < 0 or r < 0:
        raise ValueError("Inputs must be non-negative.")
    # if r > n, return 0, since it's not feasible
    if r > n:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)

def combination_with_replacement(n, r):
    if n < 0 or r < 0:
        raise ValueError("Inputs must be non-negative.")
    return factorial(n+r-1) // factorial(r) // factorial(n - 1)
