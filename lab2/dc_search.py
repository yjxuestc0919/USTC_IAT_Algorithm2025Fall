import time
data = []

with open("data.txt", "r") as f:
    for line in f:
        parts = line.strip().split()

        index = int(parts[0])
        x = float(parts[1])
        y = float(parts[2])
        data.append((index, x, y))
print(f"Total points: {len(data)}")

def get_distance(p1, p2):
    '''
    p1, p2: (index, x, y)
    '''
    return ((p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2) ** 0.5

Px = sorted(data, key=lambda point: point[1])
Py = sorted(data, key=lambda point: point[2])

def closest_pair_rec(Px, Py):
    '''
    Px, Py: List[tuple]
    '''
    # 递归到底情况
    if len(Px) <= 3:
        min_distance = float("inf")
        min_pair = None
        for i in range(len(Px)):
            for j in range(i+1, len(Px)):
                cur_distance = get_distance(Px[i], Px[j])
                if cur_distance < min_distance:
                    min_distance = cur_distance
                    min_pair = (Px[i], Px[j])
        return min_distance, min_pair

    min_distance, min_pair = float("inf"), None
    mid = len(Px) // 2
    Lx = Px[:mid]
    Rx = Px[mid:]
    mid_x = Px[mid]

    Ly = [pair for pair in Py if pair[1] <= mid_x[1]]
    Ry = [pair for pair in Py if pair[1] > mid_x[1]]

    # 递归的处理左右两边的情况
    d_left, left_pair = closest_pair_rec(Lx, Ly)
    d_right, right_pair = closest_pair_rec(Rx, Ry)

    if d_left < d_right:
        min_distance = d_left
        min_pair = left_pair
    else:
        min_distance = d_right
        min_pair = right_pair
    
    # Strip之间的情况
    strip_points = [p for p in Py if abs(p[1] - mid_x[1]) < min_distance]

    # 最多检查7个点
    for i in range(len(strip_points)):
        for j in range(i+1, min(i+8, len(strip_points))):
            cur_distance = get_distance(strip_points[i], strip_points[j])
            if cur_distance < min_distance:
                min_distance = cur_distance
                min_pair = (strip_points[i], strip_points[j])
    return min_distance, min_pair

start_time = time.time()
min_distance, min_pair = closest_pair_rec(Px, Py)
end_time = time.time()
elapsed_time = (end_time - start_time) 
print(f"{min_pair[0][0]} {min_pair[0][1]} {min_pair[0][2]}")
print(f"{min_pair[1][0]} {min_pair[1][1]} {min_pair[1][2]}")
print(f"Time taken: {elapsed_time:.3f} s")