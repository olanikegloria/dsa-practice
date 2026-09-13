# Meeting Rooms II

**Topic:** heap  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/meeting-rooms-ii/

## Problem

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

## Approach

Min-heap of end times

## Explanation

Min-heap of end times tracks concurrent meetings.

## Complexity

- Time: O(n log n)
- Space: O(n)

## Alternatives

Chronological event sweep.

## Common mistakes

Pushing starts instead of ends.

## Learning notes

Reuse freed rooms when next start >= earliest end.

## Solution

```python
from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)

```
