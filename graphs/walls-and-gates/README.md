# Walls and Gates

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/walls-and-gates/

## Problem

You are given an m x n grid rooms with three possible values: -1 for a wall or an obstacle, 0 for a gate, and INF (2147483647) for an empty room. Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should remain INF.

## Approach

Multi-source BFS

## Explanation

Multi-source BFS from all gates fills distances.

## Complexity

- Time: O(m*n)
- Space: O(m*n)

## Alternatives

Two-pass DP.

## Common mistakes

Starting BFS from empty rooms.

## Learning notes

Gate problems often use simultaneous BFS sources.

## Solution

```python
from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        q = deque()
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))

```
