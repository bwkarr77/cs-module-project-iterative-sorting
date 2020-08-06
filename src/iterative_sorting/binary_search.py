nums = [2, 6, 8, 3, 4, 1, 9, 5, 7]

def insert_sort(nums):
    # loop through 'unsorted' list
    # - can skip nums[0] because it's already 'sorted'
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i

        # NOT at the beginning, and value is NOT sorted yet
        while j > 0 and temp < nums[j-1]:
            # swap
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = temp

    return nums