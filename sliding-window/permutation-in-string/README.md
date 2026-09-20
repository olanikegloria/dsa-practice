# Permutation in String

**Topic:** sliding-window  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/permutation-in-string/

## Problem

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

## Approach

Sliding window

## Explanation

Fixed-size sliding window compares frequency counts to s1.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Sort substrings (slow).

## Common mistakes

Window size off by one.

## Learning notes

Anagram detection is frequency equality at window size.

## Solution

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0] * 26
        window = [0] * 26
        for ch in s1:
            need[ord(ch) - ord("a")] += 1
        k = len(s1)
        for i, ch in enumerate(s2):
            window[ord(ch) - ord("a")] += 1
            if i >= k:
                window[ord(s2[i - k]) - ord("a")] -= 1
            if i >= k - 1 and window == need:
                return True
        return False

```
