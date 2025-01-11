from typing import List

"""
问题：和 I 一样，但是当 nums[mid] = nums[r]的时候，没法判断是在边还是右边
这里有两种处理方法：
    1. 我们直接将 l 移动到不和结尾相等就可以了
    2. 在相等时，每次舍去 r 处的数
        如果 nums[r]是最小值，那么 nums[mid]也是最小值，还在二分范围内，不影响
        如果 nums[r]不是最小值，那么我们舍去了一个错误答案
"""

def findMin2(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        elif nums[mid] < nums[r]:
            r = mid
        else:
            r -= 1
    return nums[l]


def findMin1(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while nums[l] == nums[-1] and l < r:
        l += 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return nums[l]
