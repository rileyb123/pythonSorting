import heapq

#heap sort, very simple. Using a min heap repeatedly pop off te top of the 
# heap for all values, this returns the sorted array in nlogn

def heap_sort(arr):
    
    heapq.heapify(arr)

    return [heapq.heappop(arr) for i in range(len(arr))]

    