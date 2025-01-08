from typing import List

"""
最大化最小值问题，想到二分解决
假设：礼盒的最大甜蜜度可以为 d
单调性：d 能满足，<d 的肯定更能满足
二分上界：max(price) - min(price)
二分下界：0
二分判断：当前数组中是否存在至少 k 个价格满足甜蜜度 d
贪心：首先可以想到排序的，排序之后对于prices[i],它之前的价格与它的差值一定是递减，离得越近差值越小
     我们可以默认prices[0]是要选择的价格，使用变量记录它和最后选择的 prices[i]的差值，当差值>=d 的时候
     这个元素是可以加入的，只要元素数量可以达到 k，证明可以行
"""

def maximumTastiness(price: List[int], k: int) -> int:
    def check(d):
        ans = 1
        pre = price[0]
        for i in range(1, len(price)):
            if price[i] - pre >= d:
                ans += 1
                pre = price[i]
        return ans >= k

    price.sort()
    l, r = 0, price[-1] - price[0] + 1
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            l = mid + 1
        else:
            r = mid
    return l - 1
