# Linked List Cycle

**Topic:** linked-lists  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/linked-list-cycle/

## Problem

Given head, the head of a linked list, determine if the linked list has a cycle in it. Return true if there is a cycle in the linked list. Otherwise, return false.

## Approach

Floyd's two pointers

## Explanation

A fast pointer moving two steps meets a slow pointer inside any cycle, and falls off the end when there is none.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

A visited set of node identities, which costs O(n) memory.

## Common mistakes

Comparing values instead of node identity, or not checking fast.next before advancing twice.

## Learning notes

Two speeds on the same path is the cheapest cycle test there is.

## Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

```
