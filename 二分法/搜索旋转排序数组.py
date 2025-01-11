from bisect import bisect_left
from typing import List

"""
法 1：同上题，先找到最小值，然后判断在哪一段，进行二次二分
法 2：一次二分能解决吗？
     我们其实主要主要写一个 check 函数，判断什么情况下 需要将 l 移动到 mid + 1 (这里选择分析将 r 移动到 mid 也是可以的)
     将 l 移动到 mid + 1，也就是说可以确定 target 在 x 右方
     x = nuns[mid]
      1. x 在左半段 (x > nums[-1])
         1. 如果此时 target 在右半段，必然满足条件
         2. 如果 target 在左半段，必须要求 target > x
      2. x 在右半段 (x <= nums[-1])
         1. 此时 target 必须在有半段 且 target > x
    转化为代码即可
"""


def search2(nums: List[int], target: int) -> int:
    # 判断target是否在x=nums[mid]右侧
    def check(x):
        # x在第一段
        if x > nums[-1]:
            return target <= nums[-1] or target > x
        # x在第二段
        return x < target <= nums[-1]

    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if check(nums[mid]):
            l = mid + 1
        else:
            r = mid
    return r if nums[r] == target else -1


def search1(nums: List[int], target: int) -> int:
    def findMin():
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                # l 左边一定比 l 小
                l = mid + 1
            else:
                # r右边可能<=r
                r = mid
        return l

    i = findMin()
    if target > nums[-1]:
        l = bisect_left(nums, target, 0, i)
        return l if nums[l] == target else -1
    l = bisect_left(nums, target, i, len(nums))
    return l if l < len(nums) and nums[l] == target else -1
