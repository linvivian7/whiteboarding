#######################################################################
# HOW TO FIND POWERSET #
#######################################################################


def find_powerset(s):
    """
    >>> pset = {1,2,3}
    >>> find_powerset(pset)
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    """

    result = [[]]
    for elem in s:
        result.extend([x + [elem] for x in result])
    return result


def recursive_powerset(s):

    """
    >>> pset = [1,2,3]
    >>> recursive_powerset(pset)
    [[]]
    [[], [3]]
    [[], [3], [2], [2, 3]]
    [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

    """

    if s:
        rest = recursive_powerset(s[1:])
        print rest
        return rest + [[s[0]] + x for x in rest]
    return [[]]


def bitwise_powerset(s):
    powerset = set()
    for i in xrange(2**len(s)):
        subset = tuple([x for j, x in enumerate(s) if (i >> j) & 1])
        powerset.add(subset)
    return powerset


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
