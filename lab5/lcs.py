def lcs_full(s1: str, s2: str):
    l1, l2 = len(s1), len(s2)
    dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    i, j = l1, l2
    lcs = []
    while i>0 and j>0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i][j-1] >= dp[i-1][j]:
            j -= 1
        else:
            i -= 1

    return ''.join(reversed(lcs)), dp[l1][l2]

def lcs_two_rows(s1: str, s2: str):
    # 确保 s2 是较短的字符串，节省空间
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    l1, l2 = len(s1), len(s2)
    prev, cur = [0] * (l2 + 1), [0] * (l2 + 1)

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        # 当前行成为下一轮的“上一行”
        prev, cur = cur, [0] * (l2 + 1)

    return prev[l2]

def lcs_one_row(s1: str, s2: str):
    # 确保 s2 是较短的字符串，节省空间
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    l1, l2 = len(s1), len(s2)
    dp = [0] * (l2 + 1)

    for i in range(1, l1 + 1):
        pre = 0  # 用来保存“左上角” dp[i-1][j-1] 的值
        for j in range(1, l2 + 1):
            tmp = dp[j]  # 暂存当前 dp[j]（它是“上方”）
            if s1[i - 1] == s2[j - 1]:
                dp[j] = pre + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            pre = tmp  # 更新 pre，供下一个 j 使用
    return dp[l2]