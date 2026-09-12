# Spiral Matrix

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/spiral-matrix/

## Problem

Given an m x n matrix, return all elements of the matrix in spiral order.

## Approach

Boundary shrinking

## Explanation

Peel layers top-right-bottom-left.

## Complexity

- Time: O(m*n)
- Space: O(1)

## Alternatives

Direction vectors.

## Common mistakes

Missing boundary checks.

## Learning notes

Layer-by-layer traversal pattern.

## Solution

```python
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        out = []
        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                out.append(matrix[top][c])
            top += 1
            for r in range(top, bottom + 1):
                out.append(matrix[r][right])
            right -= 1
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    out.append(matrix[bottom][c])
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    out.append(matrix[r][left])
                left += 1
        return out

```
