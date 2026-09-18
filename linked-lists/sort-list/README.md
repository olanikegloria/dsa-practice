# Sort List

**Topic:** linked-lists  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/sort-list/

## Problem

Given the head of a linked list, return the list after sorting it in ascending order.

## Approach

Merge sort on linked list

## Explanation

Merge sort: split with slow/fast, recursively sort halves, merge.

## Complexity

- Time: O(n log n)
- Space: O(log n)

## Alternatives

Convert to array, sort, rebuild.

## Common mistakes

Not breaking link before merge.

## Learning notes

Bottom-up merge sort saves recursion depth.

## Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        def merge(a, b):
            dummy = ListNode()
            cur = dummy
            while a and b:
                if a.val <= b.val:
                    cur.next = a
                    a = a.next
                else:
                    cur.next = b
                    b = b.next
                cur = cur.next
            cur.next = a or b
            return dummy.next

        return merge(self.sortList(head), self.sortList(mid))

```
