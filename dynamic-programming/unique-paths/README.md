# Unique Paths

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/unique-paths/

## Problem

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time. Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

## Approach

Grid DP with one rolling row

## Explanation

Each cell is reachable from the left or from above, so a rolling row accumulates those two options.

## Complexity

- Time: O(m * n)
- Space: O(n)

## Alternatives

Combinatorics: C(m + n - 2, m - 1).

## Common mistakes

Off-by-one on the grid size, or resetting the first column.

## Learning notes

The first row and column stay 1 because there is only one way along an edge.

## Solution

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(1, m):
            for c in range(1, n):
                row[c] += row[c - 1]
        return row[-1]

```
