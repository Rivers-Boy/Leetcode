from typing import List

"""
找到一个最大的必然可以 - 如何思路下推
    单调性：如果当前的值<下一个值，一定在右半部分有答案
    二分下界：0
    二分上界：len(nums)
    左闭右开区间 的定义要求区间的右边界不包括在内，
    因此设置 right = len(nums) - 1 是合适的，因为这确保了区间 [left, right] 是合法的，并且在计算中点时可以正常访问数组中的元素。
"""


def findPeakElement(nums: List[int]) -> int:
    # 初始化为n-1的原因是如果数组时递增的，那么一定会找到最后一个数，初始化为n时可能会越界
    # 第二个原因：nums[n-1]要不就是顶峰，要不就在顶峰的右侧，所以可以直接染成蓝色
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= nums[mid+1]:
            # 说明峰值在左半部分（包括mid）
            r = mid
        else:
            # 说明峰值在右半部分
            l = mid + 1
    return l