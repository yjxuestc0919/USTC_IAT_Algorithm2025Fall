from collections import defaultdict
from huffman_code import create_huffman_tree, generate_huffman_code, print_compress_ratio

# 读取文件的字符串，同时过滤掉所有的空格和换行
with open("orignal.txt", "r") as f:
    content = f.read()
filtered_content = ''.join(content.split())

# 统计每一个字符的频率
frequency = defaultdict(int)
for ch in filtered_content:
    frequency[ch] += 1

huffman_tree = create_huffman_tree(frequency=frequency)
codes = generate_huffman_code(huffman_tree)
ratio = print_compress_ratio(huffman_tree, frequency)

with open("table.txt", "w", encoding="utf-8") as f_out:
    f_out.write(f"{'字符':<8}\t{'出现频率':<8}\t{'编码':<8}\n")
    for ch, code in codes.items():
        freq = frequency[ch]
        f_out.write(f"{ch:<10}\t{freq:<10}\t{code:<10}\n")