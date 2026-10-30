from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(node):
            n = 0
            while node:
                n += 1
                node = node.next
            return n

        def reverse(a, b):
            prev = None
            cur = a
            while cur != b:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        dummy = ListNode(0, head)
        prev_group = dummy
        remaining = length(head)
        while remaining >= k:
            start = prev_group.next
            end = start
            for _ in range(k - 1):
                end = end.next
            nxt = end.next
            end.next = None
            prev_group.next = reverse(start, None)
            start.next = nxt
            prev_group = start
            remaining -= k
        return dummy.next
