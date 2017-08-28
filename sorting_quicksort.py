from __future__ import print_function

import random


def quicksort(array):
    """ Quicksort
        Complexity: best O(n), avg O(n log n), worst O(n^2)
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


array = [random.randint(1,10) for _ in range(1,10)]
print(array)
print(quicksort(array))
