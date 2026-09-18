# Course Schedule III

**Topic:** heap  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/course-schedule-iii/

## Problem

There are n different courses labeled from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi]. Return the maximum number of courses you can take.

## Approach

Greedy + max heap

## Explanation

Sort by deadline; drop longest course when time exceeds deadline.

## Complexity

- Time: O(n log n)
- Space: O(n)

## Alternatives

Try all subsets (too slow).

## Common mistakes

Not removing the longest enrolled course on overflow.

## Learning notes

Classic scheduling with deadlines pattern.

## Solution

```python
from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        heap = []
        time = 0
        for duration, last in courses:
            time += duration
            heapq.heappush(heap, -duration)
            if time > last:
                time += heapq.heappop(heap)
        return len(heap)

```
