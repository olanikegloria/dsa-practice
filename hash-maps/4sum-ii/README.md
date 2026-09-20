# 4Sum II

**Topic:** hash-maps  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/4sum-ii/

## Problem

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.

## Approach

Hash map on two arrays

## Explanation

Count all a+b sums, then for each c+d add frequency of negated sum.

## Complexity

- Time: O(n^2)
- Space: O(n^2)

## Alternatives

Four nested loops.

## Common mistakes

Sign error on complement.

## Learning notes

Split four-sum into two two-sum problems.

## Solution

```python
from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ab = Counter(a + b for a in nums1 for b in nums2)
        count = 0
        for c in nums3:
            for d in nums4:
                count += ab[-(c + d)]
        return count

```
