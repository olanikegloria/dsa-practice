# Rotate Array

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/rotate-array/

## Problem

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative. Modify nums in-place.

## Approach

Three reversals

## Explanation

Reverse whole array, then reverse first k and remainder.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Cyclic replacements or extra array.

## Common mistakes

Forgetting k %= n.

## Learning notes

Reversal trick avoids O(n) extra space.

## Solution

```python
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return
        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)

```
