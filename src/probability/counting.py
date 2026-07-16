import math

def permutation_without_replacement(n, r):
    return math.factorial(n) // math.factorial(n - r)

def permutation_with_replacement(n, r):
    return n**r

def combination_without_replacement(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)

def combination_with_replacement(n, r):
    return math.factorial(n+r-1) // math.factorial(r) // math.factorial(n - 1)
