# Q1: Insect Combinatorics
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 and n == 1:
        return 1
    elif m < 1 or n < 1:
        return 0
    else:
        return paths(m - 1, n) + paths(m, n - 1)
    
print(paths(2, 2))
print(paths(5, 7))
print(paths(117, 1))
print(paths(1, 157))