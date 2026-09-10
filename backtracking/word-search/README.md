# Word Search

**Topic:** backtracking  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/word-search/

## Problem

Given an m x n grid of characters board and a string word, return true if word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Approach

Backtracking on the grid

## Explanation

From each starting cell, walk adjacent unused letters. Mark the current cell so the same square is not reused on this path.

## Complexity

- Time: O(m * n * 4^L)
- Space: O(L)

## Alternatives

Trie + search when many words are queried at once.

## Common mistakes

Forgetting to restore a cell after a failed branch.

## Learning notes

In-place marking is cheaper than a separate visited set.

## Solution

```python
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            saved = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            board[r][c] = saved
            return found

        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))

```
