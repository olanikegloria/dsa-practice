# Spiral Matrix II

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/spiral-matrix-ii/

## Problem

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

## Approach

Layer simulation

## Explanation

Fill outer layer clockwise, then shrink bounds.

## Complexity

- Time: O(n^2)
- Space: O(1) excluding output

## Alternatives

Direction vector walk.

## Common mistakes

Double-filling center on odd n.

## Learning notes

Mirror spiral matrix read pattern.

## Solution

```python
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        val = 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                matrix[top][j] = val
                val += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = val
                val += 1
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = val
                    val += 1
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = val
                    val += 1
                left += 1
        return matrix

```
