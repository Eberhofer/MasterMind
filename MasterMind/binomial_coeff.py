"""
    binomial_coeff.py module
    ------------------------
"""
from math import factorial

def binomial_coeff(degree, coefficient):
    """
        Returns the binomial coefficient n choose k.
        n is the degree of the factorial and k the degree.
    """
    if degree < coefficient:
        raise ValueError('k > n is not allowed in binomial_coeff(n, k).')
    if not isinstance(degree, int) or not isinstance(coefficient, int):
        raise ValueError('binomial_coeff(n,k) is only defined for integer n and k.')
    return int(factorial(degree)/(factorial(coefficient) * factorial(degree-coefficient)))
