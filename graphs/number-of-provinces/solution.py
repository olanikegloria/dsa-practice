from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = [False] * n

        def dfs(i):
            seen[i] = True
            for j in range(n):
                if isConnected[i][j] and not seen[j]:
                    dfs(j)

        provinces = 0
        for i in range(n):
            if not seen[i]:
                provinces += 1
                dfs(i)
        return provinces
