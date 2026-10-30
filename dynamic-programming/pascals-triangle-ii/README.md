# Pascal's Triangle II

**Topic:** dynamic-programming  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/pascals-triangle-ii/

## Problem

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

## Approach

Iterative row generation

## Explanation

Build each row from previous using adjacent sums.

## Complexity

- Time: O(rowIndex^2)
- Space: O(rowIndex)

## Alternatives

Combinatorial multipliers.

## Common mistakes

1-index vs 0-index confusion.

## Learning notes

Only last row needed — rolling update.

## Solution

```python
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]
        return row

```
