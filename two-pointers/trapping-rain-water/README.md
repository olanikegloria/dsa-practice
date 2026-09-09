# Trapping Rain Water

**Topic:** two-pointers  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/trapping-rain-water/

## Problem

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Approach

Two pointers with left and right maxima

## Explanation

Water on a bar is limited by the shorter of the two running maxima. Move the pointer under the smaller wall.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Precompute left-max and right-max arrays.

## Common mistakes

Using the current bar as the bound instead of the max seen so far.

## Learning notes

The smaller side is the only one whose water can be finalized this step.

## Solution

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        return water

```
