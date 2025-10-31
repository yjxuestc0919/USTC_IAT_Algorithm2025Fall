def insert_sort(nums: list[int]) -> list[int]:
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j > -1 and nums[j] < key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    
    return nums