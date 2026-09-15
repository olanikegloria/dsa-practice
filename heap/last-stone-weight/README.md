# Last Stone Weight

**Topic:** heap  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/last-stone-weight/

## Problem

You are given an array of integers stones where stones[i] is the weight of the ith stone. On each turn, choose the heaviest two stones and smash them together. Return the weight of the last remaining stone. If there are no stones left, return 0.

## Approach

Max-heap simulation

## Explanation

Max-heap smash two heaviest; push difference if unequal.

## Complexity

- Time: O(n log n)
- Space: O(n)

## Alternatives

Sorted multiset.

## Common mistakes

Using min-heap without negation.

## Learning notes

Negate values to simulate max-heap in Python.

## Solution

```python
from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            if a != b:
                heapq.heappush(heap, -(a - b))
        return -heap[0] if heap else 0

```
