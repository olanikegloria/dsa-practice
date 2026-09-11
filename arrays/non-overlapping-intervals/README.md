# Non-overlapping Intervals

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/non-overlapping-intervals/

## Problem

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

## Approach

Greedy by end

## Explanation

Greedy keep interval with earliest end time.

## Complexity

- Time: O(n log n)
- Space: O(1)

## Alternatives

DP on intervals.

## Common mistakes

Sorting by start instead of end.

## Learning notes

Earliest-finish-time greedy for intervals.

## Solution

```python
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = float("-inf")
        removed = 0
        for start, e in intervals:
            if start < end:
                removed += 1
            else:
                end = e
        return removed

```
