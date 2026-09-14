# Flatten Binary Tree to Linked List

**Topic:** trees  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

## Problem

Given the root of a binary tree, flatten the tree into a "linked list" in-place. The "linked list" should use the TreeNode right pointer, and the left pointer should always be null.

## Approach

Morris-like pointer splice

## Explanation

For each node, splice left subtree before right subtree.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Preorder recursion with reversed build.

## Common mistakes

Losing right subtree when attaching left.

## Learning notes

In-place flatten reuses existing TreeNode links.

## Solution

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                prev = cur.left
                while prev.right:
                    prev = prev.right
                prev.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

```
