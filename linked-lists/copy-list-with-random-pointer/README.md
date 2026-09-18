# Copy List with Random Pointer

**Topic:** linked-lists  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/copy-list-with-random-pointer/

## Problem

A linked list of length n is given such that each node contains an additional random pointer. Construct a deep copy of the list.

## Approach

Hash map two-pass

## Explanation

Map original nodes to clones, then wire next and random.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

Interleave cloned nodes in one pass.

## Common mistakes

Using old pointers in clone random field.

## Learning notes

Deep copy graphs/lists always needs old→new mapping.

## Solution

```python
from typing import Optional

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        old_to_new = {}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next
        return old_to_new[head]

```
