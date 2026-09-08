# Maximum Subarray

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/maximum-subarray/

## Problem

Given an integer array nums, find the subarray with the largest sum, and return its sum.

## Approach

Kadane's running maximum

## Explanation

At each index the best subarray ending there either extends the previous one or restarts at the current value.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Divide and conquer in O(n log n), or prefix sums with a running minimum.

## Common mistakes

Starting best at 0, which breaks on all-negative input.

## Learning notes

One local decision per element is enough when the choice only depends on the previous state.

## Solution

```python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = cur = nums[0]
        for n in nums[1:]:
            cur = max(n, cur + n)
            best = max(best, cur)
        return best

```
