from typing import List

"""
    反向思维：从所有节点判断是否可以到达 0 ❌
            从 0 开始判断是否可以到达其他节点 ✅
    无用条件：如果 0 可以达到其他节点，代表每条边的出度至少为 1，threshold必然满足
    求最大最小值：
        1. 二分：
            假设：设最大边权的最小值为 x
            单调性：如果 x 满足条件，则>x 必然满足条件
            二分上界：最长的边
            二分下界：0 或者最短的边
        2. dijkstra
"""


def minMaxWeight(n: int, edges: List[List[int]], threshold: int) -> int:
    if len(edges) < n - 1:
        return -1
    # 构建反图
    g = [[] for _ in range(n)]
    for x, y, w in edges:
        g[y].append((x, w))
    # 记录访问
    vis = [0] * n

    # 判断所有节点与 0 的连通性
    def check(upper):
        # 从 0 出发可以达到多少点
        def dfs(x):
            vis[x] = upper
            cnt = 1
            for y, w in g[x]:
                if w <= upper and vis[y] != upper:
                    cnt += dfs(y)
            return cnt

        return dfs(0) == n

    # 二分
    mx = max(x[2] for x in edges)
    l, r = 0, mx + 1

    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return -1 if l > mx else l
