from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        prev = [[board[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                live = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            live += prev[ni][nj]
                if prev[i][j]:
                    board[i][j] = 1 if live in (2, 3) else 0
                else:
                    board[i][j] = 1 if live == 3 else 0
