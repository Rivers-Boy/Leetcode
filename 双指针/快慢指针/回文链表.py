from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 反转链表
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    # 找中点
    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 找中点 - 反转 - 比较
        mid = self.findMid(head)
        h1 = self.reverseList(mid)

        while h1:
            if h1.val != head.val:
                return False
            h1 = h1.next
            head = head.next
        return True
