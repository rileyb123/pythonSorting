from bubble_sort import *
from insertion_sort import *
from merge_sort import merge_sort
from quick_sort import *


class TestSorts:

    def test_bubble_sort_basic(self):
        arr = [1,4,8,2,7,5,6,4,5,9]
        sorted_arr = [1,2,4,4,5,5,6,7,8,9]
        assert bubble_sort(arr) == sorted_arr , "arr did not match sorted array"

    def test_bubble_sort_empty(self):
        arr = []
        sorted_arr = []
        assert bubble_sort(arr) == sorted_arr , "arr did not match sorted array"

    def test_insertion_sort_basic(self):
        arr = [1,4,8,2,7,5,6,4,5,9]
        sorted_arr = [1,2,4,4,5,5,6,7,8,9]
        insertion_sort(arr)
        assert arr == sorted_arr , "arr did not match sorted array"

    def test_insertion_sort_empty(self):
        arr = []
        sorted_arr = []
        insertion_sort(arr)
        assert arr == sorted_arr , "arr did not match sorted array"
    
    def test_merge_sort_basic(self):
        arr = [1,4,8,2,7,5,6,4,5,9]
        sorted_arr = [1,2,4,4,5,5,6,7,8,9]
        merge_sort(arr)
        assert arr == sorted_arr , "arr did not match sorted array"

    def test_merge_sort_empty(self):
        arr = []
        sorted_arr = []
        merge_sort(arr)
        assert arr == sorted_arr , "arr did not match sorted array"

    def test_quick_sort_basic(self):
        arr = [1,4,8,2,7,5,6,4,5,9]
        sorted_arr = [1,2,4,4,5,5,6,7,8,9]
        quick_sort(arr,0,len(arr)-1)
        assert arr == sorted_arr , "arr did not match sorted array"

    def test_quick_sort_empty(self):
        arr = []
        sorted_arr = []
        quick_sort(arr,0,len(arr)-1)
        assert arr == sorted_arr , "arr did not match sorted array"