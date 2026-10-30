# Pascal's Triangle

**Topic:** dynamic-programming  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/pascals-triangle/

## Problem

Given an integer numRows, return the first numRows of Pascal's triangle.

## Approach

Row-by-row construction

## Explanation

Each row starts with ones; interior is sum of two above.

## Complexity

- Time: O(n^2)
- Space: O(n^2)

## Alternatives

Combinatorics formula.

## Common mistakes

Off-by-one on inner loop bounds.

## Learning notes

Classic DP triangle build.

## Solution

```python
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = rows[i - 1][j - 1] + rows[i - 1][j]
            rows.append(row)
        return rows

```
