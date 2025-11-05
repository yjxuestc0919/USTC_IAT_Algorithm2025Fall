from quick_sort import quick_sort
import time

with open("data.txt") as f:
    length = int(f.readline())
    print(length)
    nums = list(map(int, f.readline().split()))

start = time.time()
quick_sort(
    nums,
    0,
    len(nums) - 1,
    optimize="median_of_three",
    use_insert_sort=True,
    k=16,
)
end = time.time()
my_quick_sort_time = end - start


with open("sorted.txt", "w") as f:
    print(f"My Quick Sort Time: {my_quick_sort_time:.6f} seconds\n")
    f.write(" ".join(map(str, nums)) + "\n")