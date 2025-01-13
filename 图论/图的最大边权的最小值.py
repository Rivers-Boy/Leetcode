from heapq import heappop, heappush
from math import inf
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
        单源最短路径：求 0 到其他所有节点的最短路径
                    但是这里最短路径的定义不是经过的边之和，而是经过的边里的最大值
"""


def minMaxWeight(n: int, edges: List[List[int]], threshold: int) -> int:
    if len(edges) < n - 1:
        return -1
    # 构建反图
    g = [[] for _ in range(n)]
    for x, y, w in edges:
        g[y].append((x, w))
    dis = [inf] * n
    dis[0] = 0
    h = [(0, 0)]  # (路径最大边权，节点编号)

    while h:
        d, x = heappop(h)
        if d > dis[x]:
            continue
        for y, w in g[x]:
            new_d = max(d, w)
            if new_d < dis[y]:
                dis[y] = new_d
                heappush(h, (new_d, y))
    ans = max(dis)
    return ans if ans < inf else -1
