# Rotate Image

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/rotate-image/

## Problem

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place.

## Approach

Transpose + reverse

## Explanation

Transpose then reverse each row for 90° clockwise.

## Complexity

- Time: O(n^2)
- Space: O(1)

## Alternatives

Layer rotation.

## Common mistakes

Rotating counter-clockwise by mistake.

## Learning notes

Matrix rotation decomposes into transpose/reverse.

## Solution

```python
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()

```
