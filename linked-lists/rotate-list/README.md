# Rotate List

**Topic:** linked-lists  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/rotate-list/

## Problem

Given the head of a linked list, rotate the list to the right by k places.

## Approach

Circular link then cut

## Explanation

Find length, link tail to head, break at n-k.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Copy to array and rebuild.

## Common mistakes

Not reducing k modulo length.

## Learning notes

One pass to count then one to rotate.

## Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        k %= n
        if k == 0:
            return head
        cur = head
        for _ in range(n - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        tail.next = head
        return new_head

```
