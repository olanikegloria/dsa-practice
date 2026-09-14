# Diameter of Binary Tree

**Topic:** trees  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/diameter-of-binary-tree/

## Problem

Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

## Approach

DFS depth with global max

## Explanation

Diameter through node is left_depth + right_depth.

## Complexity

- Time: O(n)
- Space: O(h)

## Alternatives

Two-pass height computation.

## Common mistakes

Counting nodes instead of edges.

## Learning notes

Diameter is max sum of subtree heights at any node.

## Solution

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.best = max(self.best, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.best

```
