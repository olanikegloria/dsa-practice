# Container With Most Water

**Topic:** two-pointers  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/container-with-most-water/

## Problem

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container such that the container contains the most water. Return the maximum amount of water a container can store.

## Approach

Two pointers from the ends

## Explanation

Area is limited by the shorter wall, so moving the shorter pointer inward is the only move that can improve the answer.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Check every pair in O(n^2).

## Common mistakes

Moving the taller pointer, or using max instead of min for the height.

## Learning notes

When width shrinks every step, only a taller wall can pay for it.

## Solution

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            best = max(best, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best

```
