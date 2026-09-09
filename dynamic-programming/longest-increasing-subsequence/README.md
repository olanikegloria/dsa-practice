# Longest Increasing Subsequence

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/longest-increasing-subsequence/

## Problem

Given an integer array nums, return the length of the longest strictly increasing subsequence.

## Approach

Patience sorting with binary search

## Explanation

tails[i] is the smallest tail of an increasing subsequence of length i + 1. Each value either grows that list or replaces a tail.

## Complexity

- Time: O(n log n)
- Space: O(n)

## Alternatives

Classic O(n^2) DP comparing every earlier index.

## Common mistakes

Using <= in the search, which allows a non-strict increase.

## Learning notes

The tails array is not itself a subsequence, only a length oracle.

## Solution

```python
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: List[int] = []
        for n in nums:
            lo, hi = 0, len(tails)
            while lo < hi:
                mid = (lo + hi) // 2
                if tails[mid] < n:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == len(tails):
                tails.append(n)
            else:
                tails[lo] = n
        return len(tails)

```
