# Partition Labels

**Topic:** hash-maps  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/partition-labels/

## Problem

You are given a string s consisting of lowercase English letters. Partition the string into as many parts as possible so that each letter appears in at most one part. Return a list of integers representing the size of these parts.

## Approach

Greedy with last-index map

## Explanation

Extend partition end to last occurrence of each letter seen.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Two-pass merge intervals.

## Common mistakes

Cutting before reaching farthest last index.

## Learning notes

Same idea as merge intervals on letter spans.

## Solution

```python
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        start = 0
        end = 0
        parts = []
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                parts.append(end - start + 1)
                start = i + 1
        return parts

```
