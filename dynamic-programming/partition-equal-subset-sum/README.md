# Partition Equal Subset Sum

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/partition-equal-subset-sum/

## Problem

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

## Approach

0/1 knapsack set DP

## Explanation

Subset sum to total/2 using reachable sums set.

## Complexity

- Time: O(n * sum)
- Space: O(sum)

## Alternatives

2D boolean DP table.

## Common mistakes

Not early exiting when target found.

## Learning notes

Partition equal subset reduces to subset sum.

## Solution

```python
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = {0}
        for n in nums:
            dp = dp | {s + n for s in dp if s + n <= target}
            if target in dp:
                return True
        return target in dp

```
