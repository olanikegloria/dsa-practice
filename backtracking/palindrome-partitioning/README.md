# Palindrome Partitioning

**Topic:** backtracking  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/palindrome-partitioning/

## Problem

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

## Approach

Backtracking with a palindrome check

## Explanation

From each start index, take every palindrome prefix and recurse on the suffix.

## Complexity

- Time: O(n * 2^n)
- Space: O(n)

## Alternatives

Precompute a palindrome DP table to make each check O(1).

## Common mistakes

Only splitting on even or odd lengths, which misses mixed partitions.

## Learning notes

Every complete path is one valid partition because each piece was checked.

## Solution

```python
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out: List[List[str]] = []
        path: List[str] = []

        def is_pal(lo: int, hi: int) -> bool:
            while lo < hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        def dfs(start: int) -> None:
            if start == len(s):
                out.append(path[:])
                return
            for end in range(start, len(s)):
                if is_pal(start, end):
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return out

```
