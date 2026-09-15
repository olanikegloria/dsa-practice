# House Robber II

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/house-robber-ii/

## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Approach

Two linear DP passes

## Explanation

Rob linear excluding first or last house; take max.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

DP with modulo states.

## Common mistakes

Including both first and last house.

## Learning notes

Circular constraints split into two subproblems.

## Solution

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_line(arr):
            prev2 = prev1 = 0
            for n in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + n)
            return prev1
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))

```
