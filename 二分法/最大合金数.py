"""
https://leetcode.cn/problems/maximum-number-of-alloys/description/
"""
from typing import List


def maxNumberOfAlloys(n: int, k: int, budget: int, composition: List[List[int]], stock: List[int],
                      cost: List[int]) -> int:
    """
    题意：每台机器在budget限制下最多能制造多少合金，取最大的即可
    假设法：假设可以制造 num 台，那么 num + 1台肯定超钱，而且 num-1必然也可以制造出来，所以 num 和 budget 应该是有一个单调性的
    算法：遍历每台机器，对每一台机器能制造的合金数 num 进行二分
    二分上界：min(stock) + budget 假设每个都只需要一份的情况，当然嫌麻烦直接取 10 ** 9 也不是不行
    二分下界：0
    二分条件：计算每个 num 对应的钱数，判断是否超预算即可
    """
    ans = 0
    mx = min(stock) + budget  # 最多可以制造这么多份

    # 遍历每台机器
    for comp in composition:
        def check(num):
            money = 0
            for s, base, c in zip(stock, comp, cost):
                if s < base * num:
                    money += (base * num - s) * c
                    if money > budget:
                        return False
            return True

        # 左闭右开:最后l 和 r 应该停在了同一个地方，左边就是答案
        l, r = 0, mx + 1
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        ans = max(ans, l - 1)
    return ans
