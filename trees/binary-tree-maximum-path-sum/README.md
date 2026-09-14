# Binary Tree Maximum Path Sum

**Topic:** trees  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/binary-tree-maximum-path-sum/

## Problem

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. The path sum of a path is the sum of the node's values in the path. Given the root of a binary tree, return the maximum path sum of any non-empty path.

## Approach

Postorder DFS gain

## Explanation

At each node update global best with left+node+right; return one-arm gain.

## Complexity

- Time: O(n)
- Space: O(h)

## Alternatives

Track paths explicitly.

## Common mistakes

Allowing negative child arms without max(0).

## Learning notes

Tree path sum often splits local answer vs return value.

## Solution

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')
        def gain(node):
            if not node:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            self.best = max(self.best, node.val + left + right)
            return node.val + max(left, right)
        gain(root)
        return self.best

```
