# Sliding Window Maximum

**Topic:** heap  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/sliding-window-maximum/

## Problem

You are given an array of integers nums and an integer k. There is a sliding window of size k which moves from the very left to the very right. Return the max sliding window.

## Approach

Monotonic deque

## Explanation

Deque stores indices of decreasing values; front is window max.

## Complexity

- Time: O(n)
- Space: O(k)

## Alternatives

Heap with lazy deletion.

## Common mistakes

Forgetting to drop indices outside window.

## Learning notes

Each index enters and leaves deque once.

## Solution

```python
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        out = []
        for i, n in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] <= n:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                out.append(nums[dq[0]])
        return out

```
