# Redundant Connection

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/redundant-connection/

## Problem

In this problem, a tree is an undirected graph consisting of n nodes and n - 1 edges. You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. Return an edge that can be removed so that the resulting graph is a tree of n nodes.

## Approach

Union-Find

## Explanation

First edge creating a cycle in Union-Find is redundant.

## Complexity

- Time: O(n alpha(n))
- Space: O(n)

## Alternatives

DFS cycle detection.

## Common mistakes

Returning last edge instead of first redundant.

## Learning notes

Redundant connection finds first cycle-closing edge.

## Solution

```python
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[rb] = ra
            return True
        for a, b in edges:
            if not union(a, b):
                return [a, b]
        return []

```
