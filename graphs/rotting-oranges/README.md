# Rotting Oranges

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/rotting-oranges/

## Problem

You are given an m x n grid where each cell can have one of three values: 0 empty, 1 fresh orange, 2 rotten orange. Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

## Approach

Multi-source breadth-first search

## Explanation

Every currently rotten orange starts a multi-source BFS. Fresh neighbors rot one minute later.

## Complexity

- Time: O(m * n)
- Space: O(m * n)

## Alternatives

Simulate minute by minute on a copy of the grid.

## Common mistakes

Returning 0 when leftover fresh oranges make the answer -1.

## Learning notes

All sources in the queue at time 0 is what makes the clock correct.

## Solution

```python
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        while q:
            r, c, minutes = q.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, minutes + 1))
        return -1 if fresh else minutes

```
