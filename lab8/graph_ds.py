from collections import deque
import time

# 构造邻接矩阵
def build_adj_matrix(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    vertices = lines[0].split(",")
    n = len(vertices)

    index = {v: i for i, v in enumerate(vertices)}
    reverse_index = {i: v for i, v in enumerate(vertices)}

    adj_matrix = [[0] * n for _ in range(n)]

    for line in lines[1:]:
        u, v = line.split("-")
        i, j = index[u], index[v]
        adj_matrix[i][j] = 1
        adj_matrix[j][i] = 1 

    return adj_matrix, index, reverse_index

# 邻接矩阵 BFS
def bfs_adj_matrix(adj_matrix, index, reverse_index, start):
    n = len(adj_matrix)
    queue = deque([start])
    visited = set([start])

    print("Adjacency Matrix BFS traversal:")

    while queue:
        node = queue.popleft()
        print("Visit node:", node)

        cur_i = index[node]
        for j in range(n):
            neighbor = reverse_index[j]
            if adj_matrix[cur_i][j] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 构造邻接表
def build_adj_list(filename):
    adj = {}

    with open(filename, "r") as f:
        for line in f:
            if not line.strip():
                continue

            u, v = map(int, line.split())

            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []

            adj[u].append(v) 

    return adj

# 邻接表 BFS
def bfs_adj_list(adj):
    start_node = next(iter(adj))
    queue = deque([start_node])
    visited = set([start_node])

    start_time = time.time()

    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    end_time = time.time()

    print("Adjacency List BFS time:", end_time - start_time, "seconds")
    print("Visited nodes:", len(visited))

# 针对 u,v 形式数据构造邻接表（有向图）
def build_directed_adj_list(filename):
    adj = {}

    with open(filename, "r") as f:
        for line in f:
            if not line.strip():
                continue

            u, v = map(int, line.strip().split(","))

            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []   # 确保 v 也作为一个节点存在

            adj[u].append(v)   # 有向边 u -> v

    return adj

# 针对 CSV 邻接表的 BFS
def bfs_directed_adj_list(adj, start_node=None):
    if start_node is None:
        start_node = next(iter(adj))  # 默认选第一个节点

    queue = deque([start_node])
    visited = set([start_node])

    start_time = time.time()

    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    end_time = time.time()

    print("CSV Adjacency List BFS time:", end_time - start_time, "seconds")
    print("Visited nodes:", len(visited))