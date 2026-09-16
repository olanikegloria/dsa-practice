# Longest Palindromic Substring

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/longest-palindromic-substring/

## Problem

Given a string s, return the longest palindromic substring in s.

## Approach

Center expansion

## Explanation

Expand around each center for odd/even palindromes.

## Complexity

- Time: O(n^2)
- Space: O(1)

## Alternatives

DP table O(n^2).

## Common mistakes

Only checking odd centers.

## Learning notes

Expand-around-center avoids full DP table.

## Solution

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        best = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            cand = odd if len(odd) >= len(even) else even
            if len(cand) > len(best):
                best = cand
        return best

```
