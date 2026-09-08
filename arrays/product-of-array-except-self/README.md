# Product of Array Except Self

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/product-of-array-except-self/

## Problem

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

## Approach

Prefix and suffix products

## Explanation

Each answer is the product of everything to the left times everything to the right, so two sweeps replace division.

## Complexity

- Time: O(n)
- Space: O(1) extra besides the output

## Alternatives

Total product divided by each element, which fails when a zero is present.

## Common mistakes

Using division, or allocating separate prefix and suffix arrays when one output array is enough.

## Learning notes

When division is banned, a second sweep in reverse usually replaces it.

## Solution

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]
        return out

```
