# Add Two Numbers

**Topic:** linked-lists  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/add-two-numbers/

## Problem

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

## Approach

Linked list traversal

## Explanation

Add digits with carry on reversed lists.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Convert to integers.

## Common mistakes

Missing final carry digit.

## Learning notes

Dummy head simplifies list construction.

## Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            carry, val = divmod(s, 10)
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next

```
