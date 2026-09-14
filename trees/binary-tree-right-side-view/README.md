# Binary Tree Right Side View

**Topic:** trees  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/binary-tree-right-side-view/

## Problem

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Approach

Level-order BFS

## Explanation

Last node at each BFS level is visible from right.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

DFS tracking depth and right-first.

## Common mistakes

Appending left after right incorrectly at level.

## Learning notes

Right-side view equals last node per level.

## Solution

```python
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        out = []
        while q:
            out.append(q[-1].val)
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return out

```
