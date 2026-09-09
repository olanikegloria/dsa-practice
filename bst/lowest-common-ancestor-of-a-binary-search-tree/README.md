# Lowest Common Ancestor of a Binary Search Tree

**Topic:** bst  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

## Problem

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

## Approach

Use the BST ordering to find the split point

## Explanation

If both targets are smaller, go left. If both are larger, go right. The first split point is the answer.

## Complexity

- Time: O(h)
- Space: O(1)

## Alternatives

A generic binary-tree LCA traversal works but ignores the BST ordering.

## Common mistakes

Forgetting that one target may itself be the lowest common ancestor.

## Learning notes

Ordered trees turn a whole-tree search into one root-to-leaf walk.

## Solution

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lo, hi = sorted((p.val, q.val))
        cur = root
        while cur:
            if cur.val < lo:
                cur = cur.right
            elif cur.val > hi:
                cur = cur.left
            else:
                return cur
        raise ValueError("nodes are not in the tree")

```
