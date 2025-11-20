class RBTreeNode():
    def __init__(self, value: int, color: str, parent=None, left=None, right=None):
        if color not in ("red", "black"):
            raise ValueError("color must be 'red' or 'black'")
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value

def bstree_insert(input_node: RBTreeNode, root: RBTreeNode):
    """
    Insert the input_node into the binary search tree
    """
    if not root: return input_node
    if input_node.value < root.value:
        if not root.left:
            root.left = input_node
            input_node.parent = root
        else:
            bstree_insert(input_node, root.left)
    else:
        if not root.right:
            root.right = input_node
            input_node.parent = root
        else:
            bstree_insert(input_node, root.right)
    return root

def rotate_left(root: RBTreeNode, x: RBTreeNode):
    # 取出 x 的右孩子 y
    y = x.right

    # 把 y 的左子树β 挂到 x 的右子树上
    x.right = y.left
    if y.left is not None:
        y.left.parent = x      # β 的父亲变为 x

    # 让 y 替代 x 的位置：y 的父亲变为 x 的父亲
    y.parent = x.parent

    # 如果 x 原来是根，则现在 y 成为新的根
    if x.parent is None:
        root = y
    # 否则根据 x 在父亲的左右位置，挂上 y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    # 让 x 成为 y 的左孩子
    y.left = x
    x.parent = y

    return root

def rotate_right(root: RBTreeNode, y: RBTreeNode):
    x = y.left
    y.left = x.right
    if x.right is not None:
        x.right.parent = y

    x.parent = y.parent

    if y.parent is None:
        root = x
    elif y == y.parent.right:
        y.parent.right = x
    else:
        y.parent.left = x

    x.right = y
    y.parent = x

    return root

def rbtree_fix_up(input_node: RBTreeNode, root: RBTreeNode):
    while input_node.parent is not None and input_node.parent.color == "red":

        # Case 1~3：父亲是祖父的左孩子
        if input_node.parent == input_node.parent.parent.left:
            y = input_node.parent.parent.right   # 叔叔

            # Case 1：叔叔是红色 → 父叔变黑，爷爷变红，上移
            if y is not None and y.color == "red":
                print("Case 1")
                input_node.parent.color = "black"
                y.color = "black"
                input_node.parent.parent.color = "red"
                input_node = input_node.parent.parent

            else:
                # Case 2：内侧（父左子右）→ 先左旋父亲
                if input_node == input_node.parent.right:
                    print("Case 2")
                    input_node = input_node.parent
                    root = rotate_left(root, input_node)

                # Case 3：外侧（父左子左）→ 父变黑，爷变红，对爷爷右旋
                print("Case 3")
                input_node.parent.color = "black"
                input_node.parent.parent.color = "red"
                root = rotate_right(root, input_node.parent.parent)


        # Case 4~6：父亲是祖父的右孩子（完全对称）
        else:
            y = input_node.parent.parent.left   # 叔叔

            # Case 4：叔叔是红色
            if y is not None and y.color == "red":
                print("Case 4")
                input_node.parent.color = "black"
                y.color = "black"
                input_node.parent.parent.color = "red"
                input_node = input_node.parent.parent

            else:
                # Case 5：内侧（父右子左）
                if input_node == input_node.parent.left:
                    print("Case 5")
                    input_node = input_node.parent
                    root = rotate_right(root, input_node)

                # Case 6：外侧（父右子右）
                print("Case 6")
                input_node.parent.color = "black"
                input_node.parent.parent.color = "red"
                root = rotate_left(root, input_node.parent.parent)

    # 根必须为黑色
    root.color = "black"
    return root

def rbtree_insert(input_node: RBTreeNode, root: RBTreeNode):
    root = bstree_insert(input_node, root)
    input_node.color = "red"
    root = rbtree_fix_up(input_node, root)
    root.color = "black"
    return root