# Word Break

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/word-break/

## Problem

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words. Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Approach

Boolean DP over prefixes

## Explanation

ok[i] is true when the prefix s[:i] can be split into dictionary words. Each new cut checks every earlier true prefix.

## Complexity

- Time: O(n^2)
- Space: O(n)

## Alternatives

Memoized recursion from each start index.

## Common mistakes

Requiring unique words, or forgetting a word can be reused.

## Learning notes

The dictionary is a set so each candidate slice is an O(1) lookup after hashing.

## Solution

```python
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        ok = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            ok[i] = any(ok[j] and s[j:i] in words for j in range(i))
        return ok[-1]

```
