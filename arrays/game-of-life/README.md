# Game of Life

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/game-of-life/

## Problem

According to Wikipedia's definition of the Game of Life, the next state is determined by the current state according to four rules. Given an m x n board, return the next state.

## Approach

Snapshot + neighbor count

## Explanation

Snapshot board, then write next generation from neighbor counts.

## Complexity

- Time: O(m * n)
- Space: O(1)

## Alternatives

Copy board.

## Common mistakes

Reading updated neighbors same pass.

## Learning notes

2-bit state preserves original live bit.

## Solution

```python
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        prev = [[board[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                live = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            live += prev[ni][nj]
                if prev[i][j]:
                    board[i][j] = 1 if live in (2, 3) else 0
                else:
                    board[i][j] = 1 if live == 3 else 0

```
