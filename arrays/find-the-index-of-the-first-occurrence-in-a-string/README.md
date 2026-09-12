# Find the Index of the First Occurrence in a String

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

## Problem

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## Approach

Brute force / KMP

## Explanation

Scan haystack windows of needle length.

## Complexity

- Time: O(n*m)
- Space: O(1)

## Alternatives

KMP O(n+m).

## Common mistakes

Off-by-one on loop bounds.

## Learning notes

String search is a classic pattern-matching problem.

## Solution

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1

```
