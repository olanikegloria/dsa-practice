# Find First and Last Position of Element in Sorted Array

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## Problem

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found, return [-1, -1].

## Approach

Binary search bounds

## Explanation

Two binary searches for leftmost and rightmost indices.

## Complexity

- Time: O(log n)
- Space: O(1)

## Alternatives

Linear scan after one binary search.

## Common mistakes

Off-by-one in right bound search.

## Learning notes

Template for lower/upper bound on sorted arrays.

## Solution

```python
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bound():
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def right_bound():
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo - 1

        if not nums:
            return [-1, -1]
        l, r = left_bound(), right_bound()
        if l > r or nums[l] != target:
            return [-1, -1]
        return [l, r]

```
