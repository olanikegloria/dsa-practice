# Meeting Rooms

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/meeting-rooms/

## Problem

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

## Approach

Sort and compare neighbors

## Explanation

After sorting by start, any overlap means conflict.

## Complexity

- Time: O(n log n)
- Space: O(1)

## Alternatives

Sweep line.

## Common mistakes

Not sorting first.

## Learning notes

Meeting room I is simple overlap detection.

## Solution

```python
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True

```
