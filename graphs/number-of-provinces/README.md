# Number of Provinces

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/number-of-provinces/

## Problem

There are n cities connected by some number of direct flights. Return the total number of provinces, where a province is a group of directly or indirectly connected cities.

## Approach

DFS connected components

## Explanation

Each unvisited node starts a DFS over adjacency matrix edges.

## Complexity

- Time: O(n^2)
- Space: O(n)

## Alternatives

Union-Find.

## Common mistakes

Counting edges instead of components.

## Learning notes

Adjacency matrix graph; same as connected components count.

## Solution

```python
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = [False] * n

        def dfs(i):
            seen[i] = True
            for j in range(n):
                if isConnected[i][j] and not seen[j]:
                    dfs(j)

        provinces = 0
        for i in range(n):
            if not seen[i]:
                provinces += 1
                dfs(i)
        return provinces

```
