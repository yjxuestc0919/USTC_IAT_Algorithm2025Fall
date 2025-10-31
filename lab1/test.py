from quick_sort import quick_sort, quick_sort_optimized
import time

with open("data.txt") as f:
    length = int(f.readline())
    print(length)
    nums = list(map(int, f.readline().split()))

nums_normal = nums[:]
nums_optimized = nums[:]

start = time.time()
quick_sort_optimized(nums_optimized, 0, len(nums_normal) - 1)
end = time.time()
optimized_time = end - start

start = time.time()
quick_sort(nums_normal, 0, len(nums_normal) - 1)
end = time.time()
normal_time = end - start


assert nums_normal == nums_optimized, "❌ 排序结果不一致！"

with open("sorted.txt", "w") as f:
    print(f"Normal Quick Sort Time: {normal_time:.6f} seconds\n")
    print(f"Optimized Quick Sort Time: {optimized_time:.6f} seconds\n")
    f.write(" ".join(map(str, nums_normal)) + "\n")