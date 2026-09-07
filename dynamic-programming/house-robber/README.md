# House Robber

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/house-robber/

## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. Adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Approach

1D DP rolling state

## Explanation

For each house, take max(skip it, rob it + best two back).

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Explicit dp array.

## Common mistakes

Robbing adjacent houses.

## Learning notes

Adjacent-constraint DP is a Fibonacci cousin.

## Solution

```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = prev1 = 0
        for n in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + n)
        return prev1

```
