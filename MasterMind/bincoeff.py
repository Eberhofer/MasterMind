def binomial_coeff(n, k):
    """
        returns the binomial coefficient n choose k.
    """
    if n < k:
        raise ValueError('k > n is not allowed in binomial_coeff(n, k).')
    if type(n) != int or type(k) != int:
        raise ValueError('binomial_coeff(n,k) is only defined for integer n and k.')
    return int(factorial(n)/(factorial(k) * factorial(n-k)))
