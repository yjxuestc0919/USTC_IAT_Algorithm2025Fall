from intervaltree_insert import IntervalNode, rbtree_insert, interval_search

with open("insert.txt", "r") as f:
    n = int(f.readline().strip())
    root = None
    for _ in range(n):
        low, high = map(int, f.readline().strip().split())
        new_node = IntervalNode(low, high, color="red")
        if root is None:
            new_node.color = "black"  # 根节点为黑色
            root = new_node
        else:
            root = rbtree_insert(new_node, root)

# 从控制台接受查询区间
q_low, q_high = map(int, input("Enter query interval (low high): ").strip().split())
results = interval_search(root, q_low, q_high)
print("Overlapping intervals:")
for low, high in results:
    print(f"[{low}, {high}]")  
