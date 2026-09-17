# Jump Game II

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/jump-game-ii/

## Problem

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0. Each element nums[i] represents the maximum jump length from index i. Return the minimum number of jumps to reach index n - 1.

## Approach

Greedy BFS layers

## Explanation

Greedy: extend reachable range; count jumps at each layer boundary.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Dynamic programming.

## Common mistakes

Including the last index in the jump loop incorrectly.

## Learning notes

Treat indices as graph edges with weight 1.

## Solution

```python
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        farthest = 0
        jumps = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jumps += 1
                end = farthest
        return jumps

```
