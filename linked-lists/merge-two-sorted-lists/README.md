# Merge Two Sorted Lists

**Topic:** linked-lists  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/merge-two-sorted-lists/

## Problem

You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

## Approach

Dummy head merge

## Explanation

Two-pointer merge like merge-sort merge step.

## Complexity

- Time: O(n + m)
- Space: O(1)

## Alternatives

Recursion.

## Common mistakes

Forgetting remaining tail attach.

## Learning notes

Dummy nodes simplify edge cases.

## Solution

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next

```
