import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from lab1.quick_sort import quick_sort, quick_sort_optimized
from sort_algorithms.bubble_sort import bubble_sort
from sort_algorithms.heap_sort import heap_sort
from sort_algorithms.insert_sort_ascend import insert_sort
from sort_algorithms.select_sort import select_sort
from sort_algorithms.merge_sort import merge_sort
import time

with open("data.txt") as f:
    length = int(f.readline())
    print(length)
    nums = list(map(int, f.readline().split()))

algorithms = {
    # "Bubble Sort": bubble_sort,
    # "Selection Sort": select_sort,
    # "Insertion Sort": insert_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
    "Quick Sort": lambda nums: quick_sort(nums, 0, len(nums) - 1),
    "Optimized Quick Sort": lambda nums: quick_sort_optimized(nums, 0, len(nums) - 1),
}

results = {}
for name, func in algorithms.items():
    nums_copy = nums[:]
    start = time.time()
    if "Quick Sort" in name:
        func(nums_copy)
    elif name == "Merge Sort":
        func(nums_copy, 0, len(nums_copy) - 1)
    else:
        nums_copy = func(nums_copy)
    end = time.time()
    print(f"{name} Time: {(end-start):.6f} seconds")