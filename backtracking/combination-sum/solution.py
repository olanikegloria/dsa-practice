from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out: List[List[int]] = []
        path: List[int] = []

        def dfs(i: int, remaining: int) -> None:
            if remaining == 0:
                out.append(path[:])
                return
            if i == len(candidates) or remaining < 0:
                return
            path.append(candidates[i])
            dfs(i, remaining - candidates[i])
            path.pop()
            dfs(i + 1, remaining)

        dfs(0, target)
        return out
