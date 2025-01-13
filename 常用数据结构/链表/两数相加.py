from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers2(l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
    # 递归版本
    # 递归边界
    if not l1 and not l2:
        return ListNode(carry) if carry else None
    if not l1:
        l1, l2 = l2, l1
    s = carry + l1.val + (l2.val if l2 else 0)
    l1.val = s % 10
    l1.next = addTwoNumbers2(l1.next, l2.next if l2 else None, s // 10)
    return l1


def addTwoNumbers1(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # 迭代版本，只可以直接用一个变量来处理位置
    cur = dummy = ListNode(-1)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next

        if l2:
            carry += l2.val
            l2 = l2.next

        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10

    return dummy.next



