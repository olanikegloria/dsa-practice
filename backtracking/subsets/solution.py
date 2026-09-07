from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out: List[List[int]] = []
        path: List[int] = []

        def dfs(i: int) -> None:
            if i == len(nums):
                out.append(path[:])
                return
            dfs(i + 1)
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return out
