from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = {0}
        for n in nums:
            dp = dp | {s + n for s in dp if s + n <= target}
            if target in dp:
                return True
        return target in dp
