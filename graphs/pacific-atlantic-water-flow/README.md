# Pacific Atlantic Water Flow

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/pacific-atlantic-water-flow/

## Problem

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. Given an m x n integer matrix heights representing the height of each unit cell, return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

## Approach

Two reverse DFS searches from the borders

## Explanation

Walk uphill from each ocean. Cells that both searches visit can drain to both oceans.

## Complexity

- Time: O(m * n)
- Space: O(m * n)

## Alternatives

BFS from the same borders.

## Common mistakes

Flowing downhill from a cell instead of climbing from the ocean.

## Learning notes

Reversing the flow direction turns two oceans into two reachable sets.

## Solution

```python
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])

        def reach(starts: List[tuple[int, int]]) -> set[tuple[int, int]]:
            seen = set(starts)
            stack = list(starts)
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            return seen

        pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        both = reach(pacific) & reach(atlantic)
        return [[r, c] for r, c in both]

```
