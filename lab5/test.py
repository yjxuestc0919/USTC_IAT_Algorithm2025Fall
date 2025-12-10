from lcs import lcs_full, lcs_two_rows, lcs_one_row

def main():
    text1 = input("请输入第一个字符串：").strip()
    text2 = input("请输入第二个字符串：").strip()

    print("\n==== LCS 测试结果 ====")

    seq, length = lcs_full(text1, text2)
    print(f"[O(mn)] 完整DP法 -> 长度: {length}, 序列: {seq if length > 0 else '无公共子序列'}")

    length2 = lcs_two_rows(text1, text2)
    print(f"[O(2n)] 两行滚动数组法 -> 长度: {length2}")

    length3 = lcs_one_row(text1, text2)
    print(f"[O(n)] 一维数组优化法 -> 长度: {length3}")

if __name__ == "__main__":
    main()
