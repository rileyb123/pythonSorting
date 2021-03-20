
def counting_sort(arr):

    counts = [0 for i in range(0,10)]
   
    for i in arr:
        counts[i] += 1
    
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]

    pos = 0
    for i in range(1,len(counts)):
        while counts[i] > 0:
            arr[pos] = i
            pos += 1
            counts[i] -= 1
