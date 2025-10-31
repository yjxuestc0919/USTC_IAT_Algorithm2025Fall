import heapq

def heap_sort(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    return [heapq.heappop(heap) for _ in range(len(heap))]