from collections import defaultdict

"""
常用枚举技巧：在枚举右边的 c 和 d 的同时，用哈希表维护左边的 a / b 的个数
为什么可以直接用浮点数？
    取两个接近 1 但不相同的分数 a/a+1 和 a-1/a
    根据 IEEE 754，在使用双精度浮点数的情况下，如果这两个数的绝对差  1/a(a+1) 比 2 ** (-52)次方还小，计算机就可能会把这个两个数舍入到同一个浮点数上
    所以当 a = 2**26 的时候，可能就有问题了
    单精度的话，a = 2 ** (11.5)
"""


def numberOfSubsequences(nums: list[int]) -> int:
    n = len(nums)
    cnt = defaultdict(int)
    ans = 0
    # 枚举 c
    for i in range(4, n - 2):
        # 维护左，放入哈希表
        b = nums[i - 2]
        for a in nums[:i - 3]:
            cnt[a / b] += 1

        c = nums[i]
        # 枚举d，统计个数
        for d in nums[i + 2:]:
            ans += cnt[d / c]
    return ans
