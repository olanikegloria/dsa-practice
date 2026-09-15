# Target Sum

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/target-sum/

## Problem

You are given an integer array nums and an integer target. You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers. Return the number of different expressions that you can build, which evaluates to target.

## Approach

DP over sum frequencies

## Explanation

Track count of reachable sums after each number +/- choice.

## Complexity

- Time: O(n * sum)
- Space: O(sum)

## Alternatives

Memoized recursion.

## Common mistakes

Using list instead of sparse map.

## Learning notes

Target sum is subset sum with signed choices.

## Solution

```python
from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for n in nums:
            nxt = defaultdict(int)
            for s, cnt in dp.items():
                nxt[s + n] += cnt
                nxt[s - n] += cnt
            dp = nxt
        return dp.get(target, 0)

```
