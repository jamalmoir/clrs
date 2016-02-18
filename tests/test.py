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
        array = [1, 15, 29, 62, 44, 103, 299, 1000, 9999]
        assert search.binary_search(array, 0, len(array) - 1, 62) == 3
        assert search.binary_search(array, 0, len(array) - 1, 45) == None
