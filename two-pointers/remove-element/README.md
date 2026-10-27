# Remove Element

**Topic:** two-pointers  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/remove-element/

## Problem

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. Return k, the number of elements not equal to val.

## Approach

Two pointers (write index)

## Explanation

Write non-val elements to front; return new length.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Two-pass filter.

## Common mistakes

Returning original length.

## Learning notes

In-place compaction pattern.

## Solution

```python
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k

```
