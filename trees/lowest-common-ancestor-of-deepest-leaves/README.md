# Lowest Common Ancestor of Deepest Leaves

**Topic:** trees  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

## Problem

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

## Approach

DFS with depth

## Explanation

Postorder returns deepest node in subtree and its depth.

## Complexity

- Time: O(n)
- Space: O(h)

## Alternatives

Find deepest leaves then LCA.

## Common mistakes

Returning parent when depths equal incorrectly.

## Learning notes

When depths tie, current node is LCA of deepest leaves below.

## Solution

```python
from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node: Optional[TreeNode]) -> Tuple[TreeNode, int]:
            if not node:
                return None, 0
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)
            if left_depth > right_depth:
                return left_node, left_depth + 1
            if right_depth > left_depth:
                return right_node, right_depth + 1
            return node, left_depth + 1

        return dfs(root)[0]

```
