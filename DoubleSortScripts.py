import random

from SortScripts import sort_int_list


def sort_double_int_list(array):
    """
    :param array: a 2D list
    returns a sorted version of 2D array using the bubble sort method in ascending order
    """
    arr = array.copy()
    size = len(arr)
    for i in range(size):
        arr[i] = sort_int_list(arr[i])
    arr.sort()
    return arr


# Run with sample values
size = random.randint(2, 6)
arr = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(random.randint(1, 10000))
    arr.append(row)
print('Unsorted 2D Array: {0}'.format(arr))
print('Sorted 2D Array: {}'.format(sort_double_int_list(arr)))
