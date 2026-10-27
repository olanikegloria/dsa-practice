# Unique Paths II

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/unique-paths-ii/

## Problem

You are given an m x n integer array grid. There is a robot initially located at the top-left corner. The robot tries to move to the bottom-right corner. The robot can only move either down or right at any point in time. An obstacle and space are marked as 1 or 0 respectively. Return the number of possible unique paths.

## Approach

1D DP compression

## Explanation

Rolling DP row: paths to cell equals top + left unless blocked.

## Complexity

- Time: O(m * n)
- Space: O(n)

## Alternatives

2D DP table.

## Common mistakes

Not zeroing blocked cells.

## Learning notes

Same as unique paths with obstacle resets.

## Solution

```python
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return 0
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[n - 1]

```
