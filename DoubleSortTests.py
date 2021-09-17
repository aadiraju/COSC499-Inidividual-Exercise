import unittest

from DoubleSortScripts import sort_double_int_list


class TestSortArr(unittest.TestCase):
    def test_sort_works(self):
        # Tests whether the array is sorted.
        arr = arr = [[2, 4, 1], [0, 9, 1], [-10, -999, 999]]
        sortarr = arr.copy()
        sortarr.sort()
        for item in sortarr:
            item.sort()
        self.assertEqual(sortarr, sort_double_int_list(arr))

    def test_original_array_is_maintained(self):
        # Tests whether the original array is tampered
        arr = [[2, 4, 1], [0, 9, 1], [-10, -999, 999]]
        arr2 = arr.copy()
        sort_double_int_list(arr)
        self.assertEqual(arr, arr2)


if __name__ == '__main__':
    unittest.main()
