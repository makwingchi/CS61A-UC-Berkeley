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
def complete(t, d, k):
    """Return whether t is d-k-complete.

    >>> complete(tree(1), 0, 5)
    True
    >>> u = tree(1, [tree(1), tree(1), tree(1)])
    >>> [complete(u, 1, 3), complete(u, 1, 2), complete(u, 2, 3)]
    [True, False, False]
    >>> complete(tree(1, [u, u, u]), 2, 3)
    True
    """
    if not branches(t):
        return d == 0
    bs = [complete(b, d-1, k) for b in branches(t)]
    return len(branches(t)) == k and all(bs)

## Q2
def closest(t):
    """Return the smallest difference between an entry and the sum
    of the entries of its branches.

    >>> t = tree(8, [tree(4), tree(3)])
    >>> closest(t)
    1
    >>> closest(tree(5, [t]))
    1
    >>> closest(tree(10, [tree(2), t]))
    0
    >>> closest(tree(3))
    3
    >>> closest(tree(8, [tree(3, [tree(1, [tree(5)])])]))
    2
    """
    diff = abs(label(t) - sum([label(b) for b in branches(t)]))

    return min([diff] + [closest(b) for b in branches(t)])
