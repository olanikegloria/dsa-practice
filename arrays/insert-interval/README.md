# Insert Interval

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/insert-interval/

## Problem

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval. Insert newInterval into intervals such that intervals remains sorted and still does not have any overlapping intervals.

## Approach

Three-phase sweep

## Explanation

Append before, merge overlaps, append rest.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

Binary search insert point.

## Common mistakes

Not merging all overlaps.

## Learning notes

Same merge logic as merge-intervals.

## Solution

```python
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            out.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        out.append(newInterval)
        out.extend(intervals[i:])
        return out

```
