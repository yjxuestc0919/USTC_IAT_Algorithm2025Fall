def partition(nums, left, right):
    pivot = nums[left]
    i, j = left+1, right

    while True:
        while i <= j and nums[j] > pivot:
            j -= 1
        while i <= j and nums[i] < pivot:
            i += 1
        if i >= j: break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    nums[j], nums[left] = nums[left], nums[j]
    return j

import random
def random_partition(nums, left, right):
    pivot_index = random.randrange(left, right+1)
    nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
    pivot = nums[left]
    i, j = left+1, right

    while True:
        while i <= j and nums[j] > pivot:
            j -= 1
        while i <= j and nums[i] < pivot:
            i += 1
        if i >= j: break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    nums[j], nums[left] = nums[left], nums[j]
    return j

def medium_num(s, m, l):
    if (s <= m <= l) or (l <= m <= s):
        return m
    elif (m <= s <= l) or (l <= s <= m):
        return s
    else:
        return l

def median_of_three_partition(nums, left, right):
    mid = left + (right - left) // 2
    medium_value = medium_num(nums[left], nums[mid], nums[right])
    if medium_value == nums[mid]:
        pivot_index = mid
    elif medium_value == nums[right]:
        pivot_index = right
    else:
        pivot_index = left
    nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
    pivot = nums[left]
    i, j = left+1, right
    while True:
        while i <= j and nums[j] > pivot:
            j -= 1
        while i <= j and nums[i] < pivot:
            i += 1
        if i >= j: break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    nums[j], nums[left] = nums[left], nums[j]
    return j

def insert_sort(nums):
    for i in range(1, len(nums)):
        cur = nums[i]
        j = i-1
        while j > -1 and nums[j] > cur:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = cur

def quick_sort(
        nums, 
        left, 
        right, 
        optimize=["random_pivot", "median_of_three", None],
        use_insert_sort=False,
        k = 16):
    if use_insert_sort and right - left <= k:
        return
    if left >= right:
        return
    if optimize == "random_pivot":
        index = random_partition(nums, left, right)
    elif optimize == "median_of_three":
        index = median_of_three_partition(nums, left, right)
    else:
        index = partition(nums, left, right)
    
    quick_sort(nums, left, index-1, optimize)
    quick_sort(nums, index+1, right, optimize)

    if use_insert_sort and left == 0 and right == len(nums)-1:
        insert_sort(nums)
