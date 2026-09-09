# Binary Tree Level Order Traversal

**Topic:** trees  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/binary-tree-level-order-traversal/

## Problem

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## Approach

Breadth-first search by levels

## Explanation

A queue holds one level at a time. Drain that level, record the values, and enqueue the children for the next round.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

DFS with a depth index that appends into out[depth].

## Common mistakes

Mixing nodes from two levels in one list by forgetting to snapshot the queue length.

## Learning notes

The queue length at the start of a loop is the current level size.

## Solution

```python
from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        out: List[List[int]] = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(level)
        return out

```
