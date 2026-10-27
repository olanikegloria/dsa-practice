# 3Sum Closest

**Topic:** two-pointers  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/3sum-closest/

## Problem

Given an integer array nums and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers.

## Approach

Sort + two pointers

## Explanation

Sort; fix i and two-pointer scan tracking closest sum.

## Complexity

- Time: O(n^2)
- Space: O(1)

## Alternatives

Binary search on third element.

## Common mistakes

Not updating best on equal distance ties correctly.

## Learning notes

Same skeleton as 3Sum without duplicate skipping.

## Solution

```python
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n - 2):
            lo, hi = i + 1, n - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if abs(s - target) < abs(best - target):
                    best = s
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
                else:
                    return s
        return best

```
