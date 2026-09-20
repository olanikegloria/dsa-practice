# Minimum Size Subarray Sum

**Topic:** sliding-window  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/minimum-size-subarray-sum/

## Problem

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0.

## Approach

Sliding window

## Explanation

Grow window until sum >= target, then shrink from left.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Prefix sums + binary search.

## Common mistakes

Returning 1 when no valid window.

## Learning notes

Positive nums make two-pointer shrink valid.

## Solution

```python
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        best = float("inf")
        for right, n in enumerate(nums):
            total += n
            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if best == float("inf") else best

```
