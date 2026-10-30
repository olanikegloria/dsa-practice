# Single Number II

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/single-number-ii/

## Problem

Given an integer array nums where every element appears three times except for one, which appears exactly once, find the single element and return it.

## Approach

Bit manipulation

## Explanation

Track bit counts mod 3 with ones and twos registers.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Sum bits per position.

## Common mistakes

XOR alone fails with triple repeats.

## Learning notes

State machine for mod-3 counts.

## Solution

```python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        for n in nums:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
        return ones

```
