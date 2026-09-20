# Min Cost Climbing Stairs

**Topic:** dynamic-programming  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/min-cost-climbing-stairs/

## Problem

You are given an integer array cost where cost[i] is the cost of ith step on the staircase. Once you pay the cost, you can either climb one or two steps. Return the minimum cost to reach the top of the floor.

## Approach

DP with O(1) space

## Explanation

Rolling min cost to reach step i from the two previous steps.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Top-down memoization.

## Common mistakes

Paying cost of the top step (you may start past last index).

## Learning notes

Same recurrence as climbing stairs with weights.

## Solution

```python
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a, b = 0, 0
        for i in range(2, n + 1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b

```
