from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    #
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow is fast:
            # 这里说明存在环，同时可以从头开始了
            fast = head
            while fast is not head:
                if fast is slow:
                    return fast
                fast = fast.next
                slow = slow.next
    return None
