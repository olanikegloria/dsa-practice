# Longest Increasing Path in a Matrix

**Topic:** dynamic-programming  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

## Problem

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

## Approach

DFS + memoization

## Explanation

DFS with memo from each cell along increasing edges.

## Complexity

- Time: O(mn)
- Space: O(mn)

## Alternatives

Topological sort by out-degree.

## Common mistakes

Allowing equal or decreasing moves.

## Learning notes

DAG structure avoids cycles in increasing paths.

## Solution

```python
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r: int, c: int) -> int:
            if memo[r][c]:
                return memo[r][c]
            best = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            memo[r][c] = best
            return best

        return max(dfs(r, c) for r in range(m) for c in range(n))

```
