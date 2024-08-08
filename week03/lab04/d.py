from lab04 import * 
def size_of_tree(t):
    """Return the number of entries in the tree.
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> size_of_tree(numbers)
    7
    """
    "*** YOUR CODE HERE ***"

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
print_tree(numbers)