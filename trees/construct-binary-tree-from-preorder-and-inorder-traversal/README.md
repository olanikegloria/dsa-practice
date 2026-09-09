# Construct Binary Tree from Preorder and Inorder Traversal

**Topic:** trees  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## Problem

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

## Approach

Recursion with an inorder index map

## Explanation

Preorder gives the next root. Inorder tells you how many nodes belong on its left, so the same walk builds both subtrees.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

Slice the arrays at each step, which copies O(n^2) values.

## Common mistakes

Building the right subtree first, which consumes the left preorder values.

## Learning notes

The preorder cursor only moves forward, so the call order must match the traversal.

## Solution

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {v: i for i, v in enumerate(inorder)}
        i = 0

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            nonlocal i
            if lo > hi:
                return None
            val = preorder[i]
            i += 1
            mid = index[val]
            node = TreeNode(val)
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(inorder) - 1)

```
