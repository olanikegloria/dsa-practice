# Single Number

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/single-number/

## Problem

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with linear runtime and use only constant extra space.

## Approach

Bit XOR

## Explanation

XOR pairs cancel; leftover is the unique element.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Hash set (uses extra space).

## Common mistakes

Using sum arithmetic overflow tricks incorrectly.

## Learning notes

a ^ a = 0, a ^ 0 = a.

## Solution

```python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for n in nums:
            x ^= n
        return x

```
