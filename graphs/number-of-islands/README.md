# Number of Islands

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/number-of-islands/

## Problem

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

## Approach

DFS connected components

## Explanation

Each unseen land cell starts a DFS flood fill.

## Complexity

- Time: O(m*n)
- Space: O(m*n)

## Alternatives

BFS or Union-Find.

## Common mistakes

Not marking visited cells.

## Learning notes

Grid graphs reduce to counting components.

## Solution

```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count

```
