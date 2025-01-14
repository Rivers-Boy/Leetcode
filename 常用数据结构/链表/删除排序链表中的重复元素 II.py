# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = dummy = ListNode(next=head)

    while cur.next and cur.next.next:
        x = cur.next.val
        if cur.next.next.val == x:
            # 后面只要是=x的通通跳过，指向下一个，在!=x的时候就自动退出了
            while cur.next and cur.next.val == x:
                cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next