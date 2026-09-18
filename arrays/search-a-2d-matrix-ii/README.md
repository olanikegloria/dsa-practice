# Search a 2D Matrix II

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/search-a-2d-matrix-ii/

## Problem

Write an efficient algorithm that searches for a value target in an m x n integer matrix. Each row and column is sorted in ascending order.

## Approach

Staircase search

## Explanation

Start top-right; move left if too big else down.

## Complexity

- Time: O(m + n)
- Space: O(1)

## Alternatives

Binary search each row.

## Common mistakes

Starting from wrong corner.

## Learning notes

Sorted rows and columns give a monotonic walk.

## Solution

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            if val > target:
                col -= 1
            else:
                row += 1
        return False

```
