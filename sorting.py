#######################################################################
# BUBBLE SORT #
#######################################################################


def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    for i in range(len(lst) - 1):

        swapped = False

        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        if not swapped:
            break

    return lst


#######################################################################
# INSERTION SORT #
#######################################################################

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key


def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        # invariant: ``seq[:i]`` is sorted
        # find the least `low' such that ``seq[low]`` is not less then `key'.
        #   Binary search in sorted sequence ``seq[low:up]``:
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1
            else:
                up = middle
        # insert key at position ``low``
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]


#######################################################################
# SELECTION SORT #
#######################################################################

def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i, len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst


#######################################################################
# MERGE SORT #
#######################################################################

def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    sorted_list = []

    while len(list2) > 0 or len(list1) > 0:
        if list1 == []:
            sorted_list.append(list2.pop())

        elif list2 == []:
            sorted_list.append(list1.pop())

        elif list1[-1] > list2[-1]:
            sorted_list.append(list1.pop())

        else:
            sorted_list.append(list2.pop())

    sorted_list.reverse()

    return sorted_list


def merge_sort(lst):
    """
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    lst1 = merge_sort(lst[:mid])
    lst2 = merge_sort(lst[mid:])

    return merge_lists(lst1, lst2)


#######################################################################
# QUICK SORT #
#######################################################################

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more


#######################################################################
# HEAP SORT #
#######################################################################

def swap(i, j):
    list[i], list[j] = list[j], list[i]


def heapify(end, i):
    l = 2 * i + 1
    r = 2 * (i + 1)
    max = i
    if l < end and list[i] < list[l]:
        max = l
    if r < end and list[max] < list[r]:
        max = r
    if max != i:
        swap(i, max)
        heapify(end, max)


def heap_sort():
    end = len(list)
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(end, i)
    for i in range(end-1, 0, -1):
        swap(i, 0)
        heapify(i, 0)


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
