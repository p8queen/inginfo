# algo sort bubble

# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent 
#  elements if they are in wrong order.
# pass n times, each time the largest element will 
# be placed at the end of the array
# time complexity O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

a = [64, 34, 25, 12, 90, 11, 22]
print('unsorted', a)
print('sorted', bubble_sort(a))

# quick sort algorithm
# time complexity O(nlogn)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2] # select the middle element as pivot
    left = []
    right = []
    middle = []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            middle.append(i)
    
    return quick_sort(left) + middle + quick_sort(right)

a = [64, 34, 25, 12, 90, 11, 22]
print('unsorted', a)
print('sorted', quick_sort(a))
