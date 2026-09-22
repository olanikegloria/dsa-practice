# Delete and Earn

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/delete-and-earn/

## Problem

You are given an integer array nums. You can pick any integer from nums and earn that many points, but you must delete every element equal to that integer minus one and plus one. Return the maximum number of points you can earn.

## Approach

DP on value line

## Explanation

House-robber on sorted unique values with aggregated points.

## Complexity

- Time: O(n + U) where U is value range
- Space: O(U)

## Alternatives

Full array dp up to max(nums).

## Common mistakes

Not merging duplicate value points.

## Learning notes

Adjacent values cannot both be taken.

## Solution

```python
from typing import List
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = Counter(nums)
        keys = sorted(points)
        prev = -1
        take = 0
        skip = 0
        for k in keys:
            best_skip = max(take, skip)
            if k == prev + 1:
                take, skip = skip + k * points[k], best_skip
            else:
                take, skip = best_skip + k * points[k], best_skip
            prev = k
        return max(take, skip)

```
