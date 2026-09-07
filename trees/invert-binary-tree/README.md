# Invert Binary Tree

**Topic:** trees  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/invert-binary-tree/

## Problem

Given the root of a binary tree, invert the tree, and return its root.

## Approach

DFS swap

## Explanation

Swap children recursively.

## Complexity

- Time: O(n)
- Space: O(h)

## Alternatives

BFS queue swap.

## Common mistakes

Forgetting to assign swapped children back.

## Learning notes

Structural transforms map cleanly to recursion.

## Solution

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

```
