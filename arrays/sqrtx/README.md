# Sqrt(x)

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/sqrtx/

## Problem

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

## Approach

Binary search

## Explanation

Binary search integer mid where mid*mid <= x.

## Complexity

- Time: O(log x)
- Space: O(1)

## Alternatives

Newton's method.

## Common mistakes

Returning lo instead of hi after loop.

## Learning notes

Integer sqrt is a binary search on answer space.

## Solution

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        lo, hi = 2, x // 2
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == x:
                return mid
            if sq < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi

```
