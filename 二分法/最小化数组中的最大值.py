from typing import List

"""
https://leetcode.cn/problems/minimize-maximum-of-array/description/
题意：最小化最大值，应该会想到二分
        假设：设最小化最大值为 mx
        二分下界：0， 即不操作完成
        二分上界：max(nums) 如果超出了这个值，我们可以不操作来维持最大值
        二分判断：这个是这道题比较难想到的地方，题目的过程其实可以看成是木桶舀水，每一次操作都是将后面一个木桶的水舀到前一个木桶
                所以我们应该从后往前舀水，让每个桶都<=mx，最后取判断 nums[0]与 mx 的关系
"""


def minimizeArrayValue(nums: List[int]) -> int:
    def check(limit):
        extra = 0
        for i in range(len(nums) - 1, 0, -1):
            # 是否多余，即下一个该加的
            extra = max(nums[i] + extra - limit, 0)
        return nums[0] + extra <= limit

    l, r = 0, max(nums) + 1
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1
    # 这里 l 和 r 应该停在了同一个位置，随便返回一个都行
    return l
