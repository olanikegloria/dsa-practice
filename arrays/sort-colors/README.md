# Sort Colors

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/sort-colors/

## Problem

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

## Approach

Dutch national flag

## Explanation

Dutch national flag: three pointers partition 0/1/2.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Counting sort.

## Common mistakes

Not incrementing mid after swapping with lo.

## Learning notes

In-place three-way partition template.

## Solution

```python
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lo, mid, hi = 0, 0, len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1

```
