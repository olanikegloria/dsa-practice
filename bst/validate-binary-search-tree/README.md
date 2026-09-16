# Validate Binary Search Tree

**Topic:** bst  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/validate-binary-search-tree/

## Problem

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

## Approach

DFS with bounds

## Explanation

Each node must fall within (min, max) bounds inherited from ancestors.

## Complexity

- Time: O(n)
- Space: O(h)

## Alternatives

Inorder traversal checking sorted order.

## Common mistakes

Only comparing parent-child, not global bounds.

## Learning notes

BST validation is about valid ranges, not local checks.

## Solution

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lo, hi):
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            return dfs(node.left, lo, node.val) and dfs(node.right, node.val, hi)
        return dfs(root, float('-inf'), float('inf'))

```
