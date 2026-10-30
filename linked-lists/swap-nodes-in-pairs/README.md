# Swap Nodes in Pairs

**Topic:** linked-lists  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/swap-nodes-in-pairs/

## Problem

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes.

## Approach

Iterative pointer swap

## Explanation

Rewire pairs using dummy head; advance prev by two each step.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Recursive swap.

## Common mistakes

Losing reference to rest of list.

## Learning notes

Dummy node simplifies head swap.

## Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            a.next = b.next
            b.next = a
            prev.next = b
            prev = a
        return dummy.next

```
