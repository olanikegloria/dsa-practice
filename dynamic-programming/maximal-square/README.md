# Maximal Square

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/maximal-square/

## Problem

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

## Approach

2D DP square side

## Explanation

dp[i][j] is side length of largest square ending at cell.

## Complexity

- Time: O(m*n)
- Space: O(m*n)

## Alternatives

Expand around centers.

## Common mistakes

Returning side instead of area.

## Learning notes

Square DP uses min of three neighbors plus one.

## Solution

```python
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        best = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    best = max(best, dp[i][j])
        return best * best

```
