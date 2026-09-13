# Permutations

**Topic:** backtracking  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/permutations/

## Problem

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

## Approach

Backtracking with used array

## Explanation

Build permutations by marking used indices.

## Complexity

- Time: O(n * n!)
- Space: O(n)

## Alternatives

Swap-based backtracking.

## Common mistakes

Not unmarking used on backtrack.

## Learning notes

Permutation = choose unused elements at each depth.

## Solution

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        path = []
        used = [False] * len(nums)
        def dfs():
            if len(path) == len(nums):
                out.append(path[:])
                return
            for i, n in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(n)
                dfs()
                path.pop()
                used[i] = False
        dfs()
        return out

```
