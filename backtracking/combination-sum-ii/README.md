# Combination Sum II

**Topic:** backtracking  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/combination-sum-ii/

## Problem

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in the combination.

## Approach

Backtracking with dedup

## Explanation

Sort, skip duplicate starts, use each candidate once.

## Complexity

- Time: O(2^n)
- Space: O(n)

## Alternatives

DP subset counting.

## Common mistakes

Not skipping equal values at same depth.

## Learning notes

Combination with reuse forbidden needs duplicate skipping.

## Solution

```python
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []
        path = []
        def dfs(start, remaining):
            if remaining == 0:
                out.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                dfs(i + 1, remaining - candidates[i])
                path.pop()
        dfs(0, target)
        return out

```
