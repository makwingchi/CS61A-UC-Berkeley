# Implement the longest_increasing_suffix function, which returns
# the longests suffix (end) of a positive integer that consists of
# strictly increasing digits.

def longest_increasing_suffix(n):
    """Return the longest increasing suffix of a positive integer n.
    >>> longest_increasing_suffix(63134)
    134
    >>> longest_increasing_suffix(233)
    3
    >>> longest_increasing_suffix(5689)
    5689
    >>> longest_increasing_suffix(568901) # 01 is the suffix, displayed as 1
    1
    """
    m, suffix, k = 10, 0, 1
    while n:
        n, last = n // 10, n % 10
        if m > last:
            m, suffix, k = last, suffix + k * last, 10 * k
        else:
            return suffix

    return suffix


def sandwich(n):
    """Return True if n contains a sandwich and False otherwise
    >>> sandwich(416263) # 626
    True
    >>> sandwich(5050) # 505 or 050
    True
    >>> sandwich(4441) # 444
    True
    >>> sandwich(1231)
    False
    >>> sandwich(55)
    False
    >>> sandwich(4456)
    False
    """
    tens, ones = n // 10, n % 10
    n = n // 100
    while n > 0:
        if n % 10 == ones:
            return True
        else:
            tens, ones = tens // 10, tens % 10
            n = tens // 10 % 10

    return False


# Implement luhn_sum. The Luhn sum of a non-negative integer n adds the sum of each
# digit in an even position to the sum of doubling each digit in an odd position. If
# doubling an odd digit results in a two-digit number, those two digits are summed to
# form a single digit. You may not use recursive calls or call find_digit in your solution.

def luhn_sum(n):
    """Return the Luhn sum of n.
    >>> luhn_sum(135)
    12
    >>> luhn_sum(185)
    13
    >>> luhn_sum(138743)
    30
    """
    def luhn_digit(digit):
        x = digit * multiplier
        return (x // 10) + (x % 10)

    total, multiplier = 0, 1
    while n:
        n, last = n // 10, n % 10
        total = total + luhn_digit(last)
        multiplier = 3 - multiplier

    return total
