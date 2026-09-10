# Reorder List

**Topic:** linked-lists  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/reorder-list/

## Problem

You are given the head of a singly linked-list. The list can be represented as: L0 → L1 → … → Ln - 1 → Ln. Reorder the list to be on the following form: L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

## Approach

Midpoint split, reverse, and merge

## Explanation

Split at the midpoint, reverse the second half, then weave the two lists together.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Store nodes in an array and pick from both ends.

## Common mistakes

Leaving the two halves linked, which creates a cycle after the reverse.

## Learning notes

The in-place reorder is three classic list tricks in sequence.

## Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        first, second = head, prev
        while second:
            n1, n2 = first.next, second.next
            first.next = second
            second.next = n1
            first, second = n1, n2

```
