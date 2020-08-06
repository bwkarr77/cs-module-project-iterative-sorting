def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        # print('linear search: ', arr[i], target)
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # print('binary search: ', arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # not found
