from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                out.append(path[:])
                return
            for i, n in enumerate(nums):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(n)
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return out
