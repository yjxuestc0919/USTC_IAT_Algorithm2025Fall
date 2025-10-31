def quick_sort(nums, low, high):
    if low >= high: return

    def partition(nums, low, high):
        pivot = nums[high]
        i = low-1 # [low: i] 为所有小于 pivot 的元素

        for j in range(low, high):
            if nums[j] <= pivot: # 每一次找到比基准小的元素，就放到 [low:i] 组内
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        # 遍历完之后，把基准值放到中间。左边<pivot | 右边>pivot
        nums[high], nums[i+1] = nums[i+1], nums[high] 

        return i+1

    part_index = partition(nums, low, high)        
    quick_sort(nums, low, part_index-1)
    quick_sort(nums, part_index+1, high)


def quick_sort_optimized(nums, low, high, threshold=10):
    # 长度小于某个阈值就在后续统一采用插入排序
    if (high - low) <= threshold:
        for i in range(low + 1, high + 1):
            key = nums[i]
            j = i - 1
            while j >= low and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return
    
    def partition(nums, low, high):
        # 三数取中
        mid = (low+high) // 2
        if nums[low] > nums[mid]:
            nums[low], nums[mid] = nums[mid], nums[low]
        if nums[low] > nums[high]:
            nums[low], nums[high] = nums[high], nums[low]
        if nums[mid] > nums[high]:
            nums[mid], nums[high] = nums[high], nums[mid]
        pivot = nums[mid]

        # 聚集元素
        lt, i, gt = low, low, high # 这里 [low:lt] < pivot; [gt:high] > pivot
        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt] 
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[gt], nums[i] = nums[i], nums[gt]
                gt -= 1
            else:
                i += 1
        
        return lt, gt
    
    lt, gt = partition(nums, low, high)
    quick_sort_optimized(nums, low, lt-1)
    quick_sort_optimized(nums, gt+1, high)