# Balanced Binary Tree

**Topic:** trees  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/balanced-binary-tree/

## Problem

Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## Approach

DFS height with early exit

## Explanation

Return -1 sentinel when subtree height imbalance found.

## Complexity

- Time: O(n)
- Space: O(h)

## Alternatives

Store heights in map.

## Common mistakes

Recomputing heights separately per node O(n^2).

## Learning notes

Balance check combines height compute and validation.

## Solution

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return height(root) != -1

```
