# Triangle

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/triangle/

## Problem

Given a triangle array triangle, return the minimum path sum from top to bottom.

## Approach

1D bottom-up DP

## Explanation

Bottom-up min path: dp[j] is best from (i,j) to base.

## Complexity

- Time: O(n^2)
- Space: O(n)

## Alternatives

Top-down memoization.

## Common mistakes

Modifying triangle in place incorrectly.

## Learning notes

Classic triangle min-path DP.

## Solution

```python
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]

```
