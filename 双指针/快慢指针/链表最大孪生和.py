from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def pairSum(self, head: Optional[ListNode]) -> int:
        # 快慢指针找中点，然后反转，之后比较
        mid = self.findMid(head)
        h = self.reverseList(mid)

        ans = 0
        while h:
            ans = max(ans, h.val + head.val)
            h = h.next
            head = head.next
        return ans
