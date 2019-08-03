### Q1
def print_numbers(n, k):
    """Print all numbers that (A) can be formed from the digits of `n`
    in reverse order and (B) are multiples of `k`

    Args:
        n(int): the number that results must use digits from.
        k(int): the number that results must be multiples of.

    >>> print_numbers(97531, 5)
    135
    15
    35
    >>> print_numbers(97531, 7)
    1379
    357
    35
    >>> print_numbers(97531, 2)
    """
    def inner(n, s):
        if n == 0:
            if s > 10 and s % k == 0:
                print(s)
        else:
            inner(n//10, s*10 + n%10)
            inner(n//10, s)

    inner(n, 0)

### Q2
def sixty_ones(n):
    """Return the number of times that a 1 directly follows a 6 in the digits of n.

    Args:
        n(int): the number whose digits are to be examined

    Returns:
        int: the number of occurrences

    >>> sixty_ones(461601)
    1
    >>> sixty_ones(161461601)
    2
    """
    if n < 10:
        return 0
    elif n % 10 == 1 and (n // 10) % 10 == 6:
        return 1 + sixty_ones(n//10//10)
    else:
        return sixty_ones(n//10)

### Q3
def no_elevens(n):
    """Return the number of n-digit numbers whose digits consist of 1's
    and 6's and do not contain a 1 and then another 1 consecutively.

    Args:
        n(int): the length of the numbers

    Returns:
        int: the number of numbers

    >>> no_elevens(2) # 66, 61, 16
    3
    >>> no_elevens(3) # 666, 661, 616, 166, 161
    5
    """
    if n == 1:
        return 2 # 1 & 6
    elif n == 2:
        return 3
    else:
        return no_elevens(n-1) + no_elevens(n-2)
