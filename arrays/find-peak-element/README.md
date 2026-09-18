# Find Peak Element

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/find-peak-element/

## Problem

A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array nums, find a peak element, and return its index.

## Approach

Binary search

## Explanation

Binary search toward the larger neighbor until local peak.

## Complexity

- Time: O(log n)
- Space: O(1)

## Alternatives

Linear scan.

## Common mistakes

Assuming global maximum instead of any peak.

## Learning notes

Compare mid with mid+1 to shrink interval.

## Solution

```python
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo

```
