# Subsets

**Topic:** backtracking  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/subsets/

## Problem

Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

## Approach

Backtracking include/exclude

## Explanation

At each index, include or skip the number; record the path at the leaves.

## Complexity

- Time: O(n * 2^n)
- Space: O(n)

## Alternatives

Iterative: start from [[]] and append each number to existing subsets.

## Common mistakes

Mutating the same list without copying the path.

## Learning notes

Power set is the canonical include/exclude tree.

## Solution

```python
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out: List[List[int]] = []
        path: List[int] = []

        def dfs(i: int) -> None:
            if i == len(nums):
                out.append(path[:])
                return
            dfs(i + 1)
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return out

```
