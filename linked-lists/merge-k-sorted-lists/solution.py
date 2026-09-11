from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        uid = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, uid, node))
                uid += 1
        dummy = ListNode()
        cur = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, uid, node.next))
                uid += 1
        return dummy.next
