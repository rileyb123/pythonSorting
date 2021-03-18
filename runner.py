from bubble_sort import *


if __name__ == "__main__":
    arr = [1,4,8,2,7,5,6,4,5,9]
    sorted_arr = [1,2,4,4,5,5,6,7,8,9]
    arr = bubble_sort(arr)
    assert arr == sorted_arr , "arr was not sorted correctly, bubble sort"
    


