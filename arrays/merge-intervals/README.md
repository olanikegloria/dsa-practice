# Merge Intervals

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/merge-intervals/

## Problem

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Approach

Sort and sweep

## Explanation

Sort by start; merge overlapping into last interval.

## Complexity

- Time: O(n log n)
- Space: O(n)

## Alternatives

Sweep line.

## Common mistakes

Forgetting max end on overlap.

## Learning notes

Interval problems often start with sorting.

## Solution

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        out = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= out[-1][1]:
                out[-1][1] = max(out[-1][1], end)
            else:
                out.append([start, end])
        return out

```
