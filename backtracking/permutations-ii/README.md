# Permutations II

**Topic:** backtracking  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/permutations-ii/

## Problem

Given a collection of numbers nums that might contain duplicates, return all possible unique permutations in any order.

## Approach

Backtracking with dedupe

## Explanation

Sort; skip duplicate branches when previous equal unused.

## Complexity

- Time: O(n * n!)
- Space: O(n)

## Alternatives

Count with multiset.

## Common mistakes

Duplicate permutations in output.

## Learning notes

Standard duplicate-skip on sorted input.

## Solution

```python
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                out.append(path[:])
                return
            for i, n in enumerate(nums):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(n)
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return out

```
