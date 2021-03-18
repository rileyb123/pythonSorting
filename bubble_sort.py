
# Bubble sort, done by simply bubbling smaller elements up to the top

def bubble_sort(arr):
    
    for i in range(len(arr)-1):
        for j in range(i+1 , len(arr)):
            if(arr[i] > arr[j]):
                arr[i] , arr[j] = arr[j] , arr[i]
                
    return arr