# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for n in range(smallest_index + 1, len(arr)):
            if arr[cur_index] > arr[n]:
                cur_index = n

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    print('arr: ', arr)
    # Your code here



    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    print('max: ', maximum, ', arr: ', arr)

    if maximum is None:
        max_val = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > max_val:
                max_val = arr[i]
    else:
        max_val = maximum

    # Take the max_val from above, and increase by 1
    max_val = max_val + 1
    # create an array of zeros, with length of max_val
    # => [0, 0, ..., 0]
    counts = [0] * max_val

    for a in arr:
        # print('for loop: ', a, counts)
        counts[a] += 1
        if a < 0:
            return "Error, negative numbers not allowed in Count Sort"

    c = 0
    # loop through 0 through max_val
    for i, count in enumerate(counts):
        counts[i] = c
        c += count
        # print('for loop: ', i, count, counts)

    # Output list to be filled in
    sorted_list = [None] * len(arr)

    # Iterate through input list
    for item in arr:
        # place item into the sorted list
        sorted_list[counts[item]] = item

        counts[item] += 1

    # print('sorted list: ', sorted_list)
    return sorted_list

