#---------------#
#| Definitions |#
#---------------#

# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)

    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

## Q1
def tree_max(t):
    """Return the maximum label in a tree.

    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
    >>> tree_max(t)
    10
    """
    if is_leaf(t):
        return label(t)
    else:
        left = branches(t)[0]
        right = branches(t)[1]
        return max(label(t), label(left), label(right))

## Q2
def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    elif len(branches(t))==1:
        left_height = height(branches(t)[0])
        right_height = 0
        return left_height + 1
    else:
        left_height = height(branches(t)[0])
        right_height = height(branches(t)[1])
        return max(left_height, right_height) + 1

## Q3
def square_tree(t):
    """Return a tree with the square of every element in t"""
    return tree(label(t)**2, [square_tree(b) for b in branches(t)])

## Q4
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path

## Q5
def prune(t, k):
    """Take in a tree and a depth k and returns a new tree
    that contains only the first k levels of the original tree.
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> prune(t, 2)
    [2, [7, [3], [6]], [15]]
    """
    if k == 0:
        return tree(label(t))
    else:
        bs = [prune(b, k-1) for b in branches(t)]
        return tree(label(t), bs)

## Q6
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will
    reach N, with height H.
    >>> hailstone_tree(7,2)
    [7, [14, [28]]]
    >>> hailstone_tree(1,0)
    [1]
    >>> hailstone_tree(1,4)
    [1, [2, [4, [8, [16]]]]]
    >>> hailstone_tree(8,3)
    [8, [16, [32, [64]], [5, [10]]]]
    >>> hailstone_tree(16,3)
    [16, [32, [64, [128], [21]]], [5, [10, [20], [3]]]]
    >>> hailstone_tree(1,7)
    [1, [2, [4, [8, [16, [32, [64, [128], [21]]], [5, [10, [20], [3]]]]]]]]
    """
    if h == 0:
        return tree(n)

    left = hailstone_tree(n*2, h-1)
    right = hailstone_tree((n-1)//3, h-1)

    if (n-1) % 3 == 0 and (n-1) // 3 != 1 and ((n-1)/3) % 2 == 1:
        return tree(n, [left, right])
    else:
        return tree(n, [left])
