# All Nodes Distance K in Binary Tree

**Topic:** trees  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

## Problem

Given the root of a binary tree, the value of a target node, and an integer k, return an array of the values of all nodes that have distance k from the target node.

## Approach

Parent map + BFS

## Explanation

Map parents then BFS from target up/down to distance k.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

Convert to graph once.

## Common mistakes

Ignoring upward moves to parent.

## Learning notes

Undirected view of tree enables distance from any node.

## Solution

```python
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def walk(node, par):
            if not node:
                return
            parent[node] = par
            walk(node.left, node)
            walk(node.right, node)

        walk(root, None)
        q = [(target, 0)]
        seen = {target}
        out = []
        idx = 0
        while idx < len(q):
            node, d = q[idx]
            idx += 1
            if d == k:
                out.append(node.val)
            elif d < k:
                for nxt in (node.left, node.right, parent.get(node)):
                    if nxt and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, d + 1))
        return out

```
