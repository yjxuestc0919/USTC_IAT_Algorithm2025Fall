from graph_ds import build_adj_list, build_adj_matrix, bfs_adj_list, bfs_adj_matrix

# 数据集 1：邻接矩阵 + BFS
adj_matrix, index, reverse_index = build_adj_matrix("data.txt")
bfs_adj_matrix(adj_matrix, index, reverse_index, start="A")

print("-" * 50)

# 数据集 2：邻接表 + BFS + 时间
adj_list = build_adj_list("twitter_small.txt")
bfs_adj_list(adj_list)