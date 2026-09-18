# Interleaving String

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/interleaving-string/

## Problem

Given strings s1, s2, and s3, return true if s3 is formed by an interleaving of s1 and s2.

## Approach

Dynamic programming

## Explanation

2D DP tracks whether prefix interleaving is possible.

## Complexity

- Time: O(mn)
- Space: O(mn)

## Alternatives

DFS with memo.

## Common mistakes

Wrong index into s3.

## Learning notes

Grid DP for two-sequence merge problems.

## Solution

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i > 0 and dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]:
                    dp[i][j] = True
                if j > 0 and dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]:
                    dp[i][j] = True
        return dp[len(s1)][len(s2)]

```
