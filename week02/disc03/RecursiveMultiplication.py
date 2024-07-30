def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"

    if n == 1:
        return m * n
    else:
        return m + multiply(m, n - 1)
    
print(multiply(5, 3))