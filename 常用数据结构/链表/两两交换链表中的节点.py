from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs3(head: Optional[ListNode]) -> Optional[ListNode]:
    # 递归写法
    if not head or not head.next:
        return head  # 不足两个节点

    p1 = head
    p2 = head.next
    p3 = p1.next.next

    p1.next = swapPairs3(p3)
    # 交换之后 p2 才是第一个点
    p2.next = p1
    return p2


def swapPairs2(head: Optional[ListNode]) -> Optional[ListNode]:
    # 其中一个临时变量是没必要的，直接 next 表示，但是看起来有些繁琐
    pre = dummy = ListNode(next=head)
    cur = head
    while cur and cur.next:
        tmp = cur.next.next
        pre.next = cur.next
        cur.next.next = cur
        cur.next = tmp

        pre = cur
        cur = tmp
    return dummy.next


def swapPairs1(head: Optional[ListNode]) -> Optional[ListNode]:
    # 简洁做法：将后两个都使用临时变量表示，然后交换位置
    p0 = dummy = ListNode(next=head)
    p1 = head
    while p1 and p1.next:
        p2 = p1.next
        p3 = p1.next.next

        p0.next = p2
        p2.next = p1
        p1.next = p3

        p0 = p1
        p1 = p3
    return dummy.next
