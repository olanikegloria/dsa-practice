# Single Number III

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/single-number-iii/

## Problem

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice, return the two single elements in any order.

## Approach

XOR partition

## Explanation

XOR all; split by differing bit; XOR each group.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Hash set of seen.

## Common mistakes

Using xor=0 partition incorrectly.

## Learning notes

Isolate any set bit where singles differ.

## Solution

```python
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        diff = xor & -xor
        a = b = 0
        for n in nums:
            if n & diff:
                a ^= n
            else:
                b ^= n
        return [a, b]

```
