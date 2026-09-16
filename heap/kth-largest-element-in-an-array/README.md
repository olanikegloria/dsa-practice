# Kth Largest Element in an Array

**Topic:** heap  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/kth-largest-element-in-an-array/

## Problem

Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

## Approach

Heap nlargest

## Explanation

Keep k largest via heap; return smallest of them.

## Complexity

- Time: O(n log k)
- Space: O(k)

## Alternatives

Quickselect average O(n).

## Common mistakes

Confusing kth largest with kth smallest.

## Learning notes

Heaps solve streaming top-k problems.

## Solution

```python
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

```
