from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 找中点
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 反转后半部分
        if slow:
            # 将最后一个也包含进去，这样不用特殊处理将最后一个指向 None
            h1 = self.reverseList(slow)
            slow = head
            # 开始重排
            while h1.next:
                pre_next = slow.next
                suf_next = h1.next

                slow.next = h1
                h1.next = pre_next

                h1 = suf_next
                slow = pre_next
