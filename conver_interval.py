def converge_intervals(a, b):
    """
    >>> A = [(1, 2), (3, 4), (7, 10)]
    >>> B = [(0, 2), (3, 8), (9, 12)]
    >>> converge_intervals(A, B)
    [(1, 2), (3, 4), (7, 8), (9, 10)]
    >>> converge_intervals(B, A)
    [(1, 2), (3, 4), (7, 8), (9, 10)]

    """

    result = []

    for i in range(0, len(a)):

        if b[i][0] >= a[i][1] or a[i][0] >= b[i][1]:
            if b[i][0] >= a[1][1]:
                lower, upper = a[i]
            else:
                lower, upper = b[i]
            result.append((lower, upper))
            break

        if a[i][0] >= b[i][0]:
            lower = a[i][0]
        else:
            lower = b[i][0]

        if a[i][1] <= b[i][1]:
            upper = a[i][1]
        else:
            upper = b[i][1]
        result.append((lower, upper))

        if i < len(a) - 1:
            if b[i][1] in range(a[i+1][0], a[i+1][1]+1):
                lower1 = a[i+1][0]
                upper1 = b[i][1]
                result.append((lower1, upper1))

            elif a[i][1] in range(b[i+1][0], b[i+1][1]+1):
                lower1 = b[i+1][0]
                upper1 = a[i][1]
                result.append((lower1, upper1))
    return result

#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
