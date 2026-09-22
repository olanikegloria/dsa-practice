from typing import List
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)
        for i, boss in enumerate(manager):
            if boss != -1:
                children[boss].append(i)

        def dfs(u: int) -> int:
            if not children[u]:
                return 0
            return informTime[u] + max(dfs(v) for v in children[u])

        return dfs(headID)
