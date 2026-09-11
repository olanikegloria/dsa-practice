# Find Minimum in Rotated Sorted Array

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Problem

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. Given the sorted rotated array nums of unique elements, return the minimum element of this array.

## Approach

Binary search

## Explanation

Binary search for rotation point where right side is greater.

## Complexity

- Time: O(log n)
- Space: O(1)

## Alternatives

Linear scan.

## Common mistakes

Comparing mid with lo incorrectly.

## Learning notes

Compare mid with hi to find min side.

## Solution

```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

```
