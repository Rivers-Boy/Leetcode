from collections import defaultdict

"""
https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/description/
非常类似另一道滑窗题
https://leetcode.cn/problems/minimum-window-substring/description/ 最小覆盖子串
"""


def validSubstringCount(word1: str, word2: str) -> int:
    # 滑动窗口，用字典统计字母数量
    n = len(word1)
    dic = defaultdict(int)
    for c in word2:
        dic[c] += 1
    size = len(dic)

    # 找到一个最小的
    left = ans = 0
    for i, x in enumerate(word1):
        # 更新字典
        dic[x] -= 1
        if dic[x] == 0:
            size -= 1

        while size == 0:
            # 窗口如果已经包含 word2全部字符，更长的必然符合要求
            ans += n - i
            if dic[word1[left]] == 0:
                size += 1
            dic[word1[left]] += 1
            left += 1
    return ans
