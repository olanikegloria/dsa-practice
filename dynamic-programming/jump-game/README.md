# Jump Game

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/jump-game/

## Problem

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.

## Approach

Greedy farthest-reach scan

## Explanation

Track the farthest index reachable so far. If the scan walks past that mark, the last index is impossible.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Right-to-left DP marking indices that can reach the end.

## Common mistakes

Returning as soon as a zero is seen, even when an earlier jump already passed it.

## Learning notes

The reachable prefix is a single moving boundary.

## Solution

```python
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, jump in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + jump)
        return True

```
