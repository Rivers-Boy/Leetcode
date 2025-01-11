from typing import List

"""
和寻找峰值是类似的，这里可以说是寻找低谷
    二分单调性：如果 nums[i]>nums[i+1],说明在上升段，答案在左边，否则在右边
    二分下界：0
    二分上界：len(nums)-1
    这里和上一道题是相似的，最后一个数要么是最小的数，要么一定在最小的数右侧，所以右开区间取 n-1
"""


def findMin(nums: List[int]) -> int:
    n = len(nums)
    l, r = 0, n - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            # l 左边一定比 l 小
            l = mid + 1
        else:
            # r右边可能<=r
            r = mid
    return nums[l]
