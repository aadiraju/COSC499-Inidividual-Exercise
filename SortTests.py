import unittest

from SortScripts import sort_int_list


class TestSortArr(unittest.TestCase):
    def test_sort_works(self):
        # Tests whether the array is sorted.
        arr = [2, 4, 1, 0, 9, 1, -10, -999, 999, 8]
        sortarr = arr.copy()
        sortarr.sort()
        self.assertEqual(sortarr, sort_int_list(arr))

    def test_original_array_is_maintained(self):
        # Tests whether the original array is tampered
        arr = [2, 4, 1, 0, 9, 1, -10, -999, 999, 8]
        arr2 = arr.copy()
        sort_int_list(arr)
        self.assertEqual(arr, arr2)


if __name__ == '__main__':
    unittest.main()
