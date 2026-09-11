# Search in Rotated Sorted Array

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/search-in-rotated-sorted-array/

## Problem

There is an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index. Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

## Approach

Modified binary search

## Explanation

Binary search on rotated array by identifying sorted half.

## Complexity

- Time: O(log n)
- Space: O(1)

## Alternatives

Find pivot then search.

## Common mistakes

Wrong half selection.

## Learning notes

Rotated sorted arrays still allow log search.

## Solution

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

```
