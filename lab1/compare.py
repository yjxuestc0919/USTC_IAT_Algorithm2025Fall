import random
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from lab1.quick_sort import quick_sort
from sort_algorithms.bubble_sort import bubble_sort
from sort_algorithms.heap_sort import heap_sort
from sort_algorithms.insert_sort_ascend import insert_sort
from sort_algorithms.select_sort import select_sort
from sort_algorithms.merge_sort import merge_sort

DATA_PATH = Path(__file__).parent / "data.txt"

with open(DATA_PATH) as f:
    length = int(f.readline())
    print(length)
    nums = list(map(int, f.readline().split()))

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": select_sort,
    "Insertion Sort": insert_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
    # "Sort Algorithm in raw python": lambda arr: sorted(arr),
    "Quick Sort": lambda arr: quick_sort(arr, 0, len(arr) - 1),
}

SECONDS_ONLY = {"Bubble Sort", "Selection Sort", "Insertion Sort"}

for name, func in algorithms.items():
    nums_copy = nums[:]
    start = time.perf_counter()
    if name == "Quick Sort":
        func(nums_copy)
    elif name == "Merge Sort":
        func(nums_copy, 0, len(nums_copy) - 1)
    else:
        nums_copy = func(nums_copy)
    elapsed = time.perf_counter() - start
    if name in SECONDS_ONLY:
        print(f"{name} Time: {elapsed:.6f} seconds")
    else:
        print(f"{name} Time: {elapsed * 1000:.3f} ms")

print()
print("Quick Sort Pivot/Insertion Comparison")

reference_sorted = sorted(nums)

pivot_strategies = {
    "fixed": None,
    "random": "random_pivot",
    "median_of_three": "median_of_three",
}

insertion_options = {
    "without_insertion": False,
    "with_insertion": True,
}

results = []

for pivot_name, optimize in pivot_strategies.items():
    for insertion_name, use_insert in insertion_options.items():
        nums_copy = nums[:]
        if optimize == "random_pivot":
            random.seed(0)
        start = time.perf_counter()
        quick_sort(
            nums_copy,
            0,
            len(nums_copy) - 1,
            optimize=optimize,
            use_insert_sort=use_insert,
        )
        elapsed = time.perf_counter() - start
        is_sorted = nums_copy == reference_sorted
        results.append(
            {
                "pivot": pivot_name,
                "insertion": insertion_name,
                "time": elapsed,
                "sorted": is_sorted,
            }
        )

header = (
    f"{'Pivot Strategy':<18}"
    f"{'Insertion Sort':<20}"
    f"{'Time (s)':>12}"
    f"{'  Status'}"
)
print(header)
print("-" * len(header))
for result in results:
    status = "OK" if result["sorted"] else "FAIL"
    print(
        f"{result['pivot']:<18}"
        f"{result['insertion']:<20}"
        f"{result['time']:>12.6f}  {status}"
    )
