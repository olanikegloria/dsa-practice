# Lowest Common Ancestor of a Binary Tree

**Topic:** trees  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

## Problem

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

## Approach

Postorder DFS

## Explanation

If both sides return non-null, current node is LCA.

## Complexity

- Time: O(n)
- Space: O(h)

## Alternatives

Parent pointer walk.

## Common mistakes

Assuming BST ordering.

## Learning notes

General LCA uses divide-and-conquer on binary tree.

## Solution

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right

```
