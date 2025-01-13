from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def doubleIt2(head: Optional[ListNode]) -> Optional[ListNode]:
    # 这里可以直接套用两数相加 II，这个方法就不写了
    # 另外我们可以思考下什么时候需要思考进位：下一位>4的时候
    if head.val > 4:
        head = ListNode(0, head)
    cur = head
    while cur:
        cur.val = cur.val * 2 % 10
        if cur.next and cur.next.val > 4:
            cur.val += 1
        cur = cur.next
    return head


def doubleIt1(head: Optional[ListNode]) -> Optional[ListNode]:
    # 返回的是进位数,递归途中顺便把每个node都重新 set
    def recur(head: Optional[ListNode]):
        if not head:
            return 0
        carry = recur(head.next)
        s = head.val + head.val + carry
        head.val = s % 10
        return s // 10

    carry = recur(head)
    if carry:
        p0 = ListNode(carry, head)
        return p0
    else:
        return head