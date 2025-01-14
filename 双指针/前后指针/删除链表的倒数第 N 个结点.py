from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
1. 可以直接遍历整个链表达到链表长度，然后就可以计算出倒数第 N 个节点是正数的第几个，删除即可
2. 前后指针：先让 fast 走 n 步，然后前后指针一起走，这样 fast 为 null 的时候，slow 应该正好是要删除的位置
3. 注意可能会删除掉头节点，需要设置虚节点
"""


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow = fast = dummy = ListNode(next=head)
    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    if slow.next:
        slow.next = slow.next.next
    return dummy.next
