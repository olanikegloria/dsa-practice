# Reorganize String

**Topic:** heap  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/reorganize-string/

## Problem

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same. Return any possible rearrangement or an empty string if not possible.

## Approach

Max heap

## Explanation

Always place the most frequent char not equal to previous; defer last pick.

## Complexity

- Time: O(n log k)
- Space: O(k)

## Alternatives

Place into even/odd slots by count.

## Common mistakes

Not deferring the previous character.

## Learning notes

Impossible when one char dominates (> half).

## Solution

```python
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(-c, ch) for ch, c in counts.items()]
        heapq.heapify(heap)
        prev = None
        out = []
        while heap:
            c, ch = heapq.heappop(heap)
            out.append(ch)
            if prev:
                heapq.heappush(heap, prev)
            prev = (c + 1, ch) if c + 1 else None
        return "" if len(out) != len(s) else "".join(out)

```
