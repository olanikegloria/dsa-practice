from typing import List
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = Counter(nums)
        keys = sorted(points)
        prev = -1
        take = 0
        skip = 0
        for k in keys:
            best_skip = max(take, skip)
            if k == prev + 1:
                take, skip = skip + k * points[k], best_skip
            else:
                take, skip = best_skip + k * points[k], best_skip
            prev = k
        return max(take, skip)
