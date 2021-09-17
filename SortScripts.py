import random


def sort_int_list(array):
    """
    :param array:
    returns a sorted version of array using the bubble sort method in ascending order
    """
    arr = array.copy()
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Run with sample values
size = random.randint(2, 10)
arr = []
for i in range(size):
    arr.append(random.randint(1, 10000))
print('Unsorted Array: {0}'.format(arr))
print('Sorted Array: {}'.format(sort_int_list(arr)))
