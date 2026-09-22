# Top K Frequent Words

**Topic:** heap  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/top-k-frequent-words/

## Problem

Given an array of strings words and an integer k, return the k most frequent strings. Sort by frequency descending, then lexicographically for ties.

## Approach

Counter + heap

## Explanation

Heap ordered by negative frequency then word for lex tie-break.

## Complexity

- Time: O(n + m log m)
- Space: O(m)

## Alternatives

Bucket sort by frequency.

## Common mistakes

Using max heap without lex tie handling.

## Learning notes

Tuple ordering gives correct tie-break.

## Solution

```python
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heap = [(-counts[w], w) for w in counts]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

```
