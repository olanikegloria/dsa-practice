# Longest Common Prefix

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/longest-common-prefix/

## Problem

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

## Approach

Vertical scanning

## Explanation

Shrink shared prefix until all strings match.

## Complexity

- Time: O(S) total chars
- Space: O(1)

## Alternatives

Sort then compare ends.

## Common mistakes

Comparing full strings each time inefficiently.

## Learning notes

Prefix problems often use incremental shrinking.

## Solution

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

```
