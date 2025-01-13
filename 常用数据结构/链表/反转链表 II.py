from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # 需要特殊处理 left=1的情况，因为此时找不到前一个节点，所以我们设立一个哨兵节点来指向头节点
    x = dummy = ListNode(next=head)
    for _ in range(left - 1):
        x = x.next

    pre = None
    cur = x.next
    for _ in range(right - left + 1):
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    x.next.next = cur
    x.next = pre

    return dummy.next
