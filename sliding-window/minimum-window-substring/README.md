# Minimum Window Substring

**Topic:** sliding-window  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/minimum-window-substring/

## Problem

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

## Approach

Sliding window with a remaining-need counter

## Explanation

Grow a window until every required character is covered, then shrink from the left and keep the shortest valid window.

## Complexity

- Time: O(n)
- Space: O(k)

## Alternatives

Check every substring, which is O(n^2).

## Common mistakes

Forgetting duplicate counts in t, or updating the answer after shrinking past a valid window.

## Learning notes

A coverage counter turns the usual frequency map into a single missing total.

## Solution

```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        best_left = 0
        best_len = float("inf")
        left = 0
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if right - left + 1 < best_len:
                    best_left = left
                    best_len = right - left + 1
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return "" if best_len == float("inf") else s[best_left:best_left + int(best_len)]

```
