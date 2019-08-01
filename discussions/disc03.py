### 1.1
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(k, n):
        if n == 1:
            return False
        elif k == n:
            return True
        else:
            return n % k != 0 and prime_helper(k+1, n)


    return prime_helper(2, n)

### 1.2
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x+1, 1)
    >>> incr_1(5)
    6
    >>> incr_1(2)
    3
    """
    def repeat(n):
        if n == 1:
            return f(x)
        else:
            return f(repeat(n-1))

    return repeat

### 2.1
def count_stair_ways(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

### 2.2
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2+1, 1+2, 1+1+1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # only one step at a time
    1
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    total = 0
    i = 1
    while i <= k:
        total += count_k(n-i, k)
        i += 1

    return total

### 2.3
def pascal(row, column):
    if row < 0 or column < 0:
        return 0
    elif row == 0 and column == 0:
        return 1
    elif row < column:
        return 0
    else:
        return pascal(row-1, column) + pascal(row-1, column-1)
