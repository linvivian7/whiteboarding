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


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
