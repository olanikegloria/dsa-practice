# Longest Common Subsequence

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/longest-common-subsequence/

## Problem

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

## Approach

2D DP

## Explanation

Classic 2D DP: match adds 1 else take max skip.

## Complexity

- Time: O(m*n)
- Space: O(m*n)

## Alternatives

1D rolling array.

## Common mistakes

Off-by-one on indices.

## Learning notes

LCS template applies to many string DP problems.

## Solution

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

```
