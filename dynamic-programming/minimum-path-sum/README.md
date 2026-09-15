# Minimum Path Sum

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/minimum-path-sum/

## Problem

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time.

## Approach

Grid DP in-place

## Explanation

In-place DP: cell stores min path sum from top-left.

## Complexity

- Time: O(m*n)
- Space: O(1)

## Alternatives

Extra DP table.

## Common mistakes

Not handling first row/col base cases.

## Learning notes

Min path grid DP only moves down or right.

## Solution

```python
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                top = grid[i - 1][j] if i > 0 else float('inf')
                left = grid[i][j - 1] if j > 0 else float('inf')
                grid[i][j] += min(top, left)
        return grid[m - 1][n - 1]

```
