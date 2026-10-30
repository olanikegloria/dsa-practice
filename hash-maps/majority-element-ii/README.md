# Majority Element II

**Topic:** hash-maps  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/majority-element-ii/

## Problem

Given an integer array of size n, find all elements that appear more than floor(n / 3) times.

## Approach

Two-candidate voting

## Explanation

Boyer-Moore for two candidates; verify counts > n/3.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Hash map counts.

## Common mistakes

Skipping verification pass.

## Learning notes

At most two elements exceed n/3 frequency.

## Solution

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = None
        count1 = count2 = 0
        for n in nums:
            if c1 == n:
                count1 += 1
            elif c2 == n:
                count2 += 1
            elif count1 == 0:
                c1, count1 = n, 1
            elif count2 == 0:
                c2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = count2 = 0
        for n in nums:
            if n == c1:
                count1 += 1
            elif n == c2:
                count2 += 1
        out = []
        limit = len(nums) // 3
        if c1 is not None and count1 > limit:
            out.append(c1)
        if c2 is not None and count2 > limit and c2 != c1:
            out.append(c2)
        return out

```
