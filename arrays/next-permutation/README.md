# Next Permutation

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/next-permutation/

## Problem

A permutation of an array of integers is an arrangement of its members into a sequence. The next permutation of an array of integers is the next lexicographically greater permutation of its integer. If no such permutation exists, rearrange to the lowest possible order (ascending). Modify nums in-place.

## Approach

Lexicographic next permutation

## Explanation

Find pivot, swap with next larger, reverse suffix.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Generate all permutations.

## Common mistakes

Not reversing the entire suffix when no pivot exists.

## Learning notes

Classic in-place permutation algorithm.

## Solution

```python
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1 :] = reversed(nums[i + 1 :])

```
