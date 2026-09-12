# Set Matrix Zeroes

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/set-matrix-zeroes/

## Problem

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.

## Approach

In-place markers

## Explanation

Use first row/col as markers; handle col0 separately.

## Complexity

- Time: O(m*n)
- Space: O(1)

## Alternatives

Extra boolean matrices.

## Common mistakes

Overwriting markers too early.

## Learning notes

Marker technique saves space on matrices.

## Solution

```python
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        col0 = False
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0:
                matrix[i][0] = 0

```
