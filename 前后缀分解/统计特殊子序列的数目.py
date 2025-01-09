from collections import defaultdict
from math import gcd

"""
思维转换：将 a * c = b * d 变为 a / b = d / c 这样 abcd 就是顺序的了，这样 a 和 b 都在 c 和 d 的左边，从而方便用前后缀分解解决。
1. 统计数对 (c,d) 的最简分数的个数，记录到哈希表 dic 中
    最简分数：分子和分母互质的分数。如果分子和分母不互质，可以除以二者的最大公约数（GCD）。比如分数 4/6，分子和分母都除以二者的最大公约数 2，得到最简分数 2/3
2. 枚举 b 以及左边的 a，计算最简分数 a / b,从哈希表中查找后加到答案里
3. 在枚举了 b 之后，c 作为 b+2的位置已经不能用了，不然会重复统计，所以需要去掉
"""


def numberOfSubsequences(nums: list[int]) -> int:
    n = len(nums)
    dic = defaultdict(int)
    # 枚举 d/c的最简分数
    for i in range(4, n - 2):
        c = nums[i]
        # 枚举d
        for d in nums[i + 2:]:
            g = gcd(c, d)
            dic[d // g, c // g] += 1

    ans = 0

    # 枚举b
    for i in range(2, n - 4):
        b = nums[i]
        # 枚举a
        for a in nums[:i - 1]:
            g = gcd(a, b)
            ans += dic[a // g, b // g]
        # 撤销之前统计的 d'/c'
        c = nums[i + 2]
        for d in nums[i + 4:]:
            g = gcd(c, d)
            dic[d // g, c // g] -= 1
    return ans
