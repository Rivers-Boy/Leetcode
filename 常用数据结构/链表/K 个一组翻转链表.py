from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # 统计节点个数
    n = 0
    cur = head
    while cur:
        cur = cur.next
        n += 1
    # 虚节点
    p0 = dummy = ListNode(next=head)
    pre = None
    cur = head
    while n >= k:
        n -= k
        for _ in range(k):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        """
        一开始疑惑这里为什么不能
            p0.next.next = cur
            p0.next = pre
            p0 = pre
        原因是下一段被反转了，p0的下一个位置应该p0.next 也就是下一段开头的第一个
        但是因为后面赋值会丢失这个 next，所以用一个变量记录一下就可以了
        """
        nxt = p0.next
        p0.next.next = cur
        p0.next = pre
        p0 = nxt
    return dummy.next
