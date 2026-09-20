# Binary Search

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/binary-search/

## Problem

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, return its index; otherwise return -1.

## Approach

Binary search

## Explanation

Standard binary search on sorted array.

## Complexity

- Time: O(log n)
- Space: O(1)

## Alternatives

Built-in bisect.

## Common mistakes

Infinite loop with wrong mid updates.

## Learning notes

Template for lower/upper bound variants.

## Solution

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

```
