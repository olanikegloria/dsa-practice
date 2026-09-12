# Search a 2D Matrix

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/search-a-2d-matrix/

## Problem

You are given an m x n integer matrix matrix with the following properties: Each row is sorted in non-decreasing order. The first integer of each row is greater than the last integer of the previous row. Given an integer target, return true if target is in matrix or false otherwise.

## Approach

Staircase search

## Explanation

Start top-right; move left if too big else down.

## Complexity

- Time: O(m+n)
- Space: O(1)

## Alternatives

Flatten + binary search.

## Common mistakes

Starting from wrong corner.

## Learning notes

Sorted matrix allows elimination along row and column.

## Solution

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1
        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False

```
