def merge(nums: list[int], p: int, q: int, r: int):
    """
    合并 nums[p...q] 和 nums[q+1...r]，这两个子数组都已经排好序
    """
    n1 = q - p + 1
    n2 = r - q

    # 创建临时数组
    L = [nums[p + i] for i in range(n1)]
    R = [nums[q + 1 + j] for j in range(n2)]

    i = j = 0
    k = p

    # 合并两个有序子数组
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1

    # 复制剩余元素
    while i < n1:
        nums[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        nums[k] = R[j]
        j += 1
        k += 1


def merge_sort(nums: list[int], p: int, r: int):
    """
    归并排序
    """
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(nums, p, q)
    merge_sort(nums, q + 1, r)
    merge(nums, p, q, r)
