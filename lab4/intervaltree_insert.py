class IntervalNode:
    def __init__(self, low: int, high: int, color: str, parent=None, left=None, right=None):
        # 区间的左端点和右端点
        self.low = low
        self.high = high
        # 该节点子树中“所有区间右端点”的最大值
        self.max = high
        # 红黑树颜色，只能是 'red' 或 'black'
        if color not in ("red", "black"):
            raise ValueError("color must be 'red' or 'black'")
        self.color = color

        # 父、左、右节点指针
        self.parent = parent
        self.left = left
        self.right = right


# 更新节点的 max 值
def update_max(node):
    if node:
        node.max = max(
            node.high,
            node.left.max if node.left else float('-inf'),
            node.right.max if node.right else float('-inf')
        )

def bstree_insert(input_node: IntervalNode, root: IntervalNode):
    if not root:
        return input_node  # 空树，直接作为根节点

    # 比较插入节点的 low 值
    if input_node.low < root.low:
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

    # 插入完成后更新当前节点的 max 值
    update_max(root)
    return root

def rotate_left(root: IntervalNode, x: IntervalNode):
    # 左旋：让 x 的右孩子 y 替代 x 的位置
    y = x.right
    x.right = y.left
    if y.left:
        y.left.parent = x
    y.parent = x.parent

    if x.parent is None:  # x 是根
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y

    # 旋转后更新 max 值
    update_max(x)
    update_max(y)
    return root


def rotate_right(root: IntervalNode, y: IntervalNode):
    # 右旋：让 y 的左孩子 x 替代 y 的位置
    x = y.left
    y.left = x.right
    if x.right:
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

    update_max(y)
    update_max(x)
    return root

def rbtree_fix_up(input_node: IntervalNode, root: IntervalNode):
    while input_node.parent and input_node.parent.color == "red":
        # 父节点是祖父的左孩子
        if input_node.parent == input_node.parent.parent.left:
            y = input_node.parent.parent.right  # 叔叔节点
            if y and y.color == "red":  # Case 1：叔叔是红色
                input_node.parent.color = "black"
                y.color = "black"
                input_node.parent.parent.color = "red"
                input_node = input_node.parent.parent
            else:
                if input_node == input_node.parent.right:  # Case 2：内侧
                    input_node = input_node.parent
                    root = rotate_left(root, input_node)
                # Case 3：外侧
                input_node.parent.color = "black"
                input_node.parent.parent.color = "red"
                root = rotate_right(root, input_node.parent.parent)
        else:
            # 父节点是祖父的右孩子（对称情况）
            y = input_node.parent.parent.left
            if y and y.color == "red":  # Case 4：叔叔是红色
                input_node.parent.color = "black"
                y.color = "black"
                input_node.parent.parent.color = "red"
                input_node = input_node.parent.parent
            else:
                if input_node == input_node.parent.left:  # Case 5：内侧
                    input_node = input_node.parent
                    root = rotate_right(root, input_node)
                # Case 6：外侧
                input_node.parent.color = "black"
                input_node.parent.parent.color = "red"
                root = rotate_left(root, input_node.parent.parent)

    # 根节点必须为黑色
    root.color = "black"
    return root

def rbtree_insert(input_node: IntervalNode, root: IntervalNode):
    # 先按 BST 规则插入
    root = bstree_insert(input_node, root)
    input_node.color = "red"
    # 再进行红黑树修正
    root = rbtree_fix_up(input_node, root)
    # 插入完成后更新 max
    update_max(root)
    root.color = "black"
    return root

def overlap(a_low, a_high, b_low, b_high):
    """判断两个区间是否重叠"""
    return a_low <= b_high and b_low <= a_high


def interval_search(root: IntervalNode, query_low: int, query_high: int):
    """在区间树中查找与 [query_low, query_high] 重叠的所有区间"""
    if root is None:
        return []

    result = []

    # 当前节点的区间是否重叠
    if overlap(root.low, root.high, query_low, query_high):
        result.append((root.low, root.high))

    # 如果左子树的 max 值 >= query_low，则左子树可能有重叠
    if root.left and root.left.max >= query_low:
        result += interval_search(root.left, query_low, query_high)

    # 如果右子树的 low <= query_high，则右子树可能有重叠
    if root.right and root.low <= query_high:
        result += interval_search(root.right, query_low, query_high)

    return result
