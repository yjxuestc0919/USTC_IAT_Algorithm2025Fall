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

min_pair = None
min_distance = float("inf")

start_time = time.time()
# 暴力检索
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        xi, yi = data[i][1], data[i][2]
        xj, yj = data[j][1], data[j][2]
        distance = ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5

        if distance < min_distance:
            min_distance = distance
            min_pair = (data[i][0], data[j][0])
end_time = time.time()
elapsed_time = (end_time - start_time) 

print(f"{min_pair[0]} {data[min_pair[0]][1]} {data[min_pair[0]][2]}")
print(f"{min_pair[1]} {data[min_pair[1]][1]} {data[min_pair[1]][2]}")
print(f"Time taken: {elapsed_time:.3f} s")