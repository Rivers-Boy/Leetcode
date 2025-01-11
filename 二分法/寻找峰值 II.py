from typing import List

"""
利用行最大值判断峰顶位置
https://leetcode.cn/problems/find-a-peak-element-ii/solutions/2571587/tu-jie-li-yong-xing-zui-da-zhi-pan-duan-r4e0n/
如果在 [0,m−1] 中二分，还需要额外判断 i+1 是否越界。在 [0,m−2] 中二分可以避免越界判断。
"""


def findPeakGrid(mat: List[List[int]]) -> List[int]:
    m, n = len(mat), len(mat[0])

    l, r = 0, m - 1
    while l < r:
        mid = (l + r) // 2
        idx, mx = max(enumerate(mat[mid]), key=lambda x: x[1])
        if mx < mat[mid + 1][idx]:
            l = mid + 1
        else:
            r = mid
    return [l, max(range(n), key=lambda i: mat[l][i])]
