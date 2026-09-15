# K Closest Points to Origin

**Topic:** heap  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/k-closest-points-to-origin/

## Problem

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

## Approach

Heap nsmallest by distance

## Explanation

Select k points with smallest squared distance to origin.

## Complexity

- Time: O(n log k)
- Space: O(k)

## Alternatives

Quickselect average O(n).

## Common mistakes

Using sqrt instead of squared distance.

## Learning notes

Distance ranking only needs squared values.

## Solution

```python
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda p: p[0]*p[0] + p[1]*p[1])

```
