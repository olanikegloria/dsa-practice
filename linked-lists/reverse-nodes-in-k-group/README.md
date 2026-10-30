# Reverse Nodes in k-Group

**Topic:** linked-lists  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/reverse-nodes-in-k-group/

## Problem

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. k is a positive integer and is less than or equal to the length of the linked list.

## Approach

Block reversal with dummy

## Explanation

Reverse each full k-block; leave tail unchanged.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Recursion with k-step advance.

## Common mistakes

Reversing partial final group.

## Learning notes

Cut segment, reverse, reconnect.

## Solution

```python
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

```
