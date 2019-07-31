def keep_ints1(cond, n):
    '''Print out all integers 1...i...n where cond(i) is true

    >>> def is_even(x):
    ...     return x % 2 == 0

    >>> keep_ints1(is_even, 5)
    2
    4
    '''
    for i in range(1, n+1):
        if cond(i):
            print(i)

def keep_ints2(n):
    '''Returns a function which takes one parameter cond and prints out
    all integers 1...i...n where calling cond(i) returns True

    >>> def is_even(x):
    ...     return x % 2 == 0

    >>> keep_ints2(5)(is_even)
    2
    4
    '''
    def func(cond):
        for i in range(1, n+1):
            if cond(i):
                print(i)

    return func

def multiply(m, n):
    '''
    >>> multiply(5, 3)
    15
    '''
    if n == 1:
        return m

    return multiply(m, n-1) + m

def countdown(n):
    '''
    >>> countdown(3)
    3
    2
    1
    '''
    print(n)
    if n == 1:
        return

    countdown(n-1)

def countup(n):
    '''
    >>> countup(3)
    1
    2
    3
    '''
    if n == 1:
        print(n)
        return

    countup(n-1)
    print(n)

def sum_every_other_digit(n):
    '''
    >>> sum_every_other_digit(7)
    7
    >>> sum_every_other_digit(30)
    0
    >>> sum_every_other_digit(228)
    10
    >>> sum_every_other_digit(123456)
    12
    >>> sum_every_other_digit(1234567) # 1 + 3 + 5 + 7
    16
    '''
    if n < 10:
        return n

    all_but_the_last_and_the_second_last, last = (n // 10) // 10, n % 10

    return sum_every_other_digit(all_but_the_last_and_the_second_last) + last
