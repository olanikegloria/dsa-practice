# Find Median from Data Stream

**Topic:** heap  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/find-median-from-data-stream/

## Problem

The median is the middle value in an ordered integer list. Design a data structure that supports adding integers and finding the median of all integers received so far.

## Approach

Two heaps kept within one size of each other

## Explanation

A max-heap holds the lower half and a min-heap holds the upper half. The median is always on one of the two tops.

## Complexity

- Time: O(log n) per add, O(1) median
- Space: O(n)

## Alternatives

Keep a sorted list and insert with bisect, which is O(n) per add.

## Common mistakes

Forgetting to rebalance after every insert, or storing the lower half as a min-heap.

## Learning notes

Two heaps split an ordered stream without sorting the whole list.

## Solution

```python
import heapq

class MedianFinder:
    def __init__(self) -> None:
        self.low: list[int] = []
        self.high: list[int] = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2


class Solution:
    def build(self) -> MedianFinder:
        return MedianFinder()

```
