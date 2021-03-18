
# Insertion Sort, for each element we move/insert it into the correct position
# this is done by moving larger elements up to be able to insert our smaller element

def insertion_sort(arr):

    for i in range(len(arr)-1):
            
        current = arr[i]

        prev = i-1

        while prev >= 0 and current < arr[prev]:
            arr[prev+1] = arr[prev]
            prev -= 1
        arr[prev+1] = current

    

        
