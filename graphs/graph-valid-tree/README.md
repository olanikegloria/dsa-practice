# Graph Valid Tree

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/graph-valid-tree/

## Problem

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph. Return true if the edges of the given graph make up a valid tree, and false otherwise.

## Approach

Union-Find

## Explanation

Tree has exactly n-1 edges and no cycles (Union-Find).

## Complexity

- Time: O(n alpha(n))
- Space: O(n)

## Alternatives

BFS/DFS connectivity check.

## Common mistakes

Only checking edge count.

## Learning notes

Valid tree iff connected acyclic with n-1 edges.

## Solution

```python
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[rb] = ra
            return True
        for a, b in edges:
            if not union(a, b):
                return False
        return True

```
