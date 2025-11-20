from rbtree_insert import RBTreeNode, rbtree_insert
from collections import deque
from typing import TextIO

def preorder(node: RBTreeNode, fh: TextIO):
    if not node:
        return
    fh.write(f"({node.value}, {node.color})\n")
    preorder(node.left, fh)
    preorder(node.right, fh)

def inorder(node: RBTreeNode, fh: TextIO):
    if not node:
        return
    inorder(node.left, fh)
    fh.write(f"({node.value}, {node.color})\n")
    inorder(node.right, fh)

def levelorder(node: RBTreeNode, fh: TextIO):
    if not node:
        return
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        fh.write(f"({cur.value}, {cur.color})\n")
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)

data = []
with open("insert.txt", "r") as f:
    # 第一行为节点总数，第二行为需要插入的数值
    n = int(f.readline().strip())
    parts = f.readline().strip().split()
    for part in parts:
        node = RBTreeNode(int(part), color="red")
        data.append(node)

root = None
for node in data:
    root = rbtree_insert(node, root)

if root:
    with open("NLR.txt", "w") as f:
        preorder(root, f)
    with open("LNR.txt", "w") as f:
        inorder(root, f)
    with open("LOT.txt", "w") as f:
        levelorder(root, f)
