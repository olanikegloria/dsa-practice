# Valid Anagram

**Topic:** hash-maps  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/valid-anagram/

## Problem

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

## Approach

Frequency counting

## Explanation

Anagrams share identical character frequencies.

## Complexity

- Time: O(n)
- Space: O(1) for lowercase alphabet / O(k) generally

## Alternatives

Sort both strings and compare.

## Common mistakes

Ignoring length mismatch early exit.

## Learning notes

Counters are the natural anagram tool.

## Solution

```python
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

```
