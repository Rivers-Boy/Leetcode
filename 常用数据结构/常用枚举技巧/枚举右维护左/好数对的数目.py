from collections import defaultdict
from typing import List

"""
经典枚举右维护左
枚举 nums[j]，同时用哈希表 dic 维护 nums[j] 左边的每个数的出现次数。
"""


def numIdenticalPairs(nums: List[int]) -> int:
    dic = defaultdict(int)
    ans = 0
    for x in nums:
        ans += dic[x]
        dic[x] += 1
    return ans
