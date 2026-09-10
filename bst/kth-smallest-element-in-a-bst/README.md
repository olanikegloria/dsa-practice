# Kth Smallest Element in a BST

**Topic:** bst  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/kth-smallest-element-in-a-bst/

## Problem

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

## Approach

Iterative inorder until k hits zero

## Explanation

Inorder traversal of a BST visits values in sorted order, so the kth pop is the answer.

## Complexity

- Time: O(h + k)
- Space: O(h)

## Alternatives

Count nodes in the left subtree and recurse into one side.

## Common mistakes

Using preorder, which is not sorted.

## Learning notes

BST inorder is the cheapest sorted walk you can do.

## Solution

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right

```
