# Climbing Stairs

**Topic:** dynamic-programming  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/climbing-stairs/

## Problem

You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Approach

Bottom-up DP / Fibonacci

## Explanation

Ways(n) = ways(n-1) + ways(n-2); Fibonacci iteration.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Memoized recursion.

## Common mistakes

Off-by-one on base cases.

## Learning notes

Many DP problems reduce to recurrence relations.

## Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

```
