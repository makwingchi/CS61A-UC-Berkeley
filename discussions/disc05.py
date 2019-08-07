## Q1
def add_this_many(x, el, lst):
    """Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1,2,4,2,1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    count = 0
    for i in lst:
        if i == x:
            count += 1

    lst.extend([el for i in range(count)])

## Q2
def bathtub(n):
    """
    >>> annihilator = bathtub(500) # the force awakens...
    >>> kylo_ren = annihilator(10)
    >>> kylo_ren()
    490 rubber duckies left
    >>> rey = annihilator(-20)
    >>> rey()
    510 rubber duckies left
    >>> kylo_ren()
    500 rubber duckies left
    """
    def ducky_annihilator(rate):
        def ducky():
            nonlocal n
            n -= rate
            print(n, 'rubber duckies left')
        return ducky
    return ducky_annihilator

## Q3
def gen_all_items(lst):
    """
    >>> nums = [[1, 2], [3, 4], [5, 6]]
    >>> num_iters = [iter(l) for l in nums]
    >>> list(gen_all_items(num_iters))
    [1, 2, 3, 4, [5, 6]]
    """
    for el in range(len(lst)-1):
        yield from lst[el]
    yield list(lst[-1])
