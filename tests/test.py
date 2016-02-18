import pytest
from .context import clrs

class TestSearching:

    def test_linear_search(self):
        search = clrs.searching.Search()
        array = [1, 35, 99, 62, 33, 44, 98, 2362, 56]
        assert search.linear_search(array, 62) == 3
        assert search.linear_search(array, 2) == None

    def test_binary_search(self):
        search = clrs.searching.Search()
        array = [1, 15, 29, 32, 44, 103, 299, 1000, 9999]
        assert search.binary_search(array, 0, len(array) - 1, 44) == 4
        assert search.binary_search(array, 0, len(array) - 1, 1) == 0
        assert search.binary_search(array, 0, len(array) - 1, 9999) == 8
        assert search.binary_search(array, 0, len(array) - 1, 45) == None


class TestSorting:

    def test_insertion_sort(self):
        sort = clrs.sorting.Sort()
        array_1 = [2, 45, 78, 55, 678, 34, 69999, 9999, 34, 45]
        array_2 = [999, 100, 24555, 90, 1, 54, 2]
        array_3 = [2, 1]
        array_4 = [1, 2, 3, 4, 5]

        sort.insertion_sort(array_1, 1)
        sort.insertion_sort(array_2, -1)
        sort.insertion_sort(array_3, 1)
        sort.insertion_sort(array_4, 1)

        assert array_1 == [2, 34, 34, 45, 45, 55, 78, 678, 9999, 69999]
        assert array_2 == [24555, 999, 100, 90, 54, 2, 1]
        assert array_3 == [1, 2]
        assert array_4 == [1, 2, 3, 4, 5]

    def test_selection_sort(self):
        sort = clrs.sorting.Sort()
        array_1 = [2, 45, 78, 55, 678, 34, 69999, 9999, 34, 45]
        array_2 = [999, 100, 24555, 90, 1, 54, 2]
        array_3 = [2, 1]
        array_4 = [1, 2, 3, 4, 5]

        sort.selection_sort(array_1)
        sort.selection_sort(array_2)
        sort.selection_sort(array_3)
        sort.selection_sort(array_4)

        assert array_1 == [2, 34, 34, 45, 45, 55, 78, 678, 9999, 69999]
        assert array_2 == [1, 2, 54, 90, 100, 999, 24555]
        assert array_3 == [1, 2]
        assert array_4 == [1, 2, 3, 4, 5]

    def test_merge_sort(self):
        sort = clrs.sorting.Sort()
        array_1 = [2, 45, 78, 55, 678, 34, 69999, 9999, 34, 45]
        array_2 = [999, 100, 24555, 90, 1, 54, 2]
        array_3 = [2, 1]
        array_4 = [1, 2, 3, 4, 5]

        sort.merge_sort(array_1, 0, len(array_1) - 1)
        sort.merge_sort(array_2, 0, len(array_2) - 1)
        sort.merge_sort(array_3, 0, len(array_3) - 1)
        sort.merge_sort(array_4, 0, len(array_4) - 1)

        assert array_1 == [2, 34, 34, 45, 45, 55, 78, 678, 9999, 69999]
        assert array_2 == [1, 2, 54, 90, 100, 999, 24555]
        assert array_3 == [1, 2]
        assert array_4 == [1, 2, 3, 4, 5]
