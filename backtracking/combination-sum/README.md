# Combination Sum

**Topic:** backtracking  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/combination-sum/

## Problem

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times.

## Approach

Backtracking with take-or-skip choices

## Explanation

At each candidate, either take it again or move to the next candidate. A negative remainder closes that branch.

## Complexity

- Time: O(2^(target/minCandidate)) in the worst case
- Space: O(target/minCandidate) recursion depth

## Alternatives

Bottom-up dynamic programming can build all combinations for every subtotal.

## Common mistakes

Advancing the index after taking a candidate, which incorrectly prevents reuse.

## Learning notes

The recursion index prevents duplicate orderings while the remaining target bounds the tree.

## Solution

```python
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out: List[List[int]] = []
        path: List[int] = []

        def dfs(i: int, remaining: int) -> None:
            if remaining == 0:
                out.append(path[:])
                return
            if i == len(candidates) or remaining < 0:
                return
            path.append(candidates[i])
            dfs(i, remaining - candidates[i])
            path.pop()
            dfs(i + 1, remaining)

        dfs(0, target)
        return out

```
