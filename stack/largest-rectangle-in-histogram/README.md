# Largest Rectangle in Histogram

**Topic:** stack  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/largest-rectangle-in-histogram/

## Problem

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

## Approach

Monotonic stack

## Explanation

Monotonic stack tracks indices; pop when height drops to compute width.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

Divide and conquer.

## Common mistakes

Wrong width after pop.

## Learning notes

Sentinel zero height simplifies flush at end.

## Solution

```python
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                idx = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                best = max(best, heights[idx] * width)
            stack.append(i)
        heights.pop()
        return best

```
