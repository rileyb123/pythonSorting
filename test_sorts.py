from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from counting_sort import counting_sort
from heap_sort import heap_sort

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

    def test_counting_sort_basic(self):
        arr = [1,4,8,2,7,5,6,4,5,9]
        sorted_arr = [1,2,4,4,5,5,6,7,8,9]
        counting_sort(arr)
        assert arr == sorted_arr , "arr did not match sorted array"

    def test_counting_sort_empty(self):
        arr = []
        sorted_arr = []
        counting_sort(arr)
        assert arr == sorted_arr , "arr did not match sorted array"

    def test_heap_sort_basic(self):
        arr = [1,4,8,2,7,5,6,4,5,9]
        sorted_arr = [1,2,4,4,5,5,6,7,8,9]
        assert heap_sort(arr) == sorted_arr , "arr did not match sorted array"

    def test_heap_sort_empty(self):
        arr = []
        sorted_arr = []
        heap_sort(arr)
        assert heap_sort(arr) == sorted_arr , "arr did not match sorted array"