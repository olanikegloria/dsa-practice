# Koko Eating Bananas

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/koko-eating-bananas/

## Problem

Koko loves bananas. Return the minimum integer k such that she can eat all the bananas within h hours.

## Approach

Binary search on answer

## Explanation

Binary search smallest k with total hours <= h.

## Complexity

- Time: O(n log m)
- Space: O(1)

## Alternatives

Linear search on k.

## Common mistakes

Using floor division instead of ceil per pile.

## Learning notes

Monotonic feasibility enables search on speed.

## Solution

```python
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k):
            return sum(math.ceil(p / k) for p in piles)

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if hours(mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo

```
