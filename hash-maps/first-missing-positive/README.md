# First Missing Positive

**Topic:** hash-maps  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/first-missing-positive/

## Problem

Given an unsorted integer array nums, return the smallest missing positive integer. You must run in O(n) time and use O(1) auxiliary space.

## Approach

Index as hash bucket

## Explanation

Place value v at index v-1 when possible; scan for first mismatch.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Boolean presence array sized n.

## Common mistakes

Infinite swap loops without guard.

## Learning notes

Only positions 1..n matter.

## Solution

```python
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1
        return n + 1

```
