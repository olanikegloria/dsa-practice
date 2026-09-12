# Missing Number

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/missing-number/

## Problem

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

## Approach

Gauss sum formula

## Explanation

Expected sum minus actual sum reveals missing value.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

XOR all indices and values.

## Common mistakes

Overflow on large n (rare in constraints).

## Learning notes

Sum and XOR both solve missing-element problems.

## Solution

```python
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

```
