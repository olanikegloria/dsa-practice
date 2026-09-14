# Path Sum

**Topic:** trees  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/path-sum/

## Problem

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

## Approach

DFS root-to-leaf

## Explanation

Subtract node value; check leaf when sum reaches zero.

## Complexity

- Time: O(n)
- Space: O(h)

## Alternatives

Prefix sum map for any path.

## Common mistakes

Treating internal nodes as leaves.

## Learning notes

Path sum requires leaf termination check.

## Solution

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)

```
