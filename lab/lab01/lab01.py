"""Lab 1: Expressions and Control Structures"""

# Q3
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0 # You can replace this line!

# Q4
def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    digit = len(str(n)) - 1
    total = 0
    remainder = n

    while digit >= 0:
        integer = remainder // (10**digit)
        total += integer
        remainder = remainder % (10**digit)
        digit -= 1

    return total
