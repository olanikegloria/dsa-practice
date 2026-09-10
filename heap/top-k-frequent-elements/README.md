# Top K Frequent Elements

**Topic:** heap  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/top-k-frequent-elements/

## Problem

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Approach

Frequency map plus bucket sort

## Explanation

Frequency cannot exceed n, so bucket each value by its count and scan the buckets from high to low.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

A size-k min heap takes O(n log k), while sorting all counts takes O(n log n).

## Common mistakes

Sorting the original array instead of sorting or bucketing by frequency.

## Learning notes

A bounded integer key often replaces comparison sorting with buckets.

## Solution

```python
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for value, frequency in counts.items():
            buckets[frequency].append(value)
        out: List[int] = []
        for frequency in range(len(buckets) - 1, 0, -1):
            for value in buckets[frequency]:
                out.append(value)
                if len(out) == k:
                    return out
        return out

```
