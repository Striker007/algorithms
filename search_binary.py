from __future__ import print_function


def binary_search(list, needle):
    """ Binary search
        Complexity: best O(1), avg O(log n), worst O(log n)
    """
    low = 0
    high = len(list) - 1
    while(low <= high):
        mid = (low + high) / 2
        guess = list[mid]
        if needle == guess:
            return mid
        else:
            if needle < guess:
                high = mid - 1              
            else:
                low = mid + 1
    return None  


list = range(12, 22)
print(list)
print("position {}".format(binary_search(list, 13)))
