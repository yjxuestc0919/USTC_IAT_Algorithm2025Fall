import heapq, math
from collections import deque

class HuffmanTreeNode():
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    # 修改内置的 <  方便小根堆进行比较
    def __lt__(self, other):
        return self.frequency < other.frequency

def create_huffman_tree(frequency: dict):
    '''
    Create a Huffman Tree based on input frequency.
    
    Args:
        frequency: dict
    '''

    # 用小根堆来存储频率
    heap = []
    for ch, freq in frequency.items():
        heapq.heappush(heap, HuffmanTreeNode(ch, freq))
    

    while len(heap) > 1:
        # 每次从小根堆里面pop出频率最小的两个
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanTreeNode(None, node1.frequency+node2.frequency)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def generate_huffman_code(root: HuffmanTreeNode):
    '''
    Generate Huffman code based on root node

    Args:
        node: HuffmanTreeNode 
    '''
    if not root:
        return {}

    codes = {}
    queue = deque([(root, "")])

    while queue:
        node, current_code = queue.popleft()
        # 叶子节点
        if node.char:
            codes[node.char] = current_code
        if node.left:
            queue.append((node.left, current_code + "0"))
        if node.right:
            queue.append((node.right, current_code + "1"))
    return codes

def print_compress_ratio(root: HuffmanTreeNode, frequency: dict):
    # huffman code length
    huffman_length = 0
    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        if node.char:
            huffman_length += depth*node.frequency
        if node.left: queue.append((node.left, depth+1))
        if node.right: queue.append((node.right, depth+1))
    
    # 定长编码长度
    total_chars = sum(frequency.values())
    num_unique_chars = len(frequency)
    # 计算表示这么多字符至少需要几位
    fixed_bits_per_char = math.ceil(math.log2(num_unique_chars))
    fixed_total_bits = total_chars * fixed_bits_per_char
    ratio = (huffman_length / fixed_total_bits) * 100
    print(f"压缩率: {(ratio):.2f}%")
    return ratio