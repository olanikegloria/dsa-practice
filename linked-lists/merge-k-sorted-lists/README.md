# Merge k Sorted Lists

**Topic:** linked-lists  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/merge-k-sorted-lists/

## Problem

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

## Approach

Min-heap merge

## Explanation

Pop smallest head among k lists via min-heap.

## Complexity

- Time: O(N log k)
- Space: O(k)

## Alternatives

Divide and conquer merge.

## Common mistakes

Not using stable tie-breaker index.

## Learning notes

Heap merge is classic for k-way merge.

## Solution

```python
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

```
